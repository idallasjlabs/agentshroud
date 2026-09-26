---
type: community
cohesion: 0.40
members: 5
---

# Default Monitor-Mode Egress Rationale

**Cohesion:** 0.40 - moderately connected
**Members:** 5 nodes

## Members
- [[.test_installed_not_running()]] - code - gateway/tests/test_scanner_integration_coverage.py
- [[.test_not_installed()]] - code - gateway/tests/test_scanner_integration_coverage.py
- [[.test_running_no_alert_dir()]] - code - gateway/tests/test_scanner_integration_coverage.py
- [[.test_running_with_alert_dir()]] - code - gateway/tests/test_scanner_integration_coverage.py
- [[TestWazuhSummary]] - code - gateway/tests/test_scanner_integration_coverage.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Default_Monitor-Mode_Egress_Rationale
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_wazuh_client.py]]
- 1 edge to [[_COMMUNITY_TestMultilingualInjection]]

## Top bridge nodes
- [[TestWazuhSummary]] - degree 5, connects to 1 community
- [[.test_installed_not_running()]] - degree 2, connects to 1 community