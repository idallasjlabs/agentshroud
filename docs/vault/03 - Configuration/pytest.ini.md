---
title: pytest.ini
type: config
file_path: pytest.ini
tags: [testing, pytest, configuration]
related: [Configuration/ci-workflows, Dependencies/All Dependencies]
status: documented
---

# pytest.ini

**Location:** `pytest.ini` (repo root)
**Lines:** 3

## Purpose

Pytest configuration file for the AgentShroud test suite. Currently minimal — sets only the cache directory.

## Contents

```ini
[pytest]
cache_dir = /tmp/pytest_cache
```

## Why `/tmp/pytest_cache`

The cache directory is set to `/tmp/pytest_cache` rather than the default `.pytest_cache/` in the repo root. This prevents:
- Cache files from appearing in `git status`
- Cache from being copied into Docker build context
- CI runner disk space issues from accumulating cache

## Test Execution

The standard test command per `CLAUDE.md`:
```bash
pytest -q --asyncio-mode=auto
```

The `--asyncio-mode=auto` flag is passed at runtime (not in `pytest.ini`), enabling automatic async test detection without `@pytest.mark.asyncio` on every test.

## Coverage Requirements

Per `CLAUDE.md`:
- **≥80% test coverage** on new or modified code
- Coverage typically measured with:
  ```bash
  pytest --cov=gateway --cov-report=term-missing
  ```

## Test Locations

Tests are located in `gateway/tests/` and follow pytest discovery conventions:
- Files: `test_*.py` or `*_test.py`
- Functions: `test_*`
- Classes: `Test*`

## Related Notes

- [[Configuration/ci-workflows]] — How tests run in GitHub Actions
- [[Dependencies/All Dependencies]] — pytest, pytest-asyncio, pytest-cov dependencies
