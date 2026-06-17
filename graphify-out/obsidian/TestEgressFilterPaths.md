---
source_file: "gateway/tests/test_mcp_proxy_coverage.py"
type: "code"
community: "MCP Config & Proxy"
location: "L518"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/MCP_Config__Proxy
---

# TestEgressFilterPaths

## Connections
- [[.test_async_egress_filter_deny_uses_rule_as_reason()]] - `method` [EXTRACTED]
- [[.test_egress_filter_allow_passes_through()]] - `method` [EXTRACTED]
- [[.test_sync_egress_filter_deny_blocks()]] - `method` [EXTRACTED]
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

#graphify/code #graphify/INFERRED #community/MCP_Config__Proxy