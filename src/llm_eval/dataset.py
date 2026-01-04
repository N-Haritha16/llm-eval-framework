import json

def load_benchmark(path):
    with open(path) as f:
        return [json.loads(line) for line in f]
