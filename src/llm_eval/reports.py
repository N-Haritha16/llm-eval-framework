import json
from pathlib import Path

def generate_json_report(results, path):
    path = Path(path)

    # If user passed a file path → use it directly
    if path.suffix == ".json":
        file_path = path
    else:
        path.mkdir(parents=True, exist_ok=True)
        file_path = path / "report.json"

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)


def generate_markdown_report(results, path):
    path = Path(path)

    if path.suffix == ".md":
        file_path = path
    else:
        path.mkdir(parents=True, exist_ok=True)
        file_path = path / "report.md"

    with open(file_path, "w", encoding="utf-8") as f:
        f.write("# LLM Evaluation Report\n\n")
        for metric, score in results.items():
            f.write(f"## {metric}\n")
            f.write(f"- Score: {score}\n\n")


# Aliases for tests
generate_json = generate_json_report
generate_markdown = generate_markdown_report
