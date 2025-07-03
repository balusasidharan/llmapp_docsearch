# postgres_indexer.py
import os, uuid
from sqlalchemy import create_engine, Column, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base, Session
from pgvector.sqlalchemy import Vector
from sentence_transformers import SentenceTransformer
from loader import load_and_split

# 1. DB connection
DB_URI = os.getenv("DATABASE_URL", "postgresql://localhost:5432/docsearch")
engine = create_engine(DB_URI)
Base = declarative_base()

# 2. Table mapping
class Document(Base):
    __tablename__ = "documents"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    content = Column(Text, nullable=False)
    embedding = Column(Vector(768), nullable=False)  # match embed dim

Base.metadata.create_all(engine)

# 3. Embed + upsert
def index_docs():
    model = SentenceTransformer("all-mpnet-base-v2")
    docs = load_and_split("/Users/balusasidharanpillai/vectordocs")
    with Session(engine) as session:
        for doc in docs:
            print(f"Indexing document: {doc.page_content}")
            emb = model.encode(doc.page_content).tolist()
            session.merge(Document(
                id=uuid.uuid4(),
                content=doc.page_content,
                embedding=emb
            ))
        session.commit()

if __name__ == "__main__":
    print("Indexing documents...")
    index_docs()