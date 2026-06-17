---
type: community
cohesion: 0.25
members: 8
---

# Module Group 442

**Cohesion:** 0.25 - loosely connected
**Members:** 8 nodes

## Members
- [[.test_clean_result_passes_through()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_credit_card_detected()_1]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_credit_card_redacted()_1]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_email_detected_but_low_threat()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_pii_in_tool_result_redacted()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_ssn_detected_in_params()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_ssn_redacted_in_params()]] - code - gateway/tests/test_mcp_proxy.py
- [[TestPIIDetection]] - code - gateway/tests/test_mcp_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_442
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_MCP Config & Proxy]]
- 3 edges to [[_COMMUNITY_Module Group 78]]
- 2 edges to [[_COMMUNITY_MCP Inspector & Audit]]
- 1 edge to [[_COMMUNITY_Module Group 139]]
- 1 edge to [[_COMMUNITY_Module Group 154]]
- 1 edge to [[_COMMUNITY_MCP Permissions Manager]]
- 1 edge to [[_COMMUNITY_Module Group 266]]

## Top bridge nodes
- [[TestPIIDetection]] - degree 21, connects to 7 communities