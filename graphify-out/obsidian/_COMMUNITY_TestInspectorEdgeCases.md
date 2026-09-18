---
type: community
cohesion: 0.12
members: 16
---

# TestInspectorEdgeCases

**Cohesion:** 0.12 - loosely connected
**Members:** 16 nodes

## Members
- [[.test_clean_result_passes_through()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_credit_card_detected()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_credit_card_redacted()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_deeply_nested_pii()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_email_detected_but_low_threat()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_empty_params()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_list_params()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_no_pii_scan()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_none_values_in_params()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_pii_in_tool_result_redacted()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_ssn_detected_in_params()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_ssn_redacted_in_params()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_tool_result_none_content()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_tool_result_string_content()]] - code - gateway/tests/test_mcp_proxy.py
- [[TestInspectorEdgeCases]] - code - gateway/tests/test_mcp_proxy.py
- [[TestPIIDetection]] - code - gateway/tests/test_mcp_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestInspectorEdgeCases
SORT file.name ASC
```

## Connections to other communities
- 10 edges to [[_COMMUNITY_MCPToolCall]]
- 6 edges to [[_COMMUNITY_MCPServerConfig]]
- 4 edges to [[_COMMUNITY_PermissionLevel]]
- 2 edges to [[_COMMUNITY_MCPAuditTrail]]
- 2 edges to [[_COMMUNITY_MCPInspector]]
- 2 edges to [[_COMMUNITY_MCPPermissionManager]]
- 2 edges to [[_COMMUNITY_MCPToolResult]]

## Top bridge nodes
- [[TestInspectorEdgeCases]] - degree 21, connects to 7 communities
- [[TestPIIDetection]] - degree 21, connects to 7 communities