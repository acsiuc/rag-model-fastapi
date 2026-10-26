
from rag_model_fastapi.database import get_connection, path_exists, populate_database
from rag_model_fastapi.embedding import embed
from rag_model_fastapi.ingestion.chunking import chunk_text
from rag_model_fastapi.ingestion.loader import load_all_files
from rag_model_fastapi.paths import documentation_path


def ingest():
    connection = get_connection()
    files = load_all_files(documentation_path)

    for path_text_dict in files:
        path = str(path_text_dict['path'].relative_to(documentation_path))
        try:
            if path_exists(connection, path):
                continue
            else:
                list_of_chunks = chunk_text(path_text_dict['text'])
                embeddings = embed(list_of_chunks)
                populate_database(connection, path, embeddings, list_of_chunks)
                connection.commit()
        except Exception as e: # noqa: BLE001
            connection.rollback()
            print(f"Path {path} failed: {e}")

    connection.close()


if __name__ == "__main__":
    ingest()