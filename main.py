import os
import requests
from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever

model = OllamaLLM(model="llama3.2")

template = """You are a helpful assistant. Answer the question based on the provided context.
You will rely on csv file with "form" data which shows wins (W), losses (L), and draws (D) for each team.
Try not to make up information, but if you do not know the answer, say "I don't know".
Also don't try to give code solutions, just answer the question.
Teams: {teams}
Question: {question}
"""

prompt = ChatPromptTemplate.from_template(template)

chain = prompt | model

while True:
    print("\n\n---------------------------------------")
    question = input("Enter your question (or type 'exit' to quit): ")
    print("\n\n")
    if question.lower() == 'exit' or question.lower() == 'q':
        break

    teams = retriever.invoke(question)
    result = chain.invoke({
        "teams": teams,
        "question": question        
    })
    print(result)

