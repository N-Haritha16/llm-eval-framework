from fastapi import FastAPI

app = FastAPI(title="LLM Evaluation Framework API")

@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "llm-eval-framework"
    }
