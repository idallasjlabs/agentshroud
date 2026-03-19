---
title: ci-workflows
type: config
file_path: .github/workflows/
tags: [ci, github-actions, testing]
related: [Configuration/pytest.ini, Dependencies/All Dependencies]
status: documented
---

# CI Workflows

**Location:** `.github/workflows/` (if configured)
**Tool:** GitHub Actions

## Purpose

Automated CI pipeline for AgentShroud. Runs tests, linting, security scans, and image builds on every push and pull request.

## Expected Pipeline (Inferred)

```
Push / PR
  ├── Test
  │   ├── pytest -q (gateway tests)
  │   ├── Coverage check (≥80%)
  │   └── ruff + black formatting
  ├── Security
  │   ├── gitleaks (secret scanning)
  │   ├── trivy (image scanning)
  │   └── pip-audit (dependency CVEs)
  └── Build
      ├── Build gateway image
      └── Build bot image
```

## Key Test Command

```bash
pytest -q --asyncio-mode=auto
```

## Coverage Threshold

Per `CLAUDE.md`:
- ≥80% test coverage required on new/modified code

## Related Notes

- [[Configuration/pytest.ini]] — Test configuration
- [[Dependencies/All Dependencies]] — Test dependencies (pytest, pytest-asyncio)
