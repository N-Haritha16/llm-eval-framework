from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Dict, List

from .config import DatasetConfig

REQUIRED_FIELDS = ["query", "expected_answer", "model_answer", "retrieved_contexts"]


def _validate_sample(sample: Dict) -> Dict:
    missing = [k for k in REQUIRED_FIELDS if k not in sample]
    if missing:
        raise ValueError(f"Sample missing required fields: {missing}")
    if not isinstance(sample["retrieved_contexts"], list):
        raise ValueError("retrieved_contexts must be a list of strings")
    return sample


def load_dataset(cfg: DatasetConfig) -> List[Dict]:
    path = Path(cfg.path)
    if not path.exists():
        raise FileNotFoundError(f"Dataset file not found: {path}")

    if cfg.format == "jsonl":
        samples: List[Dict] = []
        with path.open("r", encoding="utf-8") as f:
            for line in f:
                if not line.strip():
                    continue
                sample = json.loads(line)
                samples.append(_validate_sample(sample))
        return samples

    if cfg.format == "csv":
        samples: List[Dict] = []
        with path.open("r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                rc = row.get("retrieved_contexts")
                if isinstance(rc, str):
                    row["retrieved_contexts"] = json.loads(rc)
                samples.append(_validate_sample(row))
        return samples

    raise ValueError(f"Unsupported dataset format: {cfg.format}")
