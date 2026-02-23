from __future__ import annotations

from pathlib import Path
from typing import Any, Dict

import matplotlib.pyplot as plt
import numpy as np


def generate_histograms(results: Dict[str, Any], output_dir: str) -> None:
    """Create histogram PNGs for each metric from per-example scores."""
    out_dir = Path(output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    per_example = results.get("per_example", [])
    if not per_example:
        return

    # collect metric names (exclude text fields)
    all_keys = per_example[0].keys()
    metric_names = [
        k
        for k in all_keys
        if k not in {"query", "expected_answer", "model_answer"}
    ]

    for metric in metric_names:
        scores = [row.get(metric, 0.0) for row in per_example]
        if not scores:
            continue

        plt.figure()
        plt.hist(scores, bins=10, range=(0.0, 1.0))
        plt.title(f"{metric} score distribution")
        plt.xlabel("score")
        plt.ylabel("count")

        out_path = out_dir / f"{metric}_histogram.png"
        plt.savefig(out_path, bbox_inches="tight")
        plt.close()


def generate_radar_chart(results: Dict[str, Any], output_dir: str) -> None:
    """Create a radar chart PNG from aggregate mean scores per metric."""
    out_dir = Path(output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    aggregates = results.get("aggregates", {})
    if not aggregates:
        return

    metrics = list(aggregates.keys())
    means = [aggregates[m]["mean"] for m in metrics]

    num_vars = len(metrics)
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False)
    means_cycle = np.concatenate((means, [means[0]]))
    angles_cycle = np.concatenate((angles, [angles[0]]))

    plt.figure()
    ax = plt.subplot(111, polar=True)
    ax.plot(angles_cycle, means_cycle, "o-", linewidth=2)
    ax.fill(angles_cycle, means_cycle, alpha=0.25)
    ax.set_thetagrids(angles * 180 / np.pi, metrics)
    ax.set_ylim(0.0, 1.0)
    ax.set_title("Aggregate metric scores (mean)")

    out_path = out_dir / "metrics_radar.png"
    plt.savefig(out_path, bbox_inches="tight")
    plt.close()


def generate_plots(results: Dict[str, Any], output_dir: str) -> None:
    """
    Backward-compatible wrapper used by old tests.

    Calls both histogram and radar generation.
    """
    generate_histograms(results, output_dir)
    generate_radar_chart(results, output_dir)
