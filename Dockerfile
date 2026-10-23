FROM python:3.12-slim@sha256:a6e34c598f2467ed0e9a8d349809fcd8b5c603269512df273a0bb1784edc11b1
RUN pip install uv
WORKDIR /app
COPY uv.lock pyproject.toml /app/
RUN uv sync --no-install-project
COPY src /app/src
COPY README.md /app/
RUN uv sync 
CMD ["uv", "run", "fastapi", "run", "src/rag_model_fastapi/api/endpoints.py"]