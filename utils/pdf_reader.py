# import fitz
#
# def pdf_read(pdf_file):
#     if pdf_file is None:
#         return ""
#
#     pdf = fitz.open(
#         stream=pdf_f  ile.read(),
#         filetype="pdf")
#     text = ""
#     for page in pdf:
#         text += page.get_text()
#     pdf.close()
#     return text
import os

from langchain_community.document_loaders import PyPDFLoader
import tempfile

def pdf_read(uploaded_file):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
        temp_file.write(uploaded_file.read())
        temp_path = temp_file.name

    try:
        loader = PyPDFLoader(temp_path)
        documents = loader.load()

    finally:
        os.unlink(temp_path)

    return documents
