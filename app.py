# app.py
from fastapi import FastAPI
from pydantic import BaseModel
#from langchain_community.llms import LlamaCpp
from langchain.chains.retrieval_qa.base import RetrievalQA
from vectorstore import get_vectorstore
from langchain.llms import Ollama

class Query(BaseModel):
    q: str


app = FastAPI()
vs = get_vectorstore()

# swap in your model of choice
#llm = LlamaCpp(model_path="/Users/balusasidharanpillai/llmmodels/llama-2-7b.ggmlv3.q2_K.bin", n_ctx=2048)
llm = Ollama(model="deepseek-r1:7b")
qa = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    
    retriever=vs.as_retriever(search_kwargs={"k": 5}),
    return_source_documents=True
)


# Pass `embeddings` to your vectorstore, not a function

@app.post("/search/")
async def search(req: Query):
    res = qa({"query": req.q})
    return {
        "answer": res["result"],
    }