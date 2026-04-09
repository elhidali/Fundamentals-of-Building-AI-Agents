
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import os
import httpx 

load_dotenv()


model_id = "nvidia/nemotron-3-super-120b-a12b:free"

llm = ChatOpenAI(
    model=model_id,
    openai_api_base=os.getenv("OPENROUTER_BASE_URL"),
    openai_api_key=os.getenv("OPENROUTER_API_KEY"),
    http_client=httpx.Client(verify=False)

)


response = llm.invoke("what is the score of the match between athletico madrid and barcelona yesterday?")

print(response.content)
