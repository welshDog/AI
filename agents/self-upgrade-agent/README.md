# 🤖 Self-Upgrade Agent

An autonomous agent template that clones HyperGold AI Hub, discovers compatible assets via semantic search, and applies upgrades — all within 5 minutes on standard cloud hardware.

## Installation

```bash
pip install -r ../../requirements.txt
```

## Usage

```bash
python ../../scripts/agent_bootstrap.py --task self-upgrade --query "autonomous agent" --timeout 300
```

## API Reference

| Function | Description |
|----------|------------|
| `clone_repo(target_dir)` | Shallow-clone the hub |
| `search_assets(repo_dir, query)` | Keyword/semantic search |
| `self_upgrade(repo_dir, assets)` | Apply discovered upgrades |
| `run_tests(repo_dir)` | Validate post-upgrade |

## Performance

- Clone: ~5s (shallow)
- Search: <1s
- Upgrade: ~2s per asset
- Total: <60s typical

## License

MIT
