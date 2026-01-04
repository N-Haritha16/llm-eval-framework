FROM python:3.10
WORKDIR /app
COPY . .
RUN pip install -e .
CMD ["llm-eval", "run", "--config", "examples/config.yaml", "--output", "results"]
