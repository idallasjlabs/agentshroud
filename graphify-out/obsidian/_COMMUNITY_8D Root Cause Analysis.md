---
type: community
cohesion: 0.40
members: 5
---

# 8D Root Cause Analysis

**Cohesion:** 0.40 - moderately connected
**Members:** 5 nodes

## Members
- [[.test_installed_not_running_is_clean_note()]] - code - gateway/tests/test_scanner_integration_coverage.py
- [[.test_not_installed_not_running()]] - code - gateway/tests/test_scanner_integration_coverage.py
- [[.test_running_with_alerts_sets_timestamp()]] - code - gateway/tests/test_scanner_integration_coverage.py
- [[.test_running_without_alert_dir()]] - code - gateway/tests/test_scanner_integration_coverage.py
- [[TestFalcoSummary]] - code - gateway/tests/test_scanner_integration_coverage.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/8D_Root_Cause_Analysis
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_wazuh_client.py]]
- 1 edge to [[_COMMUNITY_TestMultilingualInjection]]

## Top bridge nodes
- [[TestFalcoSummary]] - degree 5, connects to 1 community
- [[.test_installed_not_running_is_clean_note()]] - degree 2, connects to 1 community