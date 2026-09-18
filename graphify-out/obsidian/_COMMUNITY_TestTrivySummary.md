---
type: community
cohesion: 0.50
members: 4
---

# TestTrivySummary

**Cohesion:** 0.50 - moderately connected
**Members:** 4 nodes

## Members
- [[.test_clean_when_installed_without_report()]] - code - gateway/tests/test_scanner_integration_coverage.py
- [[.test_not_run_without_binary_or_report()]] - code - gateway/tests/test_scanner_integration_coverage.py
- [[.test_timestamp_falls_back_to_file_mtime()]] - code - gateway/tests/test_scanner_integration_coverage.py
- [[TestTrivySummary_1]] - code - gateway/tests/test_scanner_integration_coverage.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestTrivySummary
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_test_scanner_integration_coverage.py]]
- 1 edge to [[_COMMUNITY__w()]]

## Top bridge nodes
- [[TestTrivySummary_1]] - degree 4, connects to 1 community
- [[.test_timestamp_falls_back_to_file_mtime()]] - degree 2, connects to 1 community