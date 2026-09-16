---
source_file: "gateway/tests/test_mcp_proxy_coverage.py"
type: "code"
community: "Community 143"
location: "L122"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Community_143
---

# FakeConn

## Connections
- [[dot-__init__()_31]] - `method` [EXTRACTED]
- [[dot-send_request()_1]] - `method` [EXTRACTED]
- [[dot-stop()_3]] - `method` [EXTRACTED]
- [[dot-test_execution_redacts_admin_private_content()]] - `calls` [EXTRACTED]
- [[dot-test_execution_with_none_content_skips_result_inspection()]] - `calls` [EXTRACTED]
- [[dot-test_generic_exception()]] - `calls` [EXTRACTED]
- [[dot-test_passthrough_with_execute()]] - `calls` [EXTRACTED]
- [[dot-test_sanitized_params_preferred_over_originals()]] - `calls` [EXTRACTED]
- [[dot-test_server_error_response()]] - `calls` [EXTRACTED]
- [[dot-test_server_error_response_without_message()]] - `calls` [EXTRACTED]
- [[dot-test_shutdown_stops_all_connections()]] - `calls` [EXTRACTED]
- [[dot-test_stop_all_clears_pool()]] - `calls` [EXTRACTED]
- [[dot-test_successful_execution_with_result_inspection()]] - `calls` [EXTRACTED]
- [[dot-test_timeout_error()]] - `calls` [EXTRACTED]
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

#graphify/code #graphify/EXTRACTED #community/Community_143