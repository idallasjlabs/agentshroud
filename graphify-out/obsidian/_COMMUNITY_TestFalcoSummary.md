---
type: community
cohesion: 0.40
members: 5
---

# TestFalcoSummary

**Cohesion:** 0.40 - moderately connected
**Members:** 5 nodes

## Members
- [[.test_installed_not_running_is_clean_note()]] - code - gateway/tests/test_scanner_integration_coverage.py
- [[.test_not_installed_not_running()]] - code - gateway/tests/test_scanner_integration_coverage.py
- [[.test_running_with_alerts_sets_timestamp()]] - code - gateway/tests/test_scanner_integration_coverage.py
- [[.test_running_without_alert_dir()]] - code - gateway/tests/test_scanner_integration_coverage.py
- [[TestFalcoSummary_1]] - code - gateway/tests/test_scanner_integration_coverage.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestFalcoSummary
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_test_scanner_integration_coverage.py]]
- 1 edge to [[_COMMUNITY__w()]]

## Top bridge nodes
- [[TestFalcoSummary_1]] - degree 5, connects to 1 community
- [[.test_installed_not_running_is_clean_note()]] - degree 2, connects to 1 community