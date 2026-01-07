FROM python:3.10-slim

WORKDIR /app


RUN apt-get update && apt-get install -y \
    git \
    && rm -rf /var/lib/apt/lists/*


RUN pip install --no-cache-dir torch --index-url https://download.pytorch.org/whl/cpu

COPY . .


RUN pip install -e .

CMD ["python", "-m", "llm_eval.cli", "examples/config.yaml", "results"]
