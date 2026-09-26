---
type: community
cohesion: 0.50
members: 4
---

# MCP Tools Usage (MCPM)

**Cohesion:** 0.50 - moderately connected
**Members:** 4 nodes

## Members
- [[.test_not_running()]] - code - gateway/tests/test_scanner_integration_coverage.py
- [[.test_running_with_fresh_log()]] - code - gateway/tests/test_scanner_integration_coverage.py
- [[.test_running_without_logs()]] - code - gateway/tests/test_scanner_integration_coverage.py
- [[TestFluentBitSummary]] - code - gateway/tests/test_scanner_integration_coverage.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/MCP_Tools_Usage_MCPM
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_wazuh_client.py]]
- 1 edge to [[_COMMUNITY_TestMultilingualInjection]]

## Top bridge nodes
- [[TestFluentBitSummary]] - degree 4, connects to 1 community
- [[.test_running_with_fresh_log()]] - degree 2, connects to 1 community