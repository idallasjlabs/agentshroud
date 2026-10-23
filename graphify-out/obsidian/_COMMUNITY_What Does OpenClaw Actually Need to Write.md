---
type: community
cohesion: 0.08
members: 40
---

# What Does OpenClaw Actually Need to Write?

**Cohesion:** 0.08 - loosely connected
**Members:** 40 nodes

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
- [[A single finding from inspection.]] - rationale - gateway/proxy/mcp_inspector.py
- [[Any_25]] - code - gateway/proxy/mcp_audit.py
- [[Audit trail for MCP tool calls, integrated with SHA-256 hash chain.]] - rationale - gateway/proxy/mcp_audit.py
- [[Compute hash chain values. Returns (content_hash, chain_hash).]] - rationale - gateway/proxy/mcp_audit.py
- [[Generate an MCP audit report summary.]] - rationale - gateway/proxy/mcp_audit.py
- [[In-memory MCP audit window must be bounded (mirrors AuditChain).]] - rationale - gateway/tests/test_mcp_proxy.py
- [[InspectionFinding]] - code - gateway/proxy/mcp_inspector.py
- [[Log an incoming MCP tool result.]] - rationale - gateway/proxy/mcp_audit.py
- [[Log an outgoing MCP tool call.]] - rationale - gateway/proxy/mcp_audit.py
- [[MCPAuditEntry]] - code - gateway/proxy/mcp_audit.py
- [[MCPAuditTrail]] - code - gateway/proxy/mcp_audit.py
- [[Record the start time of a tool call for duration tracking.]] - rationale - gateway/proxy/mcp_audit.py
- [[TestAuditTrailBounded]] - code - gateway/tests/test_mcp_proxy.py
- [[Verify integrity of the retained MCP audit hash-chain window.          Anchors a]] - rationale - gateway/proxy/mcp_audit.py
- [[audit()]] - code - gateway/tests/test_mcp_proxy.py
- [[mcp_audit.py]] - code - gateway/proxy/mcp_audit.py
- [[mcp_inspector.py]] - code - gateway/proxy/mcp_inspector.py
- [[mcp_proxy.py]] - code - gateway/proxy/mcp_proxy.py
- [[proxy__init__.py]] - code - gateway/proxy/__init__.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/What_Does_OpenClaw_Actually_Need_to_Write
SORT file.name ASC
```

## Connections to other communities
- 39 edges to [[_COMMUNITY_MCPToolCall]]
- 20 edges to [[_COMMUNITY_MCPInspector]]
- 18 edges to [[_COMMUNITY_CrossBotTrustLedger]]
- 13 edges to [[_COMMUNITY_test_bots_ssh_exec_wrapper.py]]
- 10 edges to [[_COMMUNITY_StdioConnection]]
- 8 edges to [[_COMMUNITY_MCPToolResult]]
- 4 edges to [[_COMMUNITY_MCPPermissionManager (2)_1]]
- 3 edges to [[_COMMUNITY_AgentShroud Security Value Proposition]]
- 2 edges to [[_COMMUNITY_ContextSegment]]
- 2 edges to [[_COMMUNITY_MCPPermissionManager]]
- 1 edge to [[_COMMUNITY_TestInspectorEdgeCases]]
- 1 edge to [[_COMMUNITY_TestPIIDetection]]
- 1 edge to [[_COMMUNITY_KillSwitchMonitor]]
- 1 edge to [[_COMMUNITY_Egress Filter Errors]]
- 1 edge to [[_COMMUNITY_AuditChain]]
- 1 edge to [[_COMMUNITY_Enum]]
- 1 edge to [[_COMMUNITY_TestOutboundInfoFilter (2)]]

## Top bridge nodes
- [[MCPAuditTrail]] - degree 90, connects to 12 communities
- [[mcp_proxy.py]] - degree 25, connects to 11 communities
- [[proxy__init__.py]] - degree 23, connects to 6 communities
- [[TestAuditTrailBounded]] - degree 20, connects to 5 communities
- [[mcp_inspector.py]] - degree 9, connects to 3 communities
