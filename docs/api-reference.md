# 📖 API Reference

## HyperSearch (`scripts/search.py`)

### `HyperSearch(index_path)`
- `index_path`: path to `metadata/index.json`

### `.query(query_text, top_k=5) → List[Dict]`
Semantic (or keyword fallback) search. Returns ranked assets.

### `.list_all() → List[Dict]`
Returns all assets in the index.

### `.get_by_type(asset_type) → List[Dict]`
Filter by type: `model`, `dataset`, `framework`, `agent`, `tool`, `tutorial`, `benchmark`.

---

## Agent Bootstrap (`scripts/agent_bootstrap.py`)

### `clone_repo(target_dir) → float`
Clones the hub. Returns elapsed seconds.

### `search_assets(repo_dir, query) → List[Dict]`
Keyword search over the local index.

### `self_upgrade(repo_dir, assets) → None`
Applies discovered assets.

### `run_tests(repo_dir) → bool`
Runs pytest suite. Returns True if all pass.

---

## Metadata Schema

See [CONTRIBUTING.md](../CONTRIBUTING.md#metadata-json-template) for the full `metadata.json` schema.
