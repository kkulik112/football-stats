from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
import os
import pandas as pd

dataframe = pd.read_csv("data/argentina-league2-form.csv")
embeddings = OllamaEmbeddings(model="mxbai-embed-large")

db_location = "./chroma_langchain_db"

db_exists = os.path.exists(db_location)

if not db_exists:
    documents = []
    ids = []
    for index, row in dataframe.iterrows():
        doc = Document(page_content=row["Team"],
                       metadata={"group": row["Group"], "form": row["Form"]},
                       id = str(index)                       
                       )
        ids.append(str(index))
        documents.append(doc)
        
vector_story = Chroma(
    collection_name="teams_current_form",
    persist_directory=db_location,
    embedding_function=embeddings,
)

if not db_exists:
    vector_story.add_documents(documents=documents, ids=ids)
    
retriever = vector_story.as_retriever(
    search_kwargs={"k": 100}
)

