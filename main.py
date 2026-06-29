import os

from tools.hospitals_tool import hospitals_tool
from tools.institution_tool import institution_tool
from tools.restaurants_tool import restaurants_tool
from tools.web_search_tool import tavily_tool


from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from dotenv import load_dotenv

from langchain_core.messages import ToolMessage, AIMessage

load_dotenv()


tools = [
    institution_tool,
    hospitals_tool,
    restaurants_tool,
    tavily_tool,
]



endpoint = "https://models.github.ai/inference"

llm = ChatOpenAI(
    model="openai/gpt-4.1-mini",
    openai_api_key=os.getenv("GITHUB_TOKEN"),
    openai_api_base=endpoint,
    temperature=0.5,
)


# response = llm.invoke("What is captital of Bangladesh")
# print(response.content)



system_prompts = """ 
You are a helpful AI assistant.

Use the available tools to answer user questions accurately.
Prefer local database tools whenever possible.
Use Tavily only for current or external information that is not available in the local databases.
If multiple tools are needed, use them in the appropriate order.
Never make up information. If the answer cannot be found, say so politely.
Provide clear and concise responses. 
"""


agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt=system_prompts
)


# response = agent.invoke(
#     {"messages":"What is the healthcare policy of Bangladesh?"}
# )

# print(response["messages"][-1].content)



while True:
    user_input = input("User: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Exiting the AI assistant. Goodbye!")
        break

    response = agent.invoke({"messages": user_input})
    print()
    for msg in response["messages"]:
        if isinstance(msg, ToolMessage):
            print(f"[TOOL: {msg.name}] →", msg.content)
        elif isinstance(msg, AIMessage) and msg.tool_calls:
            print(f"[AGENT CALLED TOOL]:", msg.tool_calls)

    print("\nAI Assistant:", response["messages"][-1].content)
    print("-" * 50)  # Separator for clarity