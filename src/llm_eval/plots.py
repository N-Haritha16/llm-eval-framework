import os
import math
import matplotlib.pyplot as plt
import numpy as np


def _to_list(value):
    """
    Normalize metric outputs to list of floats
    """
    if isinstance(value, list):
        return [float(v) for v in value]
    return [float(value)]


def generate_plots(results: dict, output_dir: str) -> None:
    """
    Generate required evaluation plots:
    - Histogram for each metric
    - Radar chart comparing metrics
    """
    os.makedirs(output_dir, exist_ok=True)

    metric_names = list(results.keys())

    # -------- Histogram plots --------
    for metric, raw_scores in results.items():
        scores = _to_list(raw_scores)

        plt.figure()
        plt.hist(scores, bins=10)
        plt.title(f"{metric} Score Distribution")
        plt.xlabel("Score")
        plt.ylabel("Frequency")

        path = os.path.join(output_dir, f"{metric}_hist.png")
        plt.savefig(path)
        plt.close()

    # -------- Radar chart --------
    radar_scores = [sum(_to_list(results[m])) / len(_to_list(results[m])) for m in metric_names]

    angles = np.linspace(0, 2 * math.pi, len(metric_names), endpoint=False).tolist()
    angles += angles[:1]
    radar_scores += radar_scores[:1]

    plt.figure(figsize=(6, 6))
    ax = plt.subplot(111, polar=True)
    ax.plot(angles, radar_scores)
    ax.fill(angles, radar_scores, alpha=0.25)

    ax.set_thetagrids(np.degrees(angles[:-1]), metric_names)
    ax.set_title("LLM Metrics Comparison")

    radar_path = os.path.join(output_dir, "metrics_radar.png")
    plt.savefig(radar_path)
    plt.close()
