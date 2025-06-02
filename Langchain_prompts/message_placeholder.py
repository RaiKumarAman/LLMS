from langchain_core.prompts import MessagesPlaceholder, ChatPromptTemplate

chat_template=ChatPromptTemplate([
    ("system", "You are a helpful customer assistant."),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{user_input}")
])

chat_history=[]

with open(r'C:\Users\Aman\OneDrive\Documents\Coding\Python\Langchain\Langchain_prompts\chat_history.txt') as f:
    chat_history.extend(f.readlines())

print(chat_history)

prompt=chat_template.invoke({"user_input":"Refund status" , "chat_history":chat_history})

print(prompt)

