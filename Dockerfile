FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install --upgrade pip \
    && pip install -r requirements.txt \
    && pip install fastapi uvicorn

CMD ["python", "-m", "llm_eval.cli", "examples/config.yaml", "results"]
