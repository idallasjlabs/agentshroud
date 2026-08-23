---
type: community
cohesion: 0.09
members: 35
---

# Mcp Audit (proxy)

**Cohesion:** 0.09 - loosely connected
**Members:** 35 nodes

## Members
- [[.__len__()]] - code - gateway/proxy/mcp_audit.py
- [[._compute_chain_hash()]] - code - gateway/proxy/mcp_audit.py
- [[.entries()]] - code - gateway/proxy/mcp_audit.py
- [[.generate_report()]] - code - gateway/proxy/mcp_audit.py
- [[.get_blocked_entries()]] - code - gateway/proxy/mcp_audit.py
- [[.get_entries_for_agent()]] - code - gateway/proxy/mcp_audit.py
- [[.get_entries_for_server()]] - code - gateway/proxy/mcp_audit.py
- [[.get_entries_for_tool()]] - code - gateway/proxy/mcp_audit.py
- [[.get_failed_entries()]] - code - gateway/proxy/mcp_audit.py
- [[.last_hash()]] - code - gateway/proxy/mcp_audit.py
- [[.log_tool_call()]] - code - gateway/proxy/mcp_audit.py
- [[.log_tool_result()]] - code - gateway/proxy/mcp_audit.py
- [[.start_call()]] - code - gateway/proxy/mcp_audit.py
- [[.test_default_window_is_10k()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_report_total_reflects_all_appended()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_tamper_in_retained_window_detected()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_verify_chain_valid_after_wrap()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_window_capped_at_max_entries()]] - code - gateway/tests/test_mcp_proxy.py
- [[.total_appended()]] - code - gateway/proxy/mcp_audit.py
- [[.verify_chain()]] - code - gateway/proxy/mcp_audit.py
- [[A single MCP tool call audit entry.]] - rationale - gateway/proxy/mcp_audit.py
- [[Any_15]] - code - gateway/proxy/mcp_audit.py
- [[Audit trail for MCP tool calls, integrated with SHA-256 hash chain.]] - rationale - gateway/proxy/mcp_audit.py
- [[Compute hash chain values. Returns (content_hash, chain_hash).]] - rationale - gateway/proxy/mcp_audit.py
- [[Generate an MCP audit report summary.]] - rationale - gateway/proxy/mcp_audit.py
- [[In-memory MCP audit window must be bounded (mirrors AuditChain).]] - rationale - gateway/tests/test_mcp_proxy.py
- [[Log an incoming MCP tool result.]] - rationale - gateway/proxy/mcp_audit.py
- [[Log an outgoing MCP tool call.]] - rationale - gateway/proxy/mcp_audit.py
- [[MCPAuditEntry]] - code - gateway/proxy/mcp_audit.py
- [[MCPAuditTrail]] - code - gateway/proxy/mcp_audit.py
- [[MCPProxy.process_tool_call]] - code - gateway/proxy/mcp_proxy.py
- [[Record the start time of a tool call for duration tracking.]] - rationale - gateway/proxy/mcp_audit.py
- [[TestAuditTrailBounded]] - code - gateway/tests/test_mcp_proxy.py
- [[Verify integrity of the retained MCP audit hash-chain window.          Anchors a]] - rationale - gateway/proxy/mcp_audit.py
- [[audit()]] - code - gateway/tests/test_mcp_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Mcp_Audit_proxy
SORT file.name ASC
```

## Connections to other communities
- 33 edges to [[_COMMUNITY_Mcp Proxy]]
- 14 edges to [[_COMMUNITY_Mcp Proxy Coverage]]
- 10 edges to [[_COMMUNITY_Mcp Permissions]]
- 7 edges to [[_COMMUNITY_Mcp Proxy Coverage]]
- 6 edges to [[_COMMUNITY_Mcp Proxy]]
- 5 edges to [[_COMMUNITY_Mcp Inspector (proxy)]]
- 5 edges to [[_COMMUNITY_Mcp Permissions (proxy)]]
- 1 edge to [[_COMMUNITY_Mcp Proxy Wrapper (scripts)]]
- 1 edge to [[_COMMUNITY_Enhanced Approval]]
- 1 edge to [[_COMMUNITY_Mcp Proxy (proxy)]]
- 1 edge to [[_COMMUNITY_Killswitch Monitor & Observatory Mode]]
- 1 edge to [[_COMMUNITY_Pipeline Unit]]
- 1 edge to [[_COMMUNITY_Mcp Proxy]]

## Top bridge nodes
- [[MCPAuditTrail]] - degree 91, connects to 12 communities
- [[TestAuditTrailBounded]] - degree 20, connects to 4 communities
- [[MCPProxy.process_tool_call]] - degree 4, connects to 3 communities
- [[MCPAuditEntry]] - degree 11, connects to 1 community
- [[audit()]] - degree 2, connects to 1 community