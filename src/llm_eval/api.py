from fastapi import FastAPI
from pydantic import BaseModel
from llm_eval.config import load_config  # use your real path
from llm_eval.evaluator import evaluate  # use your real path

app = FastAPI(title="LLM Eval API")


@app.get("/health")
def health():
    return {"status": "ok"}


class EvalRequest(BaseModel):
    config_path: str = "examples/config.yaml"


@app.post("/evaluate")
def run_evaluation(body: EvalRequest):
    config = load_config(body.config_path)
    results = evaluate(config)
    return results
