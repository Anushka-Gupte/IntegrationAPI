from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langserve import add_routes
from langchain_community.llms import Ollama
import uvicorn
import os
os.environ["PYTHONUTF8"] = "1"

app = FastAPI(
    title="Langchain server",
    version="1.0",
    description="A simple API Server"
)

#ollama : mistral model
llm = Ollama(model="mistral")
prompt = ChatPromptTemplate.from_template("Write as essay about {topic} in about 100 words")

add_routes(
    app,
    prompt|llm,
    path="/essay"
)

if __name__ == "__main__":
    uvicorn.run(app,host="localhost",port=8000)