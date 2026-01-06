from llm_eval.reports import generate_json
import tempfile, os

def test_generate_json():
    results = {"bleu": [0.5]}
    with tempfile.TemporaryDirectory() as d:
        path = os.path.join(d, "report.json")
        generate_json(results, path)
        assert os.path.exists(path)
