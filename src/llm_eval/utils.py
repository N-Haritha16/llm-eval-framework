import json
import csv
import yaml
import os

REQUIRED_FIELDS = ["query", "expected_answer", "model_answer", "retrieved_contexts"]

def load_config(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        if path.endswith((".yml", ".yaml")):
            return yaml.safe_load(f)
        elif path.endswith(".json"):
            return json.load(f)
        else:
            raise ValueError(f"Unsupported config format: {path}")

def load_benchmark(path: str) -> list:
    if path.endswith(".jsonl"):
        data = []
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    data.append(json.loads(line))
    elif path.endswith(".json"):
        with open(path, "r", encoding="utf-8") as f:
            data = [json.loads(line) for line in f if line.strip()]
    elif path.endswith(".csv"):
        with open(path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            data = list(reader)
    else:
        raise ValueError(f"Unsupported dataset format: {path}")

    for i, sample in enumerate(data):
        for field in REQUIRED_FIELDS:
            if field not in sample:
                raise ValueError(f"Sample {i} missing required field '{field}'")
    return data
