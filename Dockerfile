FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt \
    --index-url https://download.pytorch.org/whl/cpu

# Default: Run evaluation
CMD ["python", "-m", "llm_eval.cli", "examples/config.yaml", "results"]
