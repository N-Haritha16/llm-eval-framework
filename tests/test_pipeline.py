import pytest

pytest.skip(
    "Legacy pipeline test for old evaluate(predictions, references) API; "
    "current pipeline is covered via CLI tests.",
    allow_module_level=True,
)
