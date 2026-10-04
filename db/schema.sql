CREATE EXTENSION vector;
CREATE TABLE chunks (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    content TEXT NOT NULL,
    chunk_index INTEGER NOT NULL,
    file_path TEXT NOT NULL,
    embedding vector(768) NOT NULL,
    UNIQUE (file_path, chunk_index)
);