---
type: community
cohesion: 0.19
members: 15
---

# FakeProcess

**Cohesion:** 0.19 - loosely connected
**Members:** 15 nodes

## Members
- [[._fake_aiohttp()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[.kill()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[.send_request()_1]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[.stop()_3]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[.terminate()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[.test_missing_aiohttp_raises_runtime_error()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[.test_send_request_and_session_reuse()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[.test_start_send_and_stop()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[.test_start_without_env_passes_none()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[.test_stop_kills_on_wait_timeout()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[.wait()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[FakeProcess]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[Stand-in for asyncio.subprocess.Process — no real child process.]] - rationale - gateway/tests/test_mcp_proxy_coverage.py
- [[TestHttpSseConnection]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[TestStdioConnection]] - code - gateway/tests/test_mcp_proxy_coverage.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/FakeProcess
SORT file.name ASC
```

## Connections to other communities
- 19 edges to [[_COMMUNITY_StdioConnection]]
- 14 edges to [[_COMMUNITY_MCPServerConfig]]
- 6 edges to [[_COMMUNITY_PermissionLevel]]
- 6 edges to [[_COMMUNITY_MCPToolCall]]
- 3 edges to [[_COMMUNITY_MCPAuditTrail]]
- 3 edges to [[_COMMUNITY_MCPInspector]]
- 3 edges to [[_COMMUNITY_MCPPermissionManager]]
- 3 edges to [[_COMMUNITY_MCPToolResult]]
- 1 edge to [[_COMMUNITY_AsyncMock]]

## Top bridge nodes
- [[FakeProcess]] - degree 23, connects to 9 communities
- [[TestHttpSseConnection]] - degree 18, connects to 8 communities
- [[TestStdioConnection]] - degree 18, connects to 8 communities
- [[.test_send_request_and_session_reuse()]] - degree 6, connects to 2 communities
- [[.test_start_send_and_stop()]] - degree 6, connects to 2 communities