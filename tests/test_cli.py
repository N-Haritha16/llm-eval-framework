import pytest
from pathlib import Path


@pytest.mark.skip("Skipping CLI end-to-end test in this environment.")
def test_cli_end_to_end(tmp_path: Path) -> None:
    pass
