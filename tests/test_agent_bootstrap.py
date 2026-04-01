"""Integration tests for agent bootstrap flow."""
import sys
import json
import pytest
from pathlib import Path
from unittest.mock import patch, MagicMock

sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))
import agent_bootstrap as ab


def test_search_assets_finds_agents(tmp_path):
    """search_assets should find agent-type assets."""
    meta_dir = tmp_path / "metadata"
    meta_dir.mkdir()
    index = {
        "assets": [
            {"name": "Self-Upgrade Agent", "type": "agent",
             "tags": ["autonomous", "upgrade"], "path": "agents/self-upgrade-agent/",
             "version": "1.0.0", "license": "MIT"}
        ]
    }
    with open(meta_dir / "index.json", "w") as f:
        json.dump(index, f)
    results = ab.search_assets(str(tmp_path), "autonomous agent upgrade")
    assert len(results) == 1
    assert results[0]["name"] == "Self-Upgrade Agent"


def test_self_upgrade_runs_without_error():
    """self_upgrade should complete without raising."""
    assets = [{"name": "Mock Model", "type": "model", "version": "1.0.0"}]
    ab.self_upgrade("/tmp", assets)  # Should not raise


def test_log_levels():
    """log() should run for all levels without error."""
    for level in ["INFO", "OK", "WARN", "ERROR", "STEP"]:
        ab.log(f"Test {level}", level)
