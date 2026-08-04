---
source_file: "gateway/proxy/mcp_proxy.py"
type: "code"
community: "MCP Config & Proxy"
location: "L92"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/MCP_Config__Proxy
---

# StdioConnection

## Connections
- [[.__init__()_20]] - `method` [EXTRACTED]
- [[.get_or_create()]] - `references` [EXTRACTED]
- [[.is_running()]] - `method` [EXTRACTED]
- [[.send_request()]] - `method` [EXTRACTED]
- [[.start()_1]] - `method` [EXTRACTED]
- [[.stop()_2]] - `method` [EXTRACTED]
- [[.test_start_send_and_stop()]] - `calls` [EXTRACTED]
- [[.test_start_without_env_passes_none()]] - `calls` [EXTRACTED]
- [[.test_stop_kills_on_wait_timeout()]] - `calls` [EXTRACTED]
- [[Exception_3]] - `uses` [INFERRED]
- [[FakeApprovalQueue]] - `uses` [INFERRED]
- [[FakeConn]] - `uses` [INFERRED]
- [[FakeProcess]] - `uses` [INFERRED]
- [[MCPAuditTrail]] - `uses` [INFERRED]
- [[MCPInspector]] - `uses` [INFERRED]
- [[MCPPermissionManager]] - `uses` [INFERRED]
- [[MCPProxy_1]] - `uses` [INFERRED]
- [[MCPProxyConfig_3]] - `uses` [INFERRED]
- [[MCPProxyConfig]] - `uses` [INFERRED]
- [[MCPServerConfig]] - `uses` [INFERRED]
- [[MCPToolCall_1]] - `uses` [INFERRED]
- [[MCPTransport]] - `uses` [INFERRED]
- [[Manages a stdio connection to an MCP server process.]] - `rationale_for` [EXTRACTED]
- [[TestApprovalQueue]] - `uses` [INFERRED]
- [[TestConnectionPool]] - `uses` [INFERRED]
- [[TestDataclasses]] - `uses` [INFERRED]
- [[TestEgressFilterPaths]] - `uses` [INFERRED]
- [[TestEmitPrivacyEvent]] - `uses` [INFERRED]
- [[TestExecuteToolCall]] - `uses` [INFERRED]
- [[TestExtractEgressTargets]] - `uses` [INFERRED]
- [[TestHttpSseConnection]] - `uses` [INFERRED]
- [[TestPassthrough]] - `uses` [INFERRED]
- [[TestResultProcessingAndLifecycle]] - `uses` [INFERRED]
- [[TestSanitizeAdminPrivateData]] - `uses` [INFERRED]
- [[TestStdioConnection]] - `uses` [INFERRED]
- [[mcp_proxy.py]] - `contains` [EXTRACTED]
- [[test_mcp_proxy_coverage.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/MCP_Config__Proxy
