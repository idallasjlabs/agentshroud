---
type: community
cohesion: 0.09
members: 35
---

# MCPAuditTrail

**Cohesion:** 0.09 - loosely connected
**Members:** 35 nodes

## Members
- [[dot-__len__()_1]] - code - gateway/proxy/mcp_audit.py
- [[dot-_compute_chain_hash()]] - code - gateway/proxy/mcp_audit.py
- [[dot-entries()_1]] - code - gateway/proxy/mcp_audit.py
- [[dot-generate_report()]] - code - gateway/proxy/mcp_audit.py
- [[dot-get_blocked_entries()]] - code - gateway/proxy/mcp_audit.py
- [[dot-get_entries_for_agent()]] - code - gateway/proxy/mcp_audit.py
- [[dot-get_entries_for_server()]] - code - gateway/proxy/mcp_audit.py
- [[dot-get_entries_for_tool()]] - code - gateway/proxy/mcp_audit.py
- [[dot-get_failed_entries()]] - code - gateway/proxy/mcp_audit.py
- [[dot-last_hash()_1]] - code - gateway/proxy/mcp_audit.py
- [[dot-log_tool_call()]] - code - gateway/proxy/mcp_audit.py
- [[dot-log_tool_result()]] - code - gateway/proxy/mcp_audit.py
- [[dot-start_call()]] - code - gateway/proxy/mcp_audit.py
- [[dot-test_default_window_is_10k()_1]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_report_total_reflects_all_appended()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_tamper_in_retained_window_detected()_1]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_verify_chain_valid_after_wrap()_1]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_window_capped_at_max_entries()_1]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-total_appended()_1]] - code - gateway/proxy/mcp_audit.py
- [[dot-verify_chain()_1]] - code - gateway/proxy/mcp_audit.py
- [[A single MCP tool call audit entry.]] - rationale - gateway/proxy/mcp_audit.py
- [[Any_34]] - code - gateway/proxy/mcp_audit.py
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
- [[audit()_1]] - code - gateway/tests/test_mcp_proxy.py
- [[mcp_audit.py]] - code - gateway/proxy/mcp_audit.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/MCPAuditTrail
SORT file.name ASC
```

## Connections to other communities
- 31 edges to [[_COMMUNITY_MCPToolCall]]
- 18 edges to [[_COMMUNITY_StdioConnection]]
- 18 edges to [[_COMMUNITY_MCPPermissionManager]]
- 6 edges to [[_COMMUNITY_MCPToolResult]]
- 3 edges to [[_COMMUNITY_FakeProcess]]
- 2 edges to [[_COMMUNITY_PermissionLevel]]
- 1 edge to [[_COMMUNITY_TestInspectorEdgeCases]]
- 1 edge to [[_COMMUNITY_TestPIIDetection]]
- 1 edge to [[_COMMUNITY_TestExtractEgressTargets]]
- 1 edge to [[_COMMUNITY_AuditChain]]
- 1 edge to [[_COMMUNITY_KillSwitchMonitor]]
- 1 edge to [[_COMMUNITY_TestAuditTrail]]

## Top bridge nodes
- [[MCPAuditTrail]] - degree 90, connects to 11 communities
- [[TestAuditTrailBounded]] - degree 20, connects to 4 communities
- [[mcp_audit.py]] - degree 5, connects to 2 communities
- [[MCPAuditEntry]] - degree 11, connects to 1 community
- [[audit()_1]] - degree 2, connects to 1 community
