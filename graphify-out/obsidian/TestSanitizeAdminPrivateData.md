---
source_file: "gateway/tests/test_mcp_proxy_coverage.py"
type: "code"
community: "PermissionLevel"
location: "L379"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/PermissionLevel
---

# TestSanitizeAdminPrivateData

## Connections
- [[dot-test_no_patterns_returns_unchanged()]] - `method` [EXTRACTED]
- [[dot-test_owner_bypasses_redaction()]] - `method` [EXTRACTED]
- [[dot-test_redacts_nested_dict_list_tuple()]] - `method` [EXTRACTED]
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
- [[StdioConnection]] - `uses` [INFERRED]
- [[test_mcp_proxy_coverage.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/PermissionLevel
