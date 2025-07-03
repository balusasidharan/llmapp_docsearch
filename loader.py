"""Module for loading and splitting documents using LangChain loaders and text splitters."""
from pathlib import Path
from langchain_community.document_loaders import UnstructuredPDFLoader
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


"""Load and split documents from a folder."""
def load_and_split(folder: str ):
    raw_docs = []
    print(f"Loading documents from {folder}")
    for path in Path(folder).glob("*"):
        if path.name.startswith("."):
            continue
        if path.suffix.lower() == ".pdf":
            raw_docs.extend(UnstructuredPDFLoader(str(path)).load())
        else:
            raw_docs.extend(TextLoader(str(path)).load())
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    return splitter.split_documents(raw_docs)

