from langchain.vectorstores import PGVector
from langchain_community.embeddings import HuggingFaceEmbeddings
from sqlalchemy import create_engine
import os
from loader import load_and_split

def index_docs():
    # Set up connection and embedding model
    connection_string = os.environ["PGVECTOR_CONNECTION_STRING"]
    engine = create_engine(connection_string)
    embed_model = HuggingFaceEmbeddings(model_name="all-mpnet-base-v2")
    
    # Load and split your documents
    docs = load_and_split("/Users/balusasidharanpillai/vectordocs")  # Should return a list of langchain Document objects

    # Insert documents into the vectorstore (this will create the collection/table if it doesn't exist)
    PGVector.from_documents(
        documents=docs,
        embedding=embed_model,
        connection=engine,
        collection_name="pgvectordocuments"  # Use your preferred collection/table name
    )

if __name__ == "__main__":
    print("Indexing documents...")
    index_docs()