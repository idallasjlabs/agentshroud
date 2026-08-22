---
source_file: "gateway/proxy/mcp_proxy.py"
type: "code"
community: "Mcp Proxy Coverage"
location: "L158"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Mcp_Proxy_Coverage
---

# HttpSseConnection

## Connections
- [[.__init__()_29]] - `method` [EXTRACTED]
- [[.get_or_create()]] - `references` [EXTRACTED]
- [[.send_request()_1]] - `method` [EXTRACTED]
- [[.stop()_3]] - `method` [EXTRACTED]
- [[.test_missing_aiohttp_raises_runtime_error()]] - `calls` [EXTRACTED]
- [[.test_send_request_and_session_reuse()]] - `calls` [EXTRACTED]
- [[Exception_4]] - `uses` [INFERRED]
- [[FakeApprovalQueue]] - `uses` [INFERRED]
- [[FakeConn]] - `uses` [INFERRED]
- [[FakeProcess]] - `uses` [INFERRED]
- [[InspectionResult]] - `uses` [INFERRED]
- [[MCPAuditTrail]] - `uses` [INFERRED]
- [[MCPInspector]] - `uses` [INFERRED]
- [[MCPPermissionManager]] - `uses` [INFERRED]
- [[MCPProxy_1]] - `uses` [INFERRED]
- [[MCPProxyConfig]] - `uses` [INFERRED]
- [[MCPProxyConfig_3]] - `uses` [INFERRED]
- [[MCPServerConfig]] - `uses` [INFERRED]
- [[MCPToolCall_1]] - `uses` [INFERRED]
- [[MCPTransport]] - `uses` [INFERRED]
- [[Manages an HTTPSSE connection to an MCP server.]] - `rationale_for` [EXTRACTED]
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

#graphify/code #graphify/INFERRED #community/Mcp_Proxy_Coverage