FROM python:3.10-slim

WORKDIR /app

# Copy project files
COPY . .

# Upgrade pip
RUN pip install --upgrade pip

# Install PyTorch CPU (separately)
RUN pip install torch --index-url https://download.pytorch.org/whl/cpu

# Install remaining dependencies
RUN pip install -r requirements.txt

# Default command (run evaluation)
CMD ["python", "-m", "llm_eval.cli", "examples/config.yaml", "results"]
