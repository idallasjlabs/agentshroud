---
type: community
cohesion: 0.20
members: 10
---

# Egress Filter Errors

**Cohesion:** 0.20 - loosely connected
**Members:** 10 nodes

## Members
- [[dot-test_blocked_entry_logged()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_chain_entries_linked()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_hash_chain_changes_on_append()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_hash_chain_genesis()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_hash_chain_valid()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_log_tool_call()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_log_tool_result()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_pii_redacted_flag()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_tampered_chain_detected()]] - code - gateway/tests/test_mcp_proxy.py
- [[TestAuditTrail_2]] - code - gateway/tests/test_mcp_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Egress_Filter_Errors
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
- [[TestAuditTrail_2]] - degree 23, connects to 6 communities
