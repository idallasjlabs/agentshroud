---
type: community
cohesion: 0.14
members: 14
---

# Module Group 301

**Cohesion:** 0.14 - loosely connected
**Members:** 14 nodes

## Members
- [[Block Destructive Branch Workflow]] - code - .github/workflows/block-destructive-branch.yml
- [[CI Benchmark Regression Job (macos-latest)]] - code - .github/workflows/ci.yml
- [[CI Coverage Floor 84% (--cov-fail-under=84)]] - concept - .github/workflows/ci.yml
- [[CI DAST Scan Job (Nuclei, workflow_dispatch only)]] - code - .github/workflows/ci.yml
- [[CI Docs Drift Check Job (version consistency)]] - code - .github/workflows/ci.yml
- [[CI Gitleaks Secret Scanning Job]] - code - .github/workflows/ci.yml
- [[CI Leak Gate (ResourceWarningPytestUnraisableExceptionWarning fatal on ubuntu-3.11 only)]] - rationale - .github/workflows/ci.yml
- [[CI Lint Job (black, isort, flake8)]] - code - .github/workflows/ci.yml
- [[CI Pipeline Workflow]] - code - .github/workflows/ci.yml
- [[CI SOUL.md Freshness Check Job (90-day limit)]] - code - .github/workflows/ci.yml
- [[CI Security Scan Job (pip-audit)]] - code - .github/workflows/ci.yml
- [[CI Startup Smoke Tests (static) Job]] - code - .github/workflows/ci.yml
- [[CI Test Job (matrix ubuntumacos x 3.113.13)]] - code - .github/workflows/ci.yml
- [[Dependabot Configuration]] - code - .github/dependabot.yml

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_301
SORT file.name ASC
```
