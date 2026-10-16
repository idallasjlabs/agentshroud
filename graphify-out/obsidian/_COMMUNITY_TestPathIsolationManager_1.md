---
type: community
cohesion: 0.40
members: 5
---

# TestPathIsolationManager

**Cohesion:** 0.40 - moderately connected
**Members:** 5 nodes

## Members
- [[dot-test_installed_not_running()]] - code - gateway/tests/test_scanner_integration_coverage.py
- [[dot-test_not_installed()]] - code - gateway/tests/test_scanner_integration_coverage.py
- [[dot-test_running_no_alert_dir()]] - code - gateway/tests/test_scanner_integration_coverage.py
- [[dot-test_running_with_alert_dir()]] - code - gateway/tests/test_scanner_integration_coverage.py
- [[TestWazuhSummary]] - code - gateway/tests/test_scanner_integration_coverage.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestPathIsolationManager
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY__w]]
- 1 edge to [[_COMMUNITY_ApprovalQueueConfig_7]]

## Top bridge nodes
- [[TestWazuhSummary]] - degree 5, connects to 1 community
- [[dot-test_installed_not_running()]] - degree 2, connects to 1 community
