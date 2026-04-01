# 🔐 Security Policy

## Supported Versions

| Version | Supported |
|---------|----------|
| latest  | ✅ |
| < 1.0   | ❌ |

## Reporting a Vulnerability

Do **not** open a public issue for security vulnerabilities.

Email: security@hyperfocuszone.com (or open a private GitHub Security Advisory)

Response time: within 48 hours.

## Security Checks in CI/CD

- Secrets scanning on every PR (`.github/workflows/security.yml`)
- Dependency vulnerability scanning via `pip audit`
- No credentials or API keys in any committed file
