---
type: community
cohesion: 0.07
members: 50
---

# StdioConnection

**Cohesion:** 0.07 - loosely connected
**Members:** 50 nodes

## Members
- [[dot-__init__()_38]] - code - gateway/proxy/mcp_proxy.py
- [[dot-__init__()_39]] - code - gateway/proxy/mcp_proxy.py
- [[dot-__init__()_40]] - code - gateway/proxy/mcp_proxy.py
- [[dot-__init__()_41]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[dot-_fake_aiohttp()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[dot-get_or_create()]] - code - gateway/proxy/mcp_proxy.py
- [[dot-is_running()]] - code - gateway/proxy/mcp_proxy.py
- [[dot-kill()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[dot-remove()]] - code - gateway/proxy/mcp_proxy.py
- [[dot-send_request()]] - code - gateway/proxy/mcp_proxy.py
- [[dot-send_request()_1]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[dot-shutdown()]] - code - gateway/proxy/mcp_proxy.py
- [[dot-start()_1]] - code - gateway/proxy/mcp_proxy.py
- [[dot-stop()_1]] - code - gateway/proxy/mcp_proxy.py
- [[dot-stop()_2]] - code - gateway/proxy/mcp_proxy.py
- [[dot-stop()_3]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[dot-stop_all()]] - code - gateway/proxy/mcp_proxy.py
- [[dot-terminate()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[dot-test_get_or_create_by_transport_and_caching()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[dot-test_missing_aiohttp_raises_runtime_error()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[dot-test_passthrough_process_tool_result()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[dot-test_passthrough_with_execute()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[dot-test_send_request_and_session_reuse()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[dot-test_start_send_and_stop()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[dot-test_start_without_env_passes_none()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[dot-test_stop_all_clears_pool()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[dot-test_stop_kills_on_wait_timeout()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[dot-wait()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[Clean shutdown — close all connections.]] - rationale - gateway/proxy/mcp_proxy.py
- [[ConnectionPool]] - code - gateway/proxy/mcp_proxy.py
- [[Exception]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[FakeProcess]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[Get existing connection or create a new one.]] - rationale - gateway/proxy/mcp_proxy.py
- [[HttpSseConnection]] - code - gateway/proxy/mcp_proxy.py
- [[MCPProxy]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[MCPProxyConfig]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[MCPServerConfig]] - code - gateway/proxy/mcp_proxy.py
- [[Manages a stdio connection to an MCP server process.]] - rationale - gateway/proxy/mcp_proxy.py
- [[Manages an HTTPSSE connection to an MCP server.]] - rationale - gateway/proxy/mcp_proxy.py
- [[Pool of connections to MCP servers.]] - rationale - gateway/proxy/mcp_proxy.py
- [[Send a JSON-RPC request and read the response.]] - rationale - gateway/proxy/mcp_proxy.py
- [[Stand-in for asyncio.subprocess.Process — no real child process.]] - rationale - gateway/tests/test_mcp_proxy_coverage.py
- [[Start the MCP server process.]] - rationale - gateway/proxy/mcp_proxy.py
- [[StdioConnection]] - code - gateway/proxy/mcp_proxy.py
- [[Stop the MCP server process.]] - rationale - gateway/proxy/mcp_proxy.py
- [[TestConnectionPool]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[TestHttpSseConnection]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[TestPassthrough]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[TestStdioConnection]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[make_config()]] - code - gateway/tests/test_mcp_proxy_coverage.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/StdioConnection
SORT file.name ASC
```

## Connections to other communities
- 41 edges to [[_COMMUNITY_StdioConnection]]
- 35 edges to [[_COMMUNITY_MCPPermissionManager_1]]
- 31 edges to [[_COMMUNITY_MCPInspector]]
- 18 edges to [[_COMMUNITY_MCPPermissionManager]]
- 17 edges to [[_COMMUNITY_PermissionLevel]]
- 15 edges to [[_COMMUNITY_MCPPermissionManager_4]]
- 12 edges to [[_COMMUNITY_MCPAuditTrail]]
- 12 edges to [[_COMMUNITY_MCPPermissionManager_2]]
- 3 edges to [[_COMMUNITY_Athena — Knowledge Distiller_4]]
- 1 edge to [[_COMMUNITY_AsyncMock_1]]

## Top bridge nodes
- [[FakeProcess]] - degree 23, connects to 9 communities
- [[TestHttpSseConnection]] - degree 18, connects to 8 communities
- [[TestStdioConnection]] - degree 18, connects to 8 communities
- [[MCPProxy]] - degree 17, connects to 8 communities
- [[TestConnectionPool]] - degree 17, connects to 8 communities
