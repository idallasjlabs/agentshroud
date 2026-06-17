---
type: community
cohesion: 0.09
members: 79
---

# MCP Config & Proxy

**Cohesion:** 0.09 - loosely connected
**Members:** 79 nodes

## Members
- [[.__init__()_18]] - code - gateway/proxy/mcp_inspector.py
- [[.__init__()_22]] - code - gateway/proxy/mcp_proxy.py
- [[.__init__()_21]] - code - gateway/proxy/mcp_proxy.py
- [[.__init__()_23]] - code - gateway/proxy/mcp_proxy.py
- [[.__init__()_20]] - code - gateway/proxy/mcp_proxy.py
- [[._fake_aiohttp()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[.from_dict()]] - code - gateway/proxy/mcp_config.py
- [[.get_or_create()]] - code - gateway/proxy/mcp_proxy.py
- [[.is_running()]] - code - gateway/proxy/mcp_proxy.py
- [[.kill()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[.remove()]] - code - gateway/proxy/mcp_proxy.py
- [[.send_request()_2]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[.stop()_2]] - code - gateway/proxy/mcp_proxy.py
- [[.stop()_11]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[.terminate()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[.test_bare_host_in_destination_field()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[.test_bare_host_in_non_destination_field_ignored()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[.test_direct_urls_dedup_and_lists()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[.test_get_or_create_by_transport_and_caching()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[.test_invalid_url_without_netloc_ignored()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[.test_list_inherits_parent_key()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[.test_missing_aiohttp_raises_runtime_error()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[.test_no_patterns_returns_unchanged()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[.test_non_matching_text_in_destination_field()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[.test_owner_bypasses_redaction()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[.test_passthrough_process_tool_result()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[.test_passthrough_with_execute()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[.test_redacts_nested_dict_list_tuple()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[.test_send_request_and_session_reuse()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[.test_start_send_and_stop()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[.test_start_without_env_passes_none()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[.test_stop_all_clears_pool()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[.test_stop_kills_on_wait_timeout()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[.test_tool_call_generates_id_and_timestamp()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[.wait()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[Any_13]] - code - gateway/proxy/mcp_config.py
- [[Configuration for a specific MCP tool.]] - rationale - gateway/proxy/mcp_config.py
- [[Configuration for an MCP server.]] - rationale - gateway/proxy/mcp_config.py
- [[ConnectionPool]] - code - gateway/proxy/mcp_proxy.py
- [[EnhancedApprovalQueue_1]] - code - gateway/proxy/mcp_proxy.py
- [[Exception_3]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[FakeProcess]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[Get existing connection or create a new one.]] - rationale - gateway/proxy/mcp_proxy.py
- [[HttpSseConnection]] - code - gateway/proxy/mcp_proxy.py
- [[Inspects MCP tool calls and responses for security threats.]] - rationale - gateway/proxy/mcp_inspector.py
- [[MCPAuditTrail_1]] - code - gateway/proxy/mcp_proxy.py
- [[MCPInspector_1]] - code - gateway/proxy/mcp_proxy.py
- [[MCPInspector]] - code - gateway/proxy/mcp_inspector.py
- [[MCPPermissionManager_1]] - code - gateway/proxy/mcp_proxy.py
- [[MCPProxy_1]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[MCPProxyConfig_2]] - code - gateway/proxy/mcp_proxy.py
- [[MCPProxyConfig_3]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[MCPProxyConfig]] - code - gateway/proxy/mcp_config.py
- [[MCPServerConfig_2]] - code - gateway/proxy/mcp_proxy.py
- [[MCPServerConfig]] - code - gateway/proxy/mcp_config.py
- [[MCPToolCall_1]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[MCPToolConfig]] - code - gateway/proxy/mcp_config.py
- [[MCPTransport]] - code - gateway/proxy/mcp_config.py
- [[Manages a stdio connection to an MCP server process.]] - rationale - gateway/proxy/mcp_proxy.py
- [[Manages an HTTPSSE connection to an MCP server.]] - rationale - gateway/proxy/mcp_proxy.py
- [[Parse config from a dictionary (e.g. loaded from YAML).]] - rationale - gateway/proxy/mcp_config.py
- [[Pool of connections to MCP servers.]] - rationale - gateway/proxy/mcp_proxy.py
- [[Stand-in for asyncio.subprocess.Process — no real child process.]] - rationale - gateway/tests/test_mcp_proxy_coverage.py
- [[StdioConnection]] - code - gateway/proxy/mcp_proxy.py
- [[Stop the MCP server process.]] - rationale - gateway/proxy/mcp_proxy.py
- [[TestConnectionPool]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[TestDataclasses]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[TestEgressFilterPaths]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[TestEmitPrivacyEvent]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[TestExtractEgressTargets]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[TestHttpSseConnection]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[TestPassthrough]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[TestSanitizeAdminPrivateData]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[TestStdioConnection]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[Top-level MCP proxy configuration.]] - rationale - gateway/proxy/mcp_config.py
- [[config()_1]] - code - gateway/tests/test_mcp_permissions.py
- [[config()_2]] - code - gateway/tests/test_mcp_proxy.py
- [[make_config()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[test_mcp_proxy_coverage.py]] - code - gateway/tests/test_mcp_proxy_coverage.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/MCP_Config__Proxy
SORT file.name ASC
```

## Connections to other communities
- 97 edges to [[_COMMUNITY_Module Group 78]]
- 65 edges to [[_COMMUNITY_Module Group 124]]
- 56 edges to [[_COMMUNITY_MCP Permissions Manager]]
- 55 edges to [[_COMMUNITY_MCP Inspector & Audit]]
- 32 edges to [[_COMMUNITY_Module Group 154]]
- 31 edges to [[_COMMUNITY_Module Group 266]]
- 29 edges to [[_COMMUNITY_Module Group 139]]
- 8 edges to [[_COMMUNITY_Module Group 205]]
- 5 edges to [[_COMMUNITY_Module Group 387]]
- 5 edges to [[_COMMUNITY_Module Group 442]]
- 5 edges to [[_COMMUNITY_Module Group 468]]
- 2 edges to [[_COMMUNITY_Gateway Config & Lifespan]]
- 2 edges to [[_COMMUNITY_URL Analyzer & Content Scanner]]
- 2 edges to [[_COMMUNITY_Module Group 546]]
- 1 edge to [[_COMMUNITY_CLI & Core Gateway Routes]]
- 1 edge to [[_COMMUNITY_Module Group 74]]

## Top bridge nodes
- [[MCPProxyConfig]] - degree 86, connects to 13 communities
- [[MCPServerConfig]] - degree 89, connects to 11 communities
- [[MCPTransport]] - degree 62, connects to 11 communities
- [[MCPInspector]] - degree 73, connects to 10 communities
- [[MCPToolConfig]] - degree 58, connects to 10 communities