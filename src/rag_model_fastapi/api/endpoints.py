from fastapi import FastAPI
from pydantic import BaseModel

from rag_model_fastapi.database import get_connection
from rag_model_fastapi.generation.generation import generate
from rag_model_fastapi.retrieval.retrieval import retrieve

app = FastAPI()

class Ask(BaseModel):
    question: str


@app.post('/ask')
def question_asked(user: Ask):
    connection = get_connection()
    question = user.question
    chunks = retrieve(connection, question)

    connection.close()

    return generate(question, chunks)
