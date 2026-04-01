# 🏛️ HyperGold AI Hub Governance

---

## 👑 Code Owners

All contributions require review from at least one Code Owner.

| Area | Owner |
|------|-------|
| Core infrastructure | @welshDog |
| Frameworks | @welshDog |
| Models | @welshDog |
| Datasets | @welshDog |
| Agents | @welshDog |
| Security | @welshDog |

See [CODEOWNERS](.github/CODEOWNERS) for the full machine-readable file.

---

## 🔍 Review Process

1. **PR opened** → CI/CD auto-triggers
2. **Automated checks pass** → human review assigned
3. **Review window**: 48 hours for standard PRs, 24 hours for security patches
4. **Approval**: 1 Code Owner approval required for merge
5. **Merge strategy**: Squash merge to keep history clean

---

## ⚖️ Conflict Resolution

1. Raise a disagreement as a GitHub Issue tagged `governance`
2. Discussion window: 72 hours
3. Code Owner makes final call if no consensus
4. Escalation: open a community vote via GitHub Discussions

---

## 🔐 Security Policy

See [SECURITY.md](SECURITY.md) for vulnerability reporting.

---

## 📜 Versioning Policy

- **Semver** (MAJOR.MINOR.PATCH) enforced across all assets
- Breaking changes require a MAJOR version bump + migration guide
- CI/CD blocks merges that break backwards-compatibility without a version bump

---

## 🏷️ Release Cadence

- **Weekly**: patch releases (bug fixes)
- **Monthly**: minor releases (new assets, non-breaking)
- **Quarterly**: major releases (structural changes)
