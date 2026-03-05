FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

# This line installs your package so `llm_eval` is importable
RUN pip install -e .

CMD ["python", "-m", "llm_eval.cli", "examples/config.yaml"]
