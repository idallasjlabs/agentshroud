---
type: community
cohesion: 0.09
members: 30
---

# AgentShroud v0.9.0 — Human Interface Testing Gui

**Cohesion:** 0.09 - loosely connected
**Members:** 30 nodes

## Members
- [[.__post_init__()_1]] - code - gateway/proxy/mcp_proxy.py
- [[._emit_privacy_event()]] - code - gateway/proxy/mcp_proxy.py
- [[._execute_tool_call()]] - code - gateway/proxy/mcp_proxy.py
- [[._extract_egress_targets()]] - code - gateway/proxy/mcp_proxy.py
- [[._sanitize_admin_private_data()]] - code - gateway/proxy/mcp_proxy.py
- [[.check_approval_required()]] - code - gateway/proxy/mcp_proxy.py
- [[.process_tool_call()]] - code - gateway/proxy/mcp_proxy.py
- [[.process_tool_result()_1]] - code - gateway/proxy/mcp_proxy.py
- [[.send_request()_1]] - code - gateway/proxy/mcp_proxy.py
- [[.test_admin_private_data_not_redacted_for_owner()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_admin_private_data_redacted_for_non_owner()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_clean_result_passes()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_error_result_logged()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_gateway_contributor_paths_redacted_for_non_owner()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_memory_markers_redacted_for_non_owner()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_pii_redacted_in_result()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_private_redaction_emits_privacy_event()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_result_audit_logged()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_result_processing_time()]] - code - gateway/tests/test_mcp_proxy.py
- [[Actually execute the tool call against the MCP server.]] - rationale - gateway/proxy/mcp_proxy.py
- [[Best-effort privacy event emission.]] - rationale - gateway/proxy/mcp_proxy.py
- [[Check if a tool call requires approval and wait for it if needed.]] - rationale - gateway/proxy/mcp_proxy.py
- [[Extract outbound URL-like targets from nested MCP tool parameters.]] - rationale - gateway/proxy/mcp_proxy.py
- [[MCPToolResult]] - code - gateway/proxy/mcp_proxy.py
- [[Process a tool result coming back (for cases where execution happens externally)]] - rationale - gateway/proxy/mcp_proxy.py
- [[Process an MCP tool call through the security pipeline.          Args]] - rationale - gateway/proxy/mcp_proxy.py
- [[Redact admin-private data from tool results for non-owner agents.]] - rationale - gateway/proxy/mcp_proxy.py
- [[Represents an MCP tool result.]] - rationale - gateway/proxy/mcp_proxy.py
- [[Send an HTTP request to the MCP server.]] - rationale - gateway/proxy/mcp_proxy.py
- [[TestProxyResultProcessing]] - code - gateway/tests/test_mcp_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/AgentShroud_v090__Human_Interface_Testing_Gui
SORT file.name ASC
```

## Connections to other communities
- 35 edges to [[_COMMUNITY_test_llm_proxy_local_parity.py]]
- 26 edges to [[_COMMUNITY_test_voice_gateway.py]]
- 7 edges to [[_COMMUNITY_GitGuard]]
- 7 edges to [[_COMMUNITY_TestParanoidConfig]]
- 5 edges to [[_COMMUNITY_test_e2e_proxy.py]]
- 3 edges to [[_COMMUNITY_brand-guidelines]]
- 2 edges to [[_COMMUNITY_SSHProxy]]
- 2 edges to [[_COMMUNITY_asyncio]]
- 2 edges to [[_COMMUNITY_Safe Refactor Specialist]]
- 1 edge to [[_COMMUNITY_TestCollaboratorPromptClassifiers]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy]]
- 1 edge to [[_COMMUNITY_Operating Rules (Non-Negotiable)]]
- 1 edge to [[_COMMUNITY_NetworkSecurityFinding]]
- 1 edge to [[_COMMUNITY_v0.9.0 Sentinel — Data Isolation + SOC + Remed]]
- 1 edge to [[_COMMUNITY_→ {site site1, test_mode True, output_p]]
- 1 edge to [[_COMMUNITY_Vulcan — Subject Matter Auditor]]

## Top bridge nodes
- [[MCPToolResult]] - degree 79, connects to 14 communities
- [[TestProxyResultProcessing]] - degree 23, connects to 6 communities
- [[._execute_tool_call()]] - degree 8, connects to 3 communities
- [[.process_tool_call()]] - degree 9, connects to 2 communities
- [[.process_tool_result()_1]] - degree 6, connects to 2 communities