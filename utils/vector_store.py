from langchain_chroma import Chroma
from utils.embeddings import embeddings

def vector_save(chunks):
    db = Chroma.from_documents(
        documents = chunks,
        embedding = embeddings,
        persist_directory=('./chroma_db')
    )
    print(db.get())

