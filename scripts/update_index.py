#!/usr/bin/env python3
"""
Auto-crawl all contribution folders and rebuild the metadata/index.json
Run by CI/CD on every merge to main.
"""

import json
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).parent.parent
SEARCH_DIRS = ["frameworks", "datasets", "models", "tutorials", "benchmarks", "agents", "tools"]
INDEX_OUT = ROOT / "metadata" / "index.json"


def crawl_assets():
    assets = []
    for d in SEARCH_DIRS:
        base = ROOT / d
        if not base.exists():
            continue
        for folder in base.iterdir():
            meta_file = folder / "metadata.json"
            if meta_file.exists():
                with open(meta_file) as f:
                    meta = json.load(f)
                meta["path"] = str(folder.relative_to(ROOT)) + "/"
                assets.append(meta)
    return assets


def rebuild_index():
    assets = crawl_assets()
    index = {
        "_meta": {
            "version": "1.0.0",
            "description": "HyperGold AI Hub global metadata index. Auto-updated by CI/CD.",
            "last_updated": datetime.utcnow().isoformat() + "Z",
            "total_assets": len(assets)
        },
        "assets": assets
    }
    INDEX_OUT.parent.mkdir(exist_ok=True)
    with open(INDEX_OUT, "w") as f:
        json.dump(index, f, indent=2)
    print(f"✅ Index rebuilt: {len(assets)} assets → {INDEX_OUT}")


if __name__ == "__main__":
    rebuild_index()
