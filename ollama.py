from langchain.llms import Ollama

llm = Ollama(model="deepseek-r1:7b")  
print(llm("What’s the capital of France?"))