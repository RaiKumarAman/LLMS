from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser 
load_dotenv()

model=ChatGoogleGenerativeAI(model='gemini-1.5-flash-latest', temperature=0)

prompt= PromptTemplate(
    template="Generate 5 interesting facts about {topic}",
    input_variables=['topic']
)

parser= StrOutputParser()

chain = prompt| model | parser

result= chain.invoke({'topic':'IPL'})

print(result)

chain.get_graph().print_ascii()

# install gandalf to use this 