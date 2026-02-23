from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, Any


def generate_json_report(results: Dict[str, Any], path: str) -> None:
    """Write full results dict to a JSON file."""
    out_path = Path(path)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    with out_path.open("w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)


def generate_markdown_report(aggregates: Dict[str, Dict[str, float]], path: str) -> None:
    """
    Write a Markdown report with aggregate statistics.

    Expects `aggregates` in the form:
    {
        "bleu": {"mean": ..., "median": ..., "std": ...},
        ...
    }
    """
    out_path = Path(path)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    lines = []
    lines.append("# LLM Evaluation Report\n")
    lines.append("## Aggregate Metrics\n")
    lines.append("| Metric | Mean | Median | Std Dev |")
    lines.append("|--------|------|--------|---------|")

    for name, stats in aggregates.items():
        lines.append(
            f"| {name} | {stats['mean']:.4f} | {stats['median']:.4f} | {stats['std']:.4f} |"
        )

    with out_path.open("w", encoding="utf-8") as f:
        f.write("\n".join(lines))


def generate_json(results: Dict[str, Any], path: str) -> None:
    """
    Backward-compatible wrapper for old tests.

    Old tests import `generate_json` from `llm_eval.reports`.
    Internally we just call `generate_json_report`.
    """
    generate_json_report(results, path)
