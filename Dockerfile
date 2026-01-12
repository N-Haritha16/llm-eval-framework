FROM python:3.10

WORKDIR /app
COPY . .

RUN pip install --upgrade pip \
    && pip install -r requirements.txt

CMD ["python", "-m", "llm_eval.cli", "examples/config.yaml", "results"]
