from langchain_tavily import TavilySearch
from dotenv import load_dotenv

load_dotenv()

tavily_tool = TavilySearch(
    max_results=5,
    topic="general",
    description="""
    Search the web for current or external information.

    Use this tool for recent news, current events, policy, weather,
    sports, technology, or information not available in the
    local databases.

    Do not use this tool for questions that can be answered
    by the local databases.
    """
    )

# response = tavily_tool.invoke("What is weather of dhaka today")
# print(response)