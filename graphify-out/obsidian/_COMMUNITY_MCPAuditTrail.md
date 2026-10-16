---
type: community
cohesion: 0.09
members: 34
---

# MCPAuditTrail

**Cohesion:** 0.09 - loosely connected
**Members:** 34 nodes

## Members
- [[dot-__len__()]] - code - gateway/proxy/mcp_audit.py
- [[dot-_compute_chain_hash()]] - code - gateway/proxy/mcp_audit.py
- [[dot-entries()]] - code - gateway/proxy/mcp_audit.py
- [[dot-generate_report()]] - code - gateway/proxy/mcp_audit.py
- [[dot-get_blocked_entries()]] - code - gateway/proxy/mcp_audit.py
- [[dot-get_entries_for_agent()]] - code - gateway/proxy/mcp_audit.py
- [[dot-get_entries_for_server()]] - code - gateway/proxy/mcp_audit.py
- [[dot-get_entries_for_tool()]] - code - gateway/proxy/mcp_audit.py
- [[dot-get_failed_entries()]] - code - gateway/proxy/mcp_audit.py
- [[dot-last_hash()]] - code - gateway/proxy/mcp_audit.py
- [[dot-log_tool_call()]] - code - gateway/proxy/mcp_audit.py
- [[dot-log_tool_result()]] - code - gateway/proxy/mcp_audit.py
- [[dot-start_call()]] - code - gateway/proxy/mcp_audit.py
- [[dot-test_default_window_is_10k()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_report_total_reflects_all_appended()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_tamper_in_retained_window_detected()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_verify_chain_valid_after_wrap()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_window_capped_at_max_entries()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-total_appended()]] - code - gateway/proxy/mcp_audit.py
- [[dot-verify_chain()_1]] - code - gateway/proxy/mcp_audit.py
- [[A single MCP tool call audit entry.]] - rationale - gateway/proxy/mcp_audit.py
- [[Any_32]] - code - gateway/proxy/mcp_audit.py
- [[Audit trail for MCP tool calls, integrated with SHA-256 hash chain.]] - rationale - gateway/proxy/mcp_audit.py
- [[Compute hash chain values. Returns (content_hash, chain_hash).]] - rationale - gateway/proxy/mcp_audit.py
- [[Generate an MCP audit report summary.]] - rationale - gateway/proxy/mcp_audit.py
- [[In-memory MCP audit window must be bounded (mirrors AuditChain).]] - rationale - gateway/tests/test_mcp_proxy.py
- [[Log an incoming MCP tool result.]] - rationale - gateway/proxy/mcp_audit.py
- [[Log an outgoing MCP tool call.]] - rationale - gateway/proxy/mcp_audit.py
- [[MCPAuditEntry]] - code - gateway/proxy/mcp_audit.py
- [[MCPAuditTrail]] - code - gateway/proxy/mcp_audit.py
- [[Record the start time of a tool call for duration tracking.]] - rationale - gateway/proxy/mcp_audit.py
- [[TestAuditTrailBounded]] - code - gateway/tests/test_mcp_proxy.py
- [[Verify integrity of the retained MCP audit hash-chain window.          Anchors a]] - rationale - gateway/proxy/mcp_audit.py
- [[audit()]] - code - gateway/tests/test_mcp_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/MCPAuditTrail
SORT file.name ASC
```

## Connections to other communities
- 27 edges to [[_COMMUNITY_MCPPermissionManager]]
- 18 edges to [[_COMMUNITY_StdioConnection]]
- 17 edges to [[_COMMUNITY_MCPPermissionManager_1]]
- 6 edges to [[_COMMUNITY_MCPPermissionManager_3]]
- 3 edges to [[_COMMUNITY_PermissionLevel]]
- 3 edges to [[_COMMUNITY_MCPPermissionManager_4]]
- 3 edges to [[_COMMUNITY_MCPInspector]]
- 1 edge to [[_COMMUNITY_MCPPermissionManager_5]]
- 1 edge to [[_COMMUNITY_MCPPermissionManager_2]]
- 1 edge to [[_COMMUNITY_KillSwitchMonitor]]
- 1 edge to [[_COMMUNITY_TestAuditTrail]]
- 1 edge to [[_COMMUNITY_MCPToolResult]]
- 1 edge to [[_COMMUNITY_AuditChain]]

## Top bridge nodes
- [[MCPAuditTrail]] - degree 90, connects to 12 communities
- [[TestAuditTrailBounded]] - degree 20, connects to 6 communities
- [[MCPAuditEntry]] - degree 11, connects to 1 community
- [[audit()]] - degree 2, connects to 1 community
