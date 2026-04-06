from __future__ import annotations

import base64
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BUILD_DIR = ROOT / ".build"
OUTPUT_PATH = ROOT / "site-source.zip"


def main() -> None:
    parts = sorted(BUILD_DIR.glob("site-source.zip.b64.*"))
    if not parts:
        raise FileNotFoundError("No build fragments found for site-source.zip")

    encoded = "".join(
        part.read_text(encoding="utf-8").replace("\ufeff", "").strip()
        for part in parts
    )
    OUTPUT_PATH.write_bytes(base64.b64decode(encoded))


if __name__ == "__main__":
    main()
