---
type: community
cohesion: 0.06
members: 48
---

# StdioConnection

**Cohesion:** 0.06 - loosely connected
**Members:** 48 nodes

## Members
- [[dot-__init__()_57]] - code - gateway/proxy/mcp_proxy.py
- [[dot-__init__()_58]] - code - gateway/proxy/mcp_proxy.py
- [[dot-__init__()_59]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[dot-_execute_tool_call()]] - code - gateway/proxy/mcp_proxy.py
- [[dot-_fake_aiohttp()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[dot-get_or_create()]] - code - gateway/proxy/mcp_proxy.py
- [[dot-is_running()]] - code - gateway/proxy/mcp_proxy.py
- [[dot-kill()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[dot-send_request()]] - code - gateway/proxy/mcp_proxy.py
- [[dot-send_request()_1]] - code - gateway/proxy/mcp_proxy.py
- [[dot-send_request()_2]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[dot-shutdown()]] - code - gateway/proxy/mcp_proxy.py
- [[dot-start()_1]] - code - gateway/proxy/mcp_proxy.py
- [[dot-stop()_1]] - code - gateway/proxy/mcp_proxy.py
- [[dot-stop()_2]] - code - gateway/proxy/mcp_proxy.py
- [[dot-stop()_3]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[dot-stop_all()]] - code - gateway/proxy/mcp_proxy.py
- [[dot-terminate()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[dot-test_bare_host_in_destination_field()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[dot-test_bare_host_in_non_destination_field_ignored()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[dot-test_direct_urls_dedup_and_lists()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[dot-test_invalid_url_without_netloc_ignored()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[dot-test_list_inherits_parent_key()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[dot-test_missing_aiohttp_raises_runtime_error()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[dot-test_non_matching_text_in_destination_field()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[dot-test_send_request_and_session_reuse()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[dot-test_start_send_and_stop()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[dot-test_start_without_env_passes_none()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[dot-test_stop_kills_on_wait_timeout()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[dot-wait()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[Actually execute the tool call against the MCP server.]] - rationale - gateway/proxy/mcp_proxy.py
- [[Clean shutdown — close all connections.]] - rationale - gateway/proxy/mcp_proxy.py
- [[Exception]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[FakeProcess]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[Get existing connection or create a new one.]] - rationale - gateway/proxy/mcp_proxy.py
- [[HttpSseConnection]] - code - gateway/proxy/mcp_proxy.py
- [[MCPServerConfig]] - code - gateway/proxy/mcp_proxy.py
- [[Manages a stdio connection to an MCP server process.]] - rationale - gateway/proxy/mcp_proxy.py
- [[Manages an HTTPSSE connection to an MCP server.]] - rationale - gateway/proxy/mcp_proxy.py
- [[Send a JSON-RPC request and read the response.]] - rationale - gateway/proxy/mcp_proxy.py
- [[Send an HTTP request to the MCP server.]] - rationale - gateway/proxy/mcp_proxy.py
- [[Stand-in for asyncio.subprocess.Process — no real child process.]] - rationale - gateway/tests/test_mcp_proxy_coverage.py
- [[Start the MCP server process.]] - rationale - gateway/proxy/mcp_proxy.py
- [[StdioConnection]] - code - gateway/proxy/mcp_proxy.py
- [[Stop the MCP server process.]] - rationale - gateway/proxy/mcp_proxy.py
- [[TestExtractEgressTargets]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[TestHttpSseConnection]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[TestStdioConnection]] - code - gateway/tests/test_mcp_proxy_coverage.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/StdioConnection
SORT file.name ASC
```

## Connections to other communities
- 37 edges to [[_COMMUNITY_CrossBotTrustLedger]]
- 34 edges to [[_COMMUNITY_test_bots_ssh_exec_wrapper.py]]
- 22 edges to [[_COMMUNITY_MCPInspector]]
- 13 edges to [[_COMMUNITY_MCPToolCall]]
- 10 edges to [[_COMMUNITY_What Does OpenClaw Actually Need to Write]]
- 10 edges to [[_COMMUNITY_MCPToolResult]]
- 8 edges to [[_COMMUNITY_MCPPermissionManager (2)_1]]
- 1 edge to [[_COMMUNITY_AgentShroud Security Value Proposition]]
- 1 edge to [[_COMMUNITY_api.py (2)]]

## Top bridge nodes
- [[FakeProcess]] - degree 23, connects to 8 communities
- [[TestExtractEgressTargets]] - degree 21, connects to 7 communities
- [[TestHttpSseConnection]] - degree 18, connects to 7 communities
- [[TestStdioConnection]] - degree 18, connects to 7 communities
- [[Exception]] - degree 15, connects to 7 communities
