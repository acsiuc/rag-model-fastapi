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

def populate_database(connection, file_path, embedding, chunks):

    if path_exists(connection, file_path):
        pass
    else:
        connection.execute('INSERT')
       

def path_exists(connection, file_path):

    return connection.execute('SELECT 1 FROM chunks WHERE file_path = %s LIMIT 1', (file_path,)).fetchone() is not None
     

