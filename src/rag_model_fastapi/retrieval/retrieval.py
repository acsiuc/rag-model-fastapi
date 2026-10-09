from rag_model_fastapi.database import closest_chunks
from rag_model_fastapi.embedding import embed


def retrieve(connection, question, number_of_chunks = 5):
    question_embedding = embed([question])[0]

    return closest_chunks(connection, question_embedding, number_of_chunks)