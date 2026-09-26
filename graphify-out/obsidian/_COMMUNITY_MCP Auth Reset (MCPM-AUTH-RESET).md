---
type: community
cohesion: 0.40
members: 5
---

# MCP Auth Reset (MCPM-AUTH-RESET)

**Cohesion:** 0.40 - moderately connected
**Members:** 5 nodes

## Members
- [[.test_invalid_json()]] - code - gateway/tests/test_scanner_integration_coverage.py
- [[.test_missing_dir()]] - code - gateway/tests/test_scanner_integration_coverage.py
- [[.test_no_files()]] - code - gateway/tests/test_scanner_integration_coverage.py
- [[.test_valid()]] - code - gateway/tests/test_scanner_integration_coverage.py
- [[TestGetSbom_1]] - code - gateway/tests/test_scanner_integration_coverage.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/MCP_Auth_Reset_MCPM-AUTH-RESET
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_TestMultilingualInjection]]
- 1 edge to [[_COMMUNITY_wazuh_client.py]]

## Top bridge nodes
- [[TestGetSbom_1]] - degree 5, connects to 1 community
- [[.test_invalid_json()]] - degree 2, connects to 1 community
- [[.test_valid()]] - degree 2, connects to 1 community