"""Tests for HyperSearch semantic search engine."""
import sys
import json
import pytest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))
from search import HyperSearch


@pytest.fixture
def hub():
    return HyperSearch(index_path="metadata/index.json")


def test_index_loads(hub):
    """Index must load and contain assets."""
    assert len(hub.assets) > 0


def test_keyword_search_returns_results(hub):
    results = hub._keyword_search("agent", top_k=5)
    assert isinstance(results, list)


def test_query_returns_ranked_results(hub):
    results = hub.query("autonomous agent", top_k=3)
    assert len(results) <= 3
    for r in results:
        assert "name" in r
        assert "path" in r
        assert "score" in r


def test_list_all(hub):
    assets = hub.list_all()
    assert isinstance(assets, list)
    assert all("name" in a for a in assets)


def test_get_by_type(hub):
    tools = hub.get_by_type("tool")
    for t in tools:
        assert t["type"] == "tool"


def test_metadata_schema():
    """Every asset in the index must have required fields."""
    with open("metadata/index.json") as f:
        data = json.load(f)
    required = {"name", "path", "type", "tags", "version", "license"}
    for asset in data["assets"]:
        missing = required - set(asset.keys())
        assert not missing, f"Asset '{asset.get('name')}' missing fields: {missing}"
