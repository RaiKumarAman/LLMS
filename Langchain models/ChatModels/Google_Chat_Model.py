from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

model=ChatGoogleGenerativeAI(model='gemini-1.5-pro', temperature=0)
result=model.invoke("Suggest me names of 5 suspense thriller movies")
# result=model.invoke("What is the capital of India")
print(result.content)