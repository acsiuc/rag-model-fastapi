FROM python:3.12-slim
RUN pip install uv
WORKDIR /app
COPY uv.lock pyproject.toml /app/
RUN uv sync --no-install-project
COPY src /app/src
COPY README.md /app/
RUN uv sync 
CMD ["uv", "run", "fastapi", "run", "src/rag_model_fastapi/api/endpoints.py"]
