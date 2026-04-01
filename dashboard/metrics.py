#!/usr/bin/env python3
"""
HyperGold AI Hub Metrics Collector
Fetches GitHub API data and produces a metrics snapshot.
"""

import json
import os
import argparse
from datetime import datetime

try:
    import requests
    HAS_REQUESTS = True
except ImportError:
    HAS_REQUESTS = False

REPO = "welshDog/AI"
GH_API = "https://api.github.com"


def get_repo_stats(token: str = None) -> dict:
    if not HAS_REQUESTS:
        return {"error": "requests not installed"}
    headers = {"Accept": "application/vnd.github+json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    r = requests.get(f"{GH_API}/repos/{REPO}", headers=headers)
    if r.status_code != 200:
        return {"error": r.status_code}
    d = r.json()
    return {
        "stars": d.get("stargazers_count"),
        "forks": d.get("forks_count"),
        "watchers": d.get("subscribers_count"),
        "open_issues": d.get("open_issues_count"),
        "size_kb": d.get("size")
    }


def collect_metrics(output_path: str):
    token = os.environ.get("GITHUB_TOKEN")
    stats = get_repo_stats(token)
    with open("metadata/index.json") as f:
        index = json.load(f)
    metrics = {
        "collected_at": datetime.utcnow().isoformat() + "Z",
        "total_assets": index["_meta"]["total_assets"],
        "github": stats
    }
    with open(output_path, "w") as f:
        json.dump(metrics, f, indent=2)
    print(f"✅ Metrics saved to {output_path}")
    print(json.dumps(metrics, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="dashboard/latest.json")
    args = parser.parse_args()
    collect_metrics(args.output)
