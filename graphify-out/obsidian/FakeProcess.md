---
source_file: "gateway/tests/test_mcp_proxy_coverage.py"
type: "code"
community: "MCP Config & Proxy"
location: "L93"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/MCP_Config__Proxy
---

# FakeProcess

## Connections
- [[.__init__()_126]] - `method` [EXTRACTED]
- [[.kill()]] - `method` [EXTRACTED]
- [[.terminate()]] - `method` [EXTRACTED]
- [[.test_start_send_and_stop()]] - `calls` [EXTRACTED]
- [[.test_start_without_env_passes_none()]] - `calls` [EXTRACTED]
- [[.test_stop_kills_on_wait_timeout()]] - `calls` [EXTRACTED]
- [[.wait()]] - `method` [EXTRACTED]
- [[ConnectionPool]] - `uses` [INFERRED]
- [[HttpSseConnection]] - `uses` [INFERRED]
- [[MCPAuditTrail]] - `uses` [INFERRED]
- [[MCPInspector]] - `uses` [INFERRED]
- [[MCPPermissionManager]] - `uses` [INFERRED]
- [[MCPProxy]] - `uses` [INFERRED]
- [[MCPProxyConfig]] - `uses` [INFERRED]
- [[MCPServerConfig]] - `uses` [INFERRED]
- [[MCPToolCall]] - `uses` [INFERRED]
- [[MCPToolConfig]] - `uses` [INFERRED]
- [[MCPToolResult]] - `uses` [INFERRED]
- [[MCPTransport]] - `uses` [INFERRED]
- [[PermissionLevel]] - `uses` [INFERRED]
- [[Stand-in for asyncio.subprocess.Process — no real child process.]] - `rationale_for` [EXTRACTED]
- [[StdioConnection]] - `uses` [INFERRED]
- [[test_mcp_proxy_coverage.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/MCP_Config__Proxy