def execute_sql_tool(db, schema, llm, question):
    prompt = f"""
You are an expert SQLite query generator.

Database Schema:
{schema}

User Question:
{question}

Rules:
1. Return EXACTLY one SQLite SELECT query.
2. Return ONLY SQL.
3. Do NOT use markdown.
4. Do NOT explain anything.
5. Use ONLY tables and columns from the schema.
6. Never invent a table.
7. Never invent a column.
8. Quote columns containing spaces using double quotes.
9. Never use INSERT, UPDATE, DELETE, DROP, ALTER, CREATE, or PRAGMA.
10. If the question cannot be answered from this database, return exactly:

NOT_FOUND
"""

    # Generate SQL
    sql = llm.invoke(prompt).content.strip()

    # Database doesn't contain the information
    if sql.upper() == "NOT_FOUND":
        return {
            "status": "not_found",
            "message": "The requested information is not available in this database."
        }

    # Safety check
    sql_upper = sql.upper()

    if not sql_upper.startswith("SELECT"):
        return {
            "status": "error",
            "message": "Only SELECT queries are allowed."
        }

    try:

        # Execute SQL
        rows = db.run(sql)

        # No rows found
        if not rows:

            return {
                "status": "not_found",
                "message": "No matching records were found."
            }

        return {
            "status": "success",
            "rows": rows
        }

    except Exception as e:

        return {
            "status": "error",
            "message": f"SQL execution failed: {e}"
        }