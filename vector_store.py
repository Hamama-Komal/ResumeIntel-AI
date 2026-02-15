from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter

def create_vector_store(text: str):
    # Split text into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=100
    )
    docs = text_splitter.create_documents([text])
    
    # Initialize Embeddings
    embeddings = OpenAIEmbeddings()
    
    # Build the FAISS index
    vector_db = FAISS.from_documents(docs, embeddings)
    return vector_db

# MUST BE NAMED query_vector_store to match your main.py import
def query_vector_store(vector_db, query: str):
    """
    Searches the vector database and returns a string of results.
    """
    if not vector_db:
        return "No resume processed yet."
        
    docs = vector_db.similarity_search(query, k=3)
    return "\n\n".join([doc.page_content for doc in docs])