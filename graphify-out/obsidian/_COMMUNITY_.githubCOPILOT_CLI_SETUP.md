---
type: community
members: 3
---

# .github/COPILOT_CLI_SETUP.md

**Members:** 3 nodes

## Members
- [[.test_invalid_json_returns_empty()]] - code - gateway/tests/test_scanner_integration_coverage.py
- [[.test_reads_daemon_json()]] - code - gateway/tests/test_scanner_integration_coverage.py
- [[TestDaemonConfigReader]] - code - gateway/tests/test_scanner_integration_coverage.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/github/COPILOT_CLI_SETUPmd
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_Gateway Test Suite]]
- 1 edge to [[_COMMUNITY_docsproject]]

## Top bridge nodes
- [[TestDaemonConfigReader]] - degree 3, connects to 1 community
- [[.test_reads_daemon_json()]] - degree 2, connects to 1 community
- [[.test_invalid_json_returns_empty()]] - degree 2, connects to 1 community