from types import SimpleNamespace
from unittest.mock import patch


def test_cli_main_wires_dependencies():
    with patch("llm_eval.cli.load_config") as mock_load, \
         patch("llm_eval.cli.evaluate") as mock_eval, \
         patch("llm_eval.cli.generate_json_report") as mock_json, \
         patch("llm_eval.cli.generate_markdown_report") as mock_md:

        # Fake config with output_dir attribute
        mock_load.return_value = SimpleNamespace(output_dir="dummy_output_dir")

        # Fake evaluation result structure
        mock_eval.return_value = {
            "per_example": [],
            "aggregates": {},  # or minimal dict your cli uses
        }

        from llm_eval.cli import main

        main("dummy_config.yaml", "overridden_dir")

        mock_load.assert_called_once_with("dummy_config.yaml")
        mock_eval.assert_called_once()
        mock_json.assert_called_once()
        mock_md.assert_called_once()
