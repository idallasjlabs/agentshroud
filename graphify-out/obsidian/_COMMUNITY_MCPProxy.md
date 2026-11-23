---
type: community
members: 50
---

# MCPProxy

**Members:** 50 nodes

## Members
- [[dot-__init__()_227]] - code - gateway/proxy/mcp_proxy.py
- [[dot-_emit_privacy_event()]] - code - gateway/proxy/mcp_proxy.py
- [[dot-_execute_tool_call()]] - code - gateway/proxy/mcp_proxy.py
- [[dot-_extract_egress_targets()]] - code - gateway/proxy/mcp_proxy.py
- [[dot-_sanitize_admin_private_data()]] - code - gateway/proxy/mcp_proxy.py
- [[dot-check_approval_required()]] - code - gateway/proxy/mcp_proxy.py
- [[dot-get_stats()_19]] - code - gateway/proxy/mcp_proxy.py
- [[dot-mcp_proxy_with_approval()]] - code - gateway/tests/test_enhanced_approval.py
- [[dot-process_tool_call()]] - code - gateway/proxy/mcp_proxy.py
- [[dot-process_tool_result()_1]] - code - gateway/proxy/mcp_proxy.py
- [[dot-send_request()_2]] - code - gateway/proxy/mcp_proxy.py
- [[dot-set_event_bus()_2]] - code - gateway/proxy/mcp_proxy.py
- [[dot-shutdown()]] - code - gateway/proxy/mcp_proxy.py
- [[dot-test_bare_host_in_destination_field()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[dot-test_bare_host_in_non_destination_field_ignored()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[dot-test_critical_tool_requires_approval()]] - code - gateway/tests/test_enhanced_approval.py
- [[dot-test_direct_urls_dedup_and_lists()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[dot-test_disabled_server_blocked()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_invalid_url_without_netloc_ignored()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[dot-test_list_inherits_parent_key()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[dot-test_low_risk_tool_allowed()]] - code - gateway/tests/test_enhanced_approval.py
- [[dot-test_non_matching_text_in_destination_field()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[dot-test_owner_bypass()_3]] - code - gateway/tests/test_enhanced_approval.py
- [[Actually execute the tool call against the MCP server.]] - rationale - gateway/proxy/mcp_proxy.py
- [[Any_91]] - code
- [[Best-effort privacy event emission.]] - rationale - gateway/proxy/mcp_proxy.py
- [[Check if a tool call requires approval and wait for it if needed.]] - rationale - gateway/proxy/mcp_proxy.py
- [[Clean shutdown — close all connections.]] - rationale - gateway/proxy/mcp_proxy.py
- [[Create an MCP proxy with approval queue.]] - rationale - gateway/tests/test_enhanced_approval.py
- [[Extract outbound URL-like targets from nested MCP tool parameters.]] - rationale - gateway/proxy/mcp_proxy.py
- [[Get proxy statistics._1]] - rationale - gateway/proxy/mcp_proxy.py
- [[MCPProxy]] - code - gateway/proxy/mcp_proxy.py
- [[MCPProxyConfig]] - code - gateway/proxy/mcp_config.py
- [[Main MCP proxy that intercepts tool calls and routes through security.…]] - rationale - gateway/proxy/mcp_proxy.py
- [[Process a tool result coming back (for cases where execution happens…]] - rationale - gateway/proxy/mcp_proxy.py
- [[Process an MCP tool call through the security pipeline. Args tool_call The…]] - rationale - gateway/proxy/mcp_proxy.py
- [[Redact admin-private data from tool results for non-owner agents.]] - rationale - gateway/proxy/mcp_proxy.py
- [[Send an HTTP request to the MCP server.]] - rationale - gateway/proxy/mcp_proxy.py
- [[Test MCP proxy integration with approval queue.]] - rationale - gateway/tests/test_enhanced_approval.py
- [[Test owner bypass for high-tier tools.]] - rationale - gateway/tests/test_enhanced_approval.py
- [[Test that critical tools are identified as requiring approval.]] - rationale - gateway/tests/test_enhanced_approval.py
- [[Test that low-risk tools are allowed without approval.]] - rationale - gateway/tests/test_enhanced_approval.py
- [[TestAllowDenyList]] - code - gateway/tests/test_mcp_proxy.py
- [[TestExtractEgressTargets]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[TestMCPProxyIntegration]] - code - gateway/tests/test_enhanced_approval.py
- [[Top-level MCP proxy configuration.]] - rationale - gateway/proxy/mcp_config.py
- [[Wire optional event bus for privacysecurity telemetry.]] - rationale - gateway/proxy/mcp_proxy.py
- [[_add()]] - code - gateway/proxy/mcp_proxy.py
- [[_scrub()]] - code - gateway/proxy/mcp_proxy.py
- [[_walk()_1]] - code - gateway/proxy/mcp_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/MCPProxy
SORT file.name ASC
```

## Connections to other communities
- 15 edges to [[_COMMUNITY_MCPToolCall]]
- 11 edges to [[_COMMUNITY_test_mcp_proxy.py]]
- 8 edges to [[_COMMUNITY_EnhancedApprovalQueue]]
- 6 edges to [[_COMMUNITY_test_mcp_proxy_coverage.py]]
- 5 edges to [[_COMMUNITY_MCPPermissionManager]]
- 5 edges to [[_COMMUNITY_MCPServerConfig]]
- 5 edges to [[_COMMUNITY_PermissionLevel]]
- 4 edges to [[_COMMUNITY_mcp_proxy.py]]
- 4 edges to [[_COMMUNITY_load_config]]
- 2 edges to [[_COMMUNITY_MCPAuditTrail]]
- 2 edges to [[_COMMUNITY_lifespan.py]]
- 2 edges to [[_COMMUNITY_lifespan]]
- 2 edges to [[_COMMUNITY_ingest_apimain.py]]
- 1 edge to [[_COMMUNITY_SecurityPipeline]]

## Top bridge nodes
- [[MCPProxy]] - degree 44, connects to 12 communities
- [[MCPProxyConfig]] - degree 21, connects to 7 communities
- [[dot-__init__()_227]] - degree 7, connects to 5 communities
- [[TestAllowDenyList]] - degree 7, connects to 3 communities
- [[dot-process_tool_call()]] - degree 9, connects to 2 communities
