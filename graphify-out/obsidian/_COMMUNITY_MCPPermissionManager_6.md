---
type: community
cohesion: 0.25
members: 8
---

# MCPPermissionManager

**Cohesion:** 0.25 - loosely connected
**Members:** 8 nodes

## Members
- [[dot-test_clean_result_passes_through()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_credit_card_detected()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_credit_card_redacted()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_email_detected_but_low_threat()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_pii_in_tool_result_redacted()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_ssn_detected_in_params()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_ssn_redacted_in_params()]] - code - gateway/tests/test_mcp_proxy.py
- [[TestPIIDetection_1]] - code - gateway/tests/test_mcp_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/MCPPermissionManager
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_MCPPermissionManager]]
- 2 edges to [[_COMMUNITY_MCPPermissionManager_1]]
- 2 edges to [[_COMMUNITY_PermissionLevel]]
- 2 edges to [[_COMMUNITY_MCPInspector]]
- 1 edge to [[_COMMUNITY_MCPAuditTrail]]
- 1 edge to [[_COMMUNITY_MCPPermissionManager_2]]
- 1 edge to [[_COMMUNITY_MCPPermissionManager_4]]

## Top bridge nodes
- [[TestPIIDetection_1]] - degree 21, connects to 7 communities
