from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict


def generate_json_report(results: Dict[str, Any], output_dir: str) -> None:
    out_dir = Path(output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    out_path = out_dir / "report.json"
    out_path.write_text(json.dumps(results, indent=2), encoding="utf-8")
