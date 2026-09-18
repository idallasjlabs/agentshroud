---
source_file: "gateway/tests/test_mcp_proxy_coverage.py"
type: "code"
community: "StdioConnection"
location: "L122"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/StdioConnection
---

# FakeConn

## Connections
- [[.__init__()_31]] - `method` [EXTRACTED]
- [[.send_request()_1]] - `method` [EXTRACTED]
- [[.stop()_3]] - `method` [EXTRACTED]
- [[.test_execution_redacts_admin_private_content()]] - `calls` [EXTRACTED]
- [[.test_execution_with_none_content_skips_result_inspection()]] - `calls` [EXTRACTED]
- [[.test_generic_exception()]] - `calls` [EXTRACTED]
- [[.test_passthrough_with_execute()]] - `calls` [EXTRACTED]
- [[.test_sanitized_params_preferred_over_originals()]] - `calls` [EXTRACTED]
- [[.test_server_error_response()]] - `calls` [EXTRACTED]
- [[.test_server_error_response_without_message()]] - `calls` [EXTRACTED]
- [[.test_shutdown_stops_all_connections()]] - `calls` [EXTRACTED]
- [[.test_stop_all_clears_pool()]] - `calls` [EXTRACTED]
- [[.test_successful_execution_with_result_inspection()]] - `calls` [EXTRACTED]
- [[.test_timeout_error()]] - `calls` [EXTRACTED]
- [[ConnectionPool]] - `uses` [INFERRED]
- [[HttpSseConnection]] - `uses` [INFERRED]
- [[MCPAuditTrail_1]] - `uses` [INFERRED]
- [[MCPInspector_1]] - `uses` [INFERRED]
- [[MCPPermissionManager]] - `uses` [INFERRED]
- [[MCPProxy_1]] - `uses` [INFERRED]
- [[MCPProxyConfig_2]] - `uses` [INFERRED]
- [[MCPServerConfig_2]] - `uses` [INFERRED]
- [[MCPToolCall_1]] - `uses` [INFERRED]
- [[MCPToolConfig]] - `uses` [INFERRED]
- [[MCPToolResult]] - `uses` [INFERRED]
- [[MCPTransport]] - `uses` [INFERRED]
- [[PermissionLevel_1]] - `uses` [INFERRED]
- [[Stand-in connection injected into the proxy's pool.]] - `rationale_for` [EXTRACTED]
- [[StdioConnection]] - `uses` [INFERRED]
- [[test_mcp_proxy_coverage.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/StdioConnection