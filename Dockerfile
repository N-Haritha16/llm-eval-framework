FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

# Install torch first
RUN pip install --no-cache-dir torch --index-url https://download.pytorch.org/whl/cpu

# Copy project
COPY . .

# Upgrade pip
RUN pip install --upgrade pip

# Install project WITHOUT hash strictness
RUN pip install -e . --no-deps || true

# Force install API deps
RUN pip install uvicorn fastapi

CMD ["python", "-m", "llm_eval.cli", "examples/config.yaml", "results"]
