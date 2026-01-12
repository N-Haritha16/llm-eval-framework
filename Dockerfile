FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install --upgrade pip
RUN pip install torch --index-url https://download.pytorch.org/whl/cpu
RUN pip install -r requirements.txt

# IMPORTANT for src/ layout
RUN pip install -e .

CMD ["python", "-m", "llm_eval.cli", "examples/config.yaml", "results"]
