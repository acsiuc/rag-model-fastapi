from rag_model_fastapi.database import closest_chunks
from rag_model_fastapi.embedding import embed


def retrieve(connection, question):
    question_embedding = embed([question])[0]

    return closest_chunks(connection, question_embedding)