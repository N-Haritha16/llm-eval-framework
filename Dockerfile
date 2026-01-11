FROM python:3.10-slim

WORKDIR /app

# Copy reqs first for caching
COPY requirements.txt .

# Install with retries, no-cache, upgrade pip
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt --timeout=100 --retries=3 && \
    pip install --no-cache-dir fastapi "uvicorn[standard]" --timeout=100 --retries=3

COPY . .

RUN python -c "import uvicorn; print(f'uvicorn {uvicorn.__version__} OK')"

CMD ["python", "-m", "llm_eval.cli", "examples/config.yaml", "results"]