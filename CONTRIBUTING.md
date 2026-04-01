# 🤝 Contributing to HyperGold AI Hub

Welcome, BROski! Every contribution makes this the most powerful AI resource on the planet. 🌍

---

## 📋 Contribution Checklist

Before opening a PR, every contribution **must** include:

- [ ] `metadata.json` in your contribution folder (see template below)
- [ ] `README.md` with installation, API reference, and usage examples
- [ ] License declaration
- [ ] Tests in the `tests/` directory
- [ ] Backwards-compatibility notes (if updating an existing asset)

---

## 📂 Where to Put Things

| Type | Directory | Example |
|------|-----------|--------|
| ML Framework | `frameworks/<name>/` | `frameworks/pytorch/` |
| Dataset | `datasets/<name>/` | `datasets/imagenet-mini/` |
| Pre-trained Model | `models/<name>/` | `models/gpt2-small/` |
| Tutorial | `tutorials/<topic>/` | `tutorials/fine-tuning-llm/` |
| Benchmark | `benchmarks/<name>/` | `benchmarks/glue/` |
| Agent Template | `agents/<name>/` | `agents/self-upgrade-agent/` |
| Tool/Script | `tools/<name>/` | `tools/data-preprocessor/` |

---

## 🏷️ metadata.json Template

```json
{
  "name": "Your Asset Name",
  "version": "1.0.0",
  "type": "model | dataset | framework | tutorial | benchmark | agent | tool",
  "description": "One-line description for semantic search indexing.",
  "tags": ["nlp", "transformer", "pytorch"],
  "license": "MIT",
  "author": "your-github-username",
  "created_at": "2026-04-01",
  "updated_at": "2026-04-01",
  "compatibility": {
    "python": ">=3.9",
    "frameworks": ["pytorch>=2.0"],
    "os": ["linux", "windows", "macos"]
  },
  "api_reference": "README.md#api",
  "usage_example": "README.md#usage",
  "performance_metrics": {},
  "backwards_compatible": true,
  "breaking_changes": []
}
```

---

## 🔄 PR Process

1. Fork the repo
2. Create a feature branch: `git checkout -b feat/my-awesome-ai-thing`
3. Add your contribution following the checklist above
4. Run tests locally: `python -m pytest tests/ -v`
5. Open a PR using the [PR template](.github/PULL_REQUEST_TEMPLATE.md)
6. CI/CD will auto-run — fix any failures
7. A code owner will review within 48 hours

---

## 🛡️ Security

Never commit API keys, weights files over 100MB (use Git LFS or external links), or datasets without verified licensing. See [SECURITY.md](SECURITY.md).
