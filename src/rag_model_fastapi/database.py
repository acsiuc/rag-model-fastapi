from dotenv import load_dotenv
import psycopg
from pgvector.psycopg import register_vector
import os

load_dotenv()

def get_connection():

    my_password = os.environ['POSTGRES_PASSWORD']
    connection_string = f"postgresql://postgres:{my_password}@localhost:5432/rag"
    connection = psycopg.connect(connection_string)

    register_vector(connection)

    return connection

def populate_database(connection, file_path, embeddings, chunks):

    for chunk_index, chunk in enumerate(chunks):
        connection.execute('INSERT INTO chunks(file_path, chunk_index, content, embedding) '
        'VALUES(%s, %s, %s, %s)', (file_path, chunk_index, chunk, embeddings[chunk_index]))
       

def path_exists(connection, file_path):

    return connection.execute('SELECT 1 FROM chunks WHERE file_path = %s LIMIT 1', (file_path,)).fetchone() is not None
     

def closest_chunks(connection, question_embedding, number_of_chunks = 5):

    return connection.execute('SELECT content, file_path, embedding <=> %s as distance ' \
    'FROM chunks ' \
    'ORDER BY distance ' \
    'LIMIT %s', (question_embedding, number_of_chunks)).fetchall()
