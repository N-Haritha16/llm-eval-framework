from __future__ import annotations

import json
import logging
from pathlib import Path
from typing import List, Literal, Optional

import yaml
from pydantic import BaseModel, Field, validator

logger = logging.getLogger(__name__)


class LLMJudgeConfig(BaseModel):
    provider: Literal["openai", "anthropic"]
    model: str
    api_key_env: str = Field(..., description="Env var name for API key")
    temperature: float = 0.0
    max_retries: int = 3
    backoff_seconds: float = 1.0


class MetricsConfig(BaseModel):
    metrics: List[str] = Field(
        default_factory=lambda: [
            "bleu",
            "rouge_l",
            "bertscore",
            "faithfulness",
            "context_relevance",
            "answer_relevance",
        ]
    )
    bleu_max_ngram: int = 4


class DatasetConfig(BaseModel):
    path: str
    format: Literal["jsonl", "csv"] = "jsonl"


class ModelsConfig(BaseModel):
    # you can extend this later; for now just keep outputs path info if needed
    prediction_path: Optional[str] = None


class EvalConfig(BaseModel):
    dataset: DatasetConfig
    models: ModelsConfig = ModelsConfig()
    metrics: MetricsConfig = MetricsConfig()
    llm_judge: Optional[LLMJudgeConfig] = None
    output_dir: str = "results"
    log_level: Literal["DEBUG", "INFO", "WARNING", "ERROR"] = "INFO"

    @validator("output_dir")
    def _ensure_output_dir(cls, v: str) -> str:
        Path(v).mkdir(parents=True, exist_ok=True)
        return v


def load_config(path: str | Path) -> EvalConfig:
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"Config file not found: {path}")

    if path.suffix.lower() in {".yml", ".yaml"}:
        raw = yaml.safe_load(path.read_text(encoding="utf-8"))
    elif path.suffix.lower() == ".json":
        raw = json.loads(path.read_text(encoding="utf-8"))
    else:
        raise ValueError(f"Unsupported config format: {path.suffix}")

    try:
        return EvalConfig(**raw)
    except Exception as exc:
        logger.exception("Invalid configuration")
        raise ValueError(f"Invalid configuration: {exc}") from exc
