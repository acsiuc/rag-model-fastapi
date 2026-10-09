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

    answer = generate(question, chunks)
    file_paths = []

    for content, file_path, distance in chunks:
        if file_path  not in file_paths:
            file_paths.append(file_path)
            

    return {'answer': answer, 'file_paths': file_paths}
