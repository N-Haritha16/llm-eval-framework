# Updated Dockerfile - Jan 2026

FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && rm -rf /var/lib/apt/lists/*

COPY . .

RUN pip install --upgrade pip
RUN pip install -e .

CMD ["python", "-m", "llm_eval.cli", "examples/config.yaml", "results"]
