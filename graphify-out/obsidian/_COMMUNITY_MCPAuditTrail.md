---
type: community
cohesion: 0.09
members: 34
---

# MCPAuditTrail

**Cohesion:** 0.09 - loosely connected
**Members:** 34 nodes

## Members
- [[.__len__()_1]] - code - gateway/proxy/mcp_audit.py
- [[._compute_chain_hash()]] - code - gateway/proxy/mcp_audit.py
- [[.entries()_1]] - code - gateway/proxy/mcp_audit.py
- [[.generate_report()]] - code - gateway/proxy/mcp_audit.py
- [[.get_blocked_entries()]] - code - gateway/proxy/mcp_audit.py
- [[.get_entries_for_agent()]] - code - gateway/proxy/mcp_audit.py
- [[.get_entries_for_server()]] - code - gateway/proxy/mcp_audit.py
- [[.get_entries_for_tool()]] - code - gateway/proxy/mcp_audit.py
- [[.get_failed_entries()]] - code - gateway/proxy/mcp_audit.py
- [[.last_hash()_1]] - code - gateway/proxy/mcp_audit.py
- [[.log_tool_call()]] - code - gateway/proxy/mcp_audit.py
- [[.log_tool_result()]] - code - gateway/proxy/mcp_audit.py
- [[.start_call()]] - code - gateway/proxy/mcp_audit.py
- [[.test_default_window_is_10k()_1]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_report_total_reflects_all_appended()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_tamper_in_retained_window_detected()_1]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_verify_chain_valid_after_wrap()_1]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_window_capped_at_max_entries()_1]] - code - gateway/tests/test_mcp_proxy.py
- [[.total_appended()_1]] - code - gateway/proxy/mcp_audit.py
- [[.verify_chain()_1]] - code - gateway/proxy/mcp_audit.py
- [[A single MCP tool call audit entry.]] - rationale - gateway/proxy/mcp_audit.py
- [[Any_35]] - code - gateway/proxy/mcp_audit.py
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
- [[audit()]] - code - gateway/tests/test_mcp_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/MCPAuditTrail
SORT file.name ASC
```

## Connections to other communities
- 27 edges to [[_COMMUNITY_MCPToolCall]]
- 18 edges to [[_COMMUNITY_StdioConnection]]
- 17 edges to [[_COMMUNITY_MCPServerConfig]]
- 5 edges to [[_COMMUNITY_MCPToolResult]]
- 3 edges to [[_COMMUNITY_FakeProcess]]
- 3 edges to [[_COMMUNITY_PermissionLevel]]
- 3 edges to [[_COMMUNITY_MCPInspector]]
- 2 edges to [[_COMMUNITY_TestInspectorEdgeCases]]
- 1 edge to [[_COMMUNITY_MCPPermissionManager]]
- 1 edge to [[_COMMUNITY_AuditChain]]
- 1 edge to [[_COMMUNITY_KillSwitchMonitor]]
- 1 edge to [[_COMMUNITY_TestAuditTrail]]
- 1 edge to [[_COMMUNITY_TestInjectionDetection]]

## Top bridge nodes
- [[MCPAuditTrail_1]] - degree 90, connects to 12 communities
- [[TestAuditTrailBounded]] - degree 20, connects to 6 communities
- [[MCPAuditEntry]] - degree 11, connects to 1 community
- [[audit()]] - degree 2, connects to 1 community