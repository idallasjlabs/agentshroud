---
type: community
members: 5
---

# Outbound Infrastructure Content Filter (deny-list for hostnames, tool names, user IDs)

**Members:** 5 nodes

## Members
- [[dot-test_installed_not_running_is_clean_note()]] - code - gateway/tests/test_scanner_integration_coverage.py
- [[dot-test_not_installed_not_running()]] - code - gateway/tests/test_scanner_integration_coverage.py
- [[dot-test_running_with_alerts_sets_timestamp()]] - code - gateway/tests/test_scanner_integration_coverage.py
- [[dot-test_running_without_alert_dir()]] - code - gateway/tests/test_scanner_integration_coverage.py
- [[TestFalcoSummary]] - code - gateway/tests/test_scanner_integration_coverage.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Outbound_Infrastructure_Content_Filter_deny-list_for_hostnames_tool_names_user_IDs
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_UserSessionManager (3) (2)]]
- 1 edge to [[_COMMUNITY_MiddlewareManager (3) (2)]]

## Top bridge nodes
- [[TestFalcoSummary]] - degree 5, connects to 1 community
- [[dot-test_installed_not_running_is_clean_note()]] - degree 2, connects to 1 community
