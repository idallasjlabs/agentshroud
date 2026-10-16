---
type: community
cohesion: 0.07
members: 43
---

# MCPAuditTrail

**Cohesion:** 0.07 - loosely connected
**Members:** 43 nodes

## Members
- [[dot-__len__()_1]] - code - gateway/proxy/mcp_audit.py
- [[dot-_compute_chain_hash()]] - code - gateway/proxy/mcp_audit.py
- [[dot-entries()]] - code - gateway/proxy/mcp_audit.py
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
- [[dot-test_clean_result_passes_through()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_credit_card_detected()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_credit_card_redacted()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_default_window_is_10k()_1]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_email_detected_but_low_threat()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_pii_in_tool_result_redacted()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_report_total_reflects_all_appended()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_ssn_detected_in_params()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_ssn_redacted_in_params()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_tamper_in_retained_window_detected()_1]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_verify_chain_valid_after_wrap()_1]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_window_capped_at_max_entries()_1]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-total_appended()_1]] - code - gateway/proxy/mcp_audit.py
- [[dot-verify_chain()]] - code - gateway/proxy/mcp_audit.py
- [[A single MCP tool call audit entry.]] - rationale - gateway/proxy/mcp_audit.py
- [[Any_18]] - code - gateway/proxy/mcp_audit.py
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
- [[TestPIIDetection_1]] - code - gateway/tests/test_mcp_proxy.py
- [[Verify integrity of the retained MCP audit hash-chain window.          Anchors a]] - rationale - gateway/proxy/mcp_audit.py
- [[audit()]] - code - gateway/tests/test_mcp_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/MCPAuditTrail
SORT file.name ASC
```

## Connections to other communities
- 88 edges to [[_COMMUNITY_MCPPermissionManager]]
- 4 edges to [[_COMMUNITY_StdioConnection]]
- 1 edge to [[_COMMUNITY_AuditChain]]
- 1 edge to [[_COMMUNITY_KillSwitchMonitor]]
- 1 edge to [[_COMMUNITY_TestAuditTrail]]
- 1 edge to [[_COMMUNITY_MCPToolResult]]
- 1 edge to [[_COMMUNITY_ApprovalQueueConfig_1]]

## Top bridge nodes
- [[MCPAuditTrail]] - degree 90, connects to 6 communities
- [[MCPProxy.process_tool_call]] - degree 4, connects to 2 communities
- [[TestPIIDetection_1]] - degree 21, connects to 1 community
- [[TestAuditTrailBounded]] - degree 20, connects to 1 community
- [[MCPAuditEntry]] - degree 11, connects to 1 community
