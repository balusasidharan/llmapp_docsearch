# vectorstore.py
import os
from langchain.vectorstores import PGVector
from langchain.embeddings import SentenceTransformerEmbeddings
from sqlalchemy import create_engine


def get_vectorstore():
    # Get the connection string from the environment variable
    connection_string = os.environ.get("PGVECTOR_CONNECTION_STRING")
    if not connection_string:
        raise ValueError("PGVECTOR_CONNECTION_STRING environment variable is not set.")

    # Create the SQLAlchemy engine
    engine = create_engine(connection_string)

    # Initialize the embeddings model
    embed_model = SentenceTransformerEmbeddings(
    model_name="all-mpnet-base-v2"
   
)

    # Return the PGVector instance (connect to existing collection)
    return PGVector(
        connection=engine,
        connection_string=connection_string,
        embedding_function=embed_model,
        collection_name = "pgvectordocuments"  # Change as needed
      
        )

if __name__ == "__main__":
    vs = get_vectorstore()
    print(vs)   
    answer = vs.similarity_search("What is Balu's birthdate?")
    print(answer)
