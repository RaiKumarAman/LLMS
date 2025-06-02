from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st

load_dotenv()

st.header("Research tool")
model=ChatGoogleGenerativeAI(model='gemini-1.5-flash-latest', temperature=0)

user_input=st.text_input("Enter your query here")

if st.button("Submit"):
    result=model.invoke(user_input)
    st.write(result.content)
