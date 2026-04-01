# 📊 HyperGold AI Hub Metrics Dashboard

Tracks community health and repository growth.

## Metrics Tracked

| Metric | Source | Update Frequency |
|--------|--------|------------------|
| Total assets | `metadata/index.json` | Every merge |
| PR open/close time | GitHub API | Daily |
| Issue resolution time | GitHub API | Daily |
| Stars / forks / watchers | GitHub API | Daily |
| CI/CD pass rate | GitHub Actions | Every PR |
| Top contributors | GitHub API | Weekly |
| Downloads per asset | GitHub Releases | Weekly |

## Running the Dashboard

```bash
python dashboard/metrics.py --output dashboard/latest.json
```

## Integration

Dashboard data feeds into GitHub Actions summary on every release.
