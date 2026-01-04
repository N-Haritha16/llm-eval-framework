def generate_markdown(results, path):
    with open(path, "w") as f:
        f.write("# LLM Evaluation Report\n\n")
        for metric, stats in results.items():
            f.write(f"## {metric}\n")
            for k, v in stats.items():
                f.write(f"- {k}: {v}\n")
            f.write("\n")
