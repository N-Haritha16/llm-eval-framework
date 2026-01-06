import json
import yaml


def load_config(path: str) -> dict:
    """
    Load YAML configuration file
    """
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_benchmark(path: str) -> list:
    """
    Load benchmark dataset from JSONL file
    """
    data = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            data.append(json.loads(line))
    return data
