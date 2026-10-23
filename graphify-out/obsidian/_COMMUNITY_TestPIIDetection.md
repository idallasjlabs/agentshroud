---
type: community
cohesion: 0.25
members: 8
---

# TestPIIDetection

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
TABLE source_file, type FROM #community/TestPIIDetection
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_MCPToolCall]]
- 4 edges to [[_COMMUNITY_CrossBotTrustLedger]]
- 2 edges to [[_COMMUNITY_MCPInspector]]
- 1 edge to [[_COMMUNITY_What Does OpenClaw Actually Need to Write]]
- 1 edge to [[_COMMUNITY_MCPPermissionManager (2)_1]]
- 1 edge to [[_COMMUNITY_MCPToolResult]]

## Top bridge nodes
- [[TestPIIDetection_1]] - degree 21, connects to 6 communities
