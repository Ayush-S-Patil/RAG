import streamlit as st
# from utils.file_handler import save_text
from utils.text_splitter import text_splitter
from utils.embeddings import embed
from utils.vector_store import vector_save
from langchain_core.documents import Document

from utils.pdf_reader import pdf_read
st.title("AI PDF CHATBOT")
st.write("Ask question on your pdf")
uploaded_file = st.file_uploader("Upload your files", type=["pdf"], max_upload_size=400)


if uploaded_file is not None:
    st.success(f"Uploaded: {uploaded_file.name}")
st.write("No file selected")

if st.button("Process PDF",icon="🤖"):
    documents = pdf_read(uploaded_file)
    chunks = text_splitter(documents)
    vector_save(chunks)
    st.success("Text Extracted Successfully and chunked as well")
    st.write(chunks)
    st.write(vector_save(chunks))
    print(type(chunks))
    print(type(chunks[0]))