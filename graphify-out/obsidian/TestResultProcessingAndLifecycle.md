---
source_file: "gateway/tests/test_mcp_proxy_coverage.py"
type: "code"
community: "Community 103"
location: "L677"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Community_103
---

# TestResultProcessingAndLifecycle

## Connections
- [[.test_get_stats_after_allowed_call()]] - `method` [EXTRACTED]
- [[.test_get_stats_zero_and_after_calls()]] - `method` [EXTRACTED]
- [[.test_process_tool_result_handles_none_content()]] - `method` [EXTRACTED]
- [[.test_process_tool_result_redacts_private_data()]] - `method` [EXTRACTED]
- [[.test_shutdown_stops_all_connections()]] - `method` [EXTRACTED]
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

#graphify/code #graphify/INFERRED #community/Community_103