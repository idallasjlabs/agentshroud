---
type: community
cohesion: 0.07
members: 42
---

# Mcp Proxy Coverage

**Cohesion:** 0.07 - loosely connected
**Members:** 42 nodes

## Members
- [[.__init__()_29]] - code - gateway/proxy/mcp_proxy.py
- [[.__init__()_28]] - code - gateway/proxy/mcp_proxy.py
- [[._fake_aiohttp()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[.get_or_create()]] - code - gateway/proxy/mcp_proxy.py
- [[.is_running()]] - code - gateway/proxy/mcp_proxy.py
- [[.kill()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[.send_request()]] - code - gateway/proxy/mcp_proxy.py
- [[.send_request()_2]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[.shutdown()]] - code - gateway/proxy/mcp_proxy.py
- [[.start()_1]] - code - gateway/proxy/mcp_proxy.py
- [[.stop()_3]] - code - gateway/proxy/mcp_proxy.py
- [[.stop()_2]] - code - gateway/proxy/mcp_proxy.py
- [[.stop()_12]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[.stop_all()]] - code - gateway/proxy/mcp_proxy.py
- [[.terminate()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[.test_bare_host_in_destination_field()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[.test_bare_host_in_non_destination_field_ignored()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[.test_direct_urls_dedup_and_lists()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[.test_invalid_url_without_netloc_ignored()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[.test_list_inherits_parent_key()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[.test_missing_aiohttp_raises_runtime_error()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[.test_non_matching_text_in_destination_field()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[.test_send_request_and_session_reuse()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[.test_start_send_and_stop()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[.test_start_without_env_passes_none()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[.test_stop_kills_on_wait_timeout()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[.wait()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[Clean shutdown — close all connections.]] - rationale - gateway/proxy/mcp_proxy.py
- [[FakeProcess]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[Get existing connection or create a new one.]] - rationale - gateway/proxy/mcp_proxy.py
- [[HttpSseConnection]] - code - gateway/proxy/mcp_proxy.py
- [[MCPServerConfig_2]] - code - gateway/proxy/mcp_proxy.py
- [[Manages a stdio connection to an MCP server process.]] - rationale - gateway/proxy/mcp_proxy.py
- [[Manages an HTTPSSE connection to an MCP server.]] - rationale - gateway/proxy/mcp_proxy.py
- [[Send a JSON-RPC request and read the response.]] - rationale - gateway/proxy/mcp_proxy.py
- [[Stand-in for asyncio.subprocess.Process — no real child process.]] - rationale - gateway/tests/test_mcp_proxy_coverage.py
- [[Start the MCP server process.]] - rationale - gateway/proxy/mcp_proxy.py
- [[StdioConnection]] - code - gateway/proxy/mcp_proxy.py
- [[Stop the MCP server process.]] - rationale - gateway/proxy/mcp_proxy.py
- [[TestExtractEgressTargets]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[TestHttpSseConnection]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[TestStdioConnection]] - code - gateway/tests/test_mcp_proxy_coverage.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Mcp_Proxy_Coverage
SORT file.name ASC
```

## Connections to other communities
- 36 edges to [[_COMMUNITY_Mcp Proxy Coverage]]
- 31 edges to [[_COMMUNITY_Mcp Proxy]]
- 25 edges to [[_COMMUNITY_Mcp Permissions]]
- 8 edges to [[_COMMUNITY_Mcp Proxy]]
- 7 edges to [[_COMMUNITY_Mcp Audit (proxy)]]
- 7 edges to [[_COMMUNITY_Mcp Permissions (proxy)]]
- 3 edges to [[_COMMUNITY_Mcp Inspector (proxy)]]
- 3 edges to [[_COMMUNITY_Mcp Proxy (proxy)]]
- 1 edge to [[_COMMUNITY_Slack Proxy Coverage]]

## Top bridge nodes
- [[HttpSseConnection]] - degree 35, connects to 8 communities
- [[StdioConnection]] - degree 38, connects to 7 communities
- [[FakeProcess]] - degree 23, connects to 7 communities
- [[TestExtractEgressTargets]] - degree 21, connects to 6 communities
- [[TestHttpSseConnection]] - degree 18, connects to 6 communities