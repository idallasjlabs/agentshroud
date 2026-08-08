---
source_file: "gateway/tests/test_mcp_proxy_coverage.py"
type: "code"
community: "Gateway Test Suite"
location: "L379"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Gateway_Test_Suite
---

# TestSanitizeAdminPrivateData

## Connections
- [[.test_no_patterns_returns_unchanged()]] - `method` [EXTRACTED]
- [[.test_owner_bypasses_redaction()]] - `method` [EXTRACTED]
- [[.test_redacts_nested_dict_list_tuple()]] - `method` [EXTRACTED]
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