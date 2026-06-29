import os
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv


load_dotenv()

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.github.ai/inference"
model = "openai/gpt-4.1-mini"


llm = ChatOpenAI(
    model_name=model,
    openai_api_key=token,
    openai_api_base=endpoint,
    temperature=0.5,
)


# response = llm.invoke("What is the captial of france")
# print(response.content)