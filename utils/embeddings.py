from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()
apikey = os.getenv("GEMINI_API_KEY")
# print(os.getenv("GEMINI_API_KEY"))
embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-2-preview",api_key=apikey)


def embed(chunks):
    vector = embeddings.embed_documents(chunks)
    return vector[0]
