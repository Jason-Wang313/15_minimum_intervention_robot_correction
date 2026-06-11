import json
import zipfile
from io import BytesIO
from pathlib import Path

import requests


ROOT = Path(__file__).resolve().parents[1]
PAPER = ROOT / "paper"
DOCS = ROOT / "docs"
STATUS = DOCS / "template_status.json"

OFFICIAL_TEMPLATE_URL = "https://github.com/ICLR/Master-Template/raw/master/iclr2026.zip"
AUTHOR_GUIDE_URL = "https://iclr.cc/Conferences/2026/AuthorGuide"


def main() -> None:
    PAPER.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    status = {
        "official_author_guide": AUTHOR_GUIDE_URL,
        "template_url": OFFICIAL_TEMPLATE_URL,
        "downloaded": False,
        "extracted": [],
        "warnings": [],
    }
    try:
        response = requests.get(OFFICIAL_TEMPLATE_URL, timeout=45, headers={"User-Agent": "robotics-paper-template-fetch/1.0"})
        response.raise_for_status()
        status["downloaded"] = True
        archive_path = PAPER / "iclr2026.zip"
        archive_path.write_bytes(response.content)
        with zipfile.ZipFile(BytesIO(response.content)) as zf:
            for name in zf.namelist():
                base = Path(name).name
                if base in {"iclr2026_conference.sty", "iclr2026_conference.bst"}:
                    target = PAPER / base
                    target.write_bytes(zf.read(name))
                    status["extracted"].append(base)
        missing = [f for f in ["iclr2026_conference.sty", "iclr2026_conference.bst"] if not (PAPER / f).exists()]
        if missing:
            status["warnings"].append(f"Missing expected template files: {missing}")
    except Exception as exc:
        status["warnings"].append(f"Template retrieval failed: {exc}")
        print(f"WARN: template retrieval failed: {exc}")
    finally:
        STATUS.write_text(json.dumps(status, indent=2), encoding="utf-8")
        print(json.dumps(status, indent=2))


if __name__ == "__main__":
    main()
