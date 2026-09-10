# def text_splitter(text):
#     chunks = []
#     chunk_size = 500
#     for i in range(0, len(text), chunk_size):
#         chunks.append(text[i:i+500])
#     return chunks
#
#

from langchain_text_splitters import RecursiveCharacterTextSplitter
def text_splitter(text):
    text_split_obj = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    texts = text_split_obj.split_documents(text)
    return texts