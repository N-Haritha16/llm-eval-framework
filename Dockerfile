FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    pip install --no-cache-dir fastapi uvicorn[standard]

COPY . .

# Verify uvicorn
RUN python -c "import uvicorn; print('uvicorn ready:', uvicorn.__version__)"

CMD ["python", "-m", "llm_eval.cli", "examples/config.yaml", "results"]