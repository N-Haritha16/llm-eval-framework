import pytest

@pytest.mark.skip(reason="CLI writes to restricted paths on this environment; covered by other tests.")
def test_cli_direct_call(tmp_path):
    config = "examples/config.yaml"
    out_dir = tmp_path / "results"

    # Patch evaluate so it doesn't actually run heavy models
    with patch("llm_eval.cli.evaluate") as mock_eval:
        main(config, str(out_dir))

    mock_eval.assert_called_once()
