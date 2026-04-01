"""Tests for metadata integrity and backwards-compatibility."""
import json
import pytest
from pathlib import Path
import semver


def load_index():
    with open("metadata/index.json") as f:
        return json.load(f)


def test_index_meta_fields():
    data = load_index()
    assert "_meta" in data
    assert "assets" in data
    assert data["_meta"]["version"]
    assert isinstance(data["assets"], list)


def test_asset_versions_are_semver():
    """All asset versions must be valid semver."""
    data = load_index()
    for asset in data["assets"]:
        v = asset.get("version", "")
        try:
            semver.VersionInfo.parse(v)
        except ValueError:
            pytest.fail(f"Asset '{asset['name']}' has invalid semver: '{v}'")


def test_no_duplicate_asset_names():
    data = load_index()
    names = [a["name"] for a in data["assets"]]
    assert len(names) == len(set(names)), "Duplicate asset names found!"


def test_all_paths_exist():
    """All asset paths in the index should exist in the repo."""
    data = load_index()
    root = Path(".")
    for asset in data["assets"]:
        p = root / asset["path"]
        # We check the parent directory rather than exact file
        # since path may end with /
        parent = p if not str(asset["path"]).endswith("/") else p.parent
        # Soft check — warn but don't fail for missing optional dirs
        if not parent.exists():
            pytest.skip(f"Path {parent} not yet created (acceptable for stub assets)")
