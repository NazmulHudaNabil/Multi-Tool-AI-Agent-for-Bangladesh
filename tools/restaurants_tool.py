import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT))

from langchain_community.utilities import SQLDatabase
from langchain.tools import tool
from utils.sql_executor import execute_sql_tool
from utils.llm import llm




db_path = ROOT / "data" / "sql" / "resturants.db"
db = SQLDatabase.from_uri(f"sqlite:///{db_path}")
SCHEMA = db.get_table_info()


# print(db.get_table_info())


@tool
def restaurants_tool(question: str):
    """Search the Bangladesh restaurants database."""
    return execute_sql_tool(db, SCHEMA, llm, question)