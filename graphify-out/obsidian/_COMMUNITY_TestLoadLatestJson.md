---
type: community
cohesion: 0.50
members: 4
---

# TestLoadLatestJson

**Cohesion:** 0.50 - moderately connected
**Members:** 4 nodes

## Members
- [[.test_empty_files_skipped()]] - code - gateway/tests/test_scanner_integration_coverage.py
- [[.test_invalid_then_valid()]] - code - gateway/tests/test_scanner_integration_coverage.py
- [[.test_missing_dir_returns_none()]] - code - gateway/tests/test_scanner_integration_coverage.py
- [[TestLoadLatestJson]] - code - gateway/tests/test_scanner_integration_coverage.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestLoadLatestJson
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY__w()]]
- 1 edge to [[_COMMUNITY_test_scanner_integration_coverage.py]]

## Top bridge nodes
- [[TestLoadLatestJson]] - degree 4, connects to 1 community
- [[.test_empty_files_skipped()]] - degree 2, connects to 1 community
- [[.test_invalid_then_valid()]] - degree 2, connects to 1 community