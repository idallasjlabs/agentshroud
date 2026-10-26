---
type: community
members: 33
---

# Community 184

**Members:** 33 nodes

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
- [[Record the start time of a tool call for duration tracking.]] - rationale - gateway/proxy/mcp_audit.py
- [[TestAuditTrailBounded]] - code - gateway/tests/test_mcp_proxy.py
- [[Verify integrity of the retained MCP audit hash-chain window.          Anchors a]] - rationale - gateway/proxy/mcp_audit.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_184
SORT file.name ASC
```

## Connections to other communities
- 26 edges to [[_COMMUNITY_Community 64]]
- 22 edges to [[_COMMUNITY_Community 132]]
- 10 edges to [[_COMMUNITY_Community 230]]
- 9 edges to [[_COMMUNITY_Community 54]]
- 6 edges to [[_COMMUNITY_Community 329]]
- 2 edges to [[_COMMUNITY_Community 941]]
- 1 edge to [[_COMMUNITY_Community 9]]
- 1 edge to [[_COMMUNITY_Community 232]]
- 1 edge to [[_COMMUNITY_Community 24]]
- 1 edge to [[_COMMUNITY_Community 140]]
- 1 edge to [[_COMMUNITY_Community 1970]]
- 1 edge to [[_COMMUNITY_Community 2042]]
- 1 edge to [[_COMMUNITY_Community 2071]]
- 1 edge to [[_COMMUNITY_Community 59]]

## Top bridge nodes
- [[MCPAuditTrail]] - degree 90, connects to 13 communities
- [[TestAuditTrailBounded]] - degree 20, connects to 6 communities
- [[MCPAuditEntry]] - degree 11, connects to 1 community