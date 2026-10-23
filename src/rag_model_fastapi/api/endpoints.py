from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from psycopg import OperationalError
from pydantic import BaseModel

from rag_model_fastapi.database import get_connection
from rag_model_fastapi.generation.generation import generate
from rag_model_fastapi.retrieval.retrieval import retrieve

app = FastAPI()

origins = [
    'http://localhost:5173',
    "http://localhost:8080"
    ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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

@app.get('/health')
def get_health():

    try :
        connection = get_connection()
        connection.close()
        return {'status': 'OK'}
    except OperationalError:
        raise HTTPException(status_code = 503, detail = "Service Unavailable")

    
    

