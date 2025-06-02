from langchain_core.prompts import ChatPromptTemplate


chat_template=ChatPromptTemplate([
    ("system", "You are a helpful {domain} assistant."),
    ("human", "{user_input}")
])

prompt=chat_template.invoke({"domain":"cinephile","user_input":"Name movie that has feel same as Indiana Jones"})

print(prompt)