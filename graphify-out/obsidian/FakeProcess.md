---
source_file: "gateway/tests/test_mcp_proxy_coverage.py"
type: "code"
community: "MCPPermissionManager"
location: "L93"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/MCPPermissionManager
---

# FakeProcess

## Connections
- [[dot-__init__()_113]] - `method` [EXTRACTED]
- [[dot-kill()]] - `method` [EXTRACTED]
- [[dot-terminate()]] - `method` [EXTRACTED]
- [[dot-test_start_send_and_stop()]] - `calls` [EXTRACTED]
- [[dot-test_start_without_env_passes_none()]] - `calls` [EXTRACTED]
- [[dot-test_stop_kills_on_wait_timeout()]] - `calls` [EXTRACTED]
- [[dot-wait()]] - `method` [EXTRACTED]
- [[ConnectionPool]] - `uses` [INFERRED]
- [[HttpSseConnection]] - `uses` [INFERRED]
- [[MCPAuditTrail]] - `uses` [INFERRED]
- [[MCPInspector]] - `uses` [INFERRED]
- [[MCPPermissionManager]] - `uses` [INFERRED]
- [[MCPProxy]] - `uses` [INFERRED]
- [[MCPProxyConfig_3]] - `uses` [INFERRED]
- [[MCPServerConfig_2]] - `uses` [INFERRED]
- [[MCPToolCall_1]] - `uses` [INFERRED]
- [[MCPToolConfig]] - `uses` [INFERRED]
- [[MCPToolResult]] - `uses` [INFERRED]
- [[MCPTransport]] - `uses` [INFERRED]
- [[PermissionLevel]] - `uses` [INFERRED]
- [[Stand-in for asyncio.subprocess.Process — no real child process.]] - `rationale_for` [EXTRACTED]
- [[StdioConnection]] - `uses` [INFERRED]
- [[test_mcp_proxy_coverage.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/MCPPermissionManager
