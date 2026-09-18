---
type: community
cohesion: 0.40
members: 5
---

# TestOpenscapSummary

**Cohesion:** 0.40 - moderately connected
**Members:** 5 nodes

## Members
- [[.test_compact_timestamp_normalised_to_iso()]] - code - gateway/tests/test_scanner_integration_coverage.py
- [[.test_critical_and_warning_statuses()]] - code - gateway/tests/test_scanner_integration_coverage.py
- [[.test_garbage_timestamp_falls_back_to_mtime()]] - code - gateway/tests/test_scanner_integration_coverage.py
- [[.test_not_run()]] - code - gateway/tests/test_scanner_integration_coverage.py
- [[TestOpenscapSummary]] - code - gateway/tests/test_scanner_integration_coverage.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestOpenscapSummary
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY__w()]]
- 1 edge to [[_COMMUNITY_test_scanner_integration_coverage.py]]

## Top bridge nodes
- [[TestOpenscapSummary]] - degree 5, connects to 1 community
- [[.test_compact_timestamp_normalised_to_iso()]] - degree 2, connects to 1 community
- [[.test_critical_and_warning_statuses()]] - degree 2, connects to 1 community
- [[.test_garbage_timestamp_falls_back_to_mtime()]] - degree 2, connects to 1 community