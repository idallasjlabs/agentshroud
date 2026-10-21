---
type: community
members: 34
---

# MCPAuditTrail

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
- [[dot-verify_chain()]] - code - gateway/proxy/mcp_audit.py
- [[A single MCP tool call audit entry.]] - rationale - gateway/proxy/mcp_audit.py
- [[Any_36]] - code - gateway/proxy/mcp_audit.py
- [[Audit trail for MCP tool calls, integrated with SHA-256 hash chain.]] - rationale - gateway/proxy/mcp_audit.py
- [[Compute hash chain values. Returns (content_hash, chain_hash).]] - rationale - gateway/proxy/mcp_audit.py
- [[Generate an MCP audit report summary.]] - rationale - gateway/proxy/mcp_audit.py
- [[In-memory MCP audit window must be bounded (mirrors AuditChain).]] - rationale - gateway/tests/test_mcp_proxy.py
- [[Log an incoming MCP tool result.]] - rationale - gateway/proxy/mcp_audit.py
- [[Log an outgoing MCP tool call.]] - rationale - gateway/proxy/mcp_audit.py
- [[MCPAuditEntry]] - code - gateway/proxy/mcp_audit.py
- [[MCPAuditTrail_1]] - code - gateway/proxy/mcp_audit.py
- [[Record the start time of a tool call for duration tracking.]] - rationale - gateway/proxy/mcp_audit.py
- [[TestAuditTrailBounded]] - code - gateway/tests/test_mcp_proxy.py
- [[Verify integrity of the retained MCP audit hash-chain window.          Anchors a]] - rationale - gateway/proxy/mcp_audit.py
- [[mcp_audit.py]] - code - gateway/proxy/mcp_audit.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/MCPAuditTrail
SORT file.name ASC
```

## Connections to other communities
- 27 edges to [[_COMMUNITY_MCPPermissionManager]]
- 12 edges to [[_COMMUNITY_StdioConnection]]
- 10 edges to [[_COMMUNITY_StdioConnection (2)]]
- 9 edges to [[_COMMUNITY_MCPInspector]]
- 8 edges to [[_COMMUNITY_MCPPermissionManager (3)]]
- 6 edges to [[_COMMUNITY_MCPPermissionManager (4)]]
- 2 edges to [[_COMMUNITY_PermissionLevel]]
- 1 edge to [[_COMMUNITY_MCPToolResult]]
- 1 edge to [[_COMMUNITY_MCPPermissionManager (5)]]
- 1 edge to [[_COMMUNITY_MCPPermissionManager (6)]]
- 1 edge to [[_COMMUNITY_Athena — Knowledge Distiller (4)]]
- 1 edge to [[_COMMUNITY_MCPPermissionManager (7)]]
- 1 edge to [[_COMMUNITY_KillSwitchMonitor (3)]]
- 1 edge to [[_COMMUNITY_MCPPermissionManager (2)]]
- 1 edge to [[_COMMUNITY_TestMCPProxyEndpoint]]
- 1 edge to [[_COMMUNITY_TestAuditTrail]]
- 1 edge to [[_COMMUNITY_SecurityPipeline]]

## Top bridge nodes
- [[MCPAuditTrail_1]] - degree 90, connects to 15 communities
- [[TestAuditTrailBounded]] - degree 20, connects to 6 communities
- [[mcp_audit.py]] - degree 5, connects to 2 communities
- [[MCPAuditEntry]] - degree 11, connects to 1 community
