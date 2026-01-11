FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

# Install core ML deps
RUN pip install --upgrade pip
RUN pip install torch --index-url https://download.pytorch.org/whl/cpu

# Copy project
COPY . .

# Install runtime deps manually (NO HASH CHECK)
RUN pip install \
    typer pyyaml nltk rouge-score bert-score matplotlib \
    fastapi uvicorn

# Default: run evaluation
CMD ["python", "-m", "llm_eval.cli", "examples/config.yaml", "results"]
