---
source_file: "gateway/tests/test_mcp_proxy_coverage.py"
type: "code"
community: "Gateway Test Suite"
location: "L561"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Gateway_Test_Suite
---

# TestExecuteToolCall

## Connections
- [[.test_execution_redacts_admin_private_content()]] - `method` [EXTRACTED]
- [[.test_execution_with_none_content_skips_result_inspection()]] - `method` [EXTRACTED]
- [[.test_generic_exception()]] - `method` [EXTRACTED]
- [[.test_sanitized_params_preferred_over_originals()]] - `method` [EXTRACTED]
- [[.test_server_error_response()]] - `method` [EXTRACTED]
- [[.test_server_error_response_without_message()]] - `method` [EXTRACTED]
- [[.test_successful_execution_with_result_inspection()]] - `method` [EXTRACTED]
- [[.test_timeout_error()]] - `method` [EXTRACTED]
- [[.test_unknown_server_returns_error_result()]] - `method` [EXTRACTED]
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
- [[StdioConnection]] - `uses` [INFERRED]
- [[test_mcp_proxy_coverage.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Gateway_Test_Suite