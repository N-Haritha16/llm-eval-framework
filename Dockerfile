FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install --upgrade pip \
    && pip install -e . \
    && pip install fastapi uvicorn pytest pytest-cov

CMD ["python", "-m", "llm_eval.cli", "examples/config.yaml", "results"]
