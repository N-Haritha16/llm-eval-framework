import json
import os


def generate_json(results: dict, output_path: str) -> None:
    """
    Save evaluation results as JSON
    """
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)


def generate_markdown(results: dict, output_path: str) -> None:
    """
    Save evaluation results as Markdown
    """
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("# LLM Evaluation Report\n\n")
        for metric, score in results.items():
            f.write(f"## {metric}\n")
            f.write(f"- Score: {score}\n\n")
