import json

def generate_json_report(results, path):
    with open(path, "w") as f:
        json.dump(results, f, indent=2)