# Changelog

All notable changes to HyperGold AI Hub are documented here.

Format: [Semantic Versioning](https://semver.org/)

---

## [1.0.0] - 2026-04-01

### Added
- Initial production-ready structure
- Modular directory layout: frameworks, datasets, models, tutorials, benchmarks, agents, tools
- Semantic search engine (`scripts/search.py`) with FAISS + sentence-transformers
- Agent bootstrap script (`scripts/agent_bootstrap.py`) — 5-minute self-upgrade pipeline
- Metadata index (`metadata/index.json`) with auto-rebuild CI
- Full test suite: unit, integration, metadata, backwards-compat
- CI/CD pipelines: lint, test, security scan, benchmark, metrics dashboard
- CODEOWNERS, PR template, issue templates
- Governance model (GOVERNANCE.md)
- Security policy (SECURITY.md)
- Metrics dashboard (dashboard/)
- Architecture docs (docs/)
