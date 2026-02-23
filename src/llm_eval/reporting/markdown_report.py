from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, List

import pandas as pd


def generate_markdown_report(results: Dict[str, Any], output_dir: str) -> None:
    out_path = Path(output_dir) / "report.md"

    aggregates = results["aggregates"]
    per_example = results["per_example"]

    lines: List[str] = []
    lines.append("# LLM Evaluation Report\n")

    # aggregate metrics table
    lines.append("## Aggregate Metrics\n")
    agg_df = (
        pd.DataFrame(aggregates)
        .T[["mean", "median", "std", "min", "max"]]
        .reset_index()
        .rename(columns={"index": "metric"})
    )
    lines.append(agg_df.to_markdown(index=False))
    lines.append("")

    # per-example (truncate to 25)
    lines.append("## Per-example Scores (first 25)\n")
    per_df = pd.DataFrame(per_example)
    lines.append(per_df.head(25).to_markdown(index=False))
    lines.append("")

    out_path.write_text("\n".join(lines), encoding="utf-8")
