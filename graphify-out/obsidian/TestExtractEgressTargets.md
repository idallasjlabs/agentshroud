---
source_file: "gateway/tests/test_mcp_proxy_coverage.py"
type: "code"
community: "MCP Config & Proxy"
location: "L346"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/MCP_Config__Proxy
---

# TestExtractEgressTargets

## Connections
- [[.test_bare_host_in_destination_field()]] - `method` [EXTRACTED]
- [[.test_bare_host_in_non_destination_field_ignored()]] - `method` [EXTRACTED]
- [[.test_direct_urls_dedup_and_lists()]] - `method` [EXTRACTED]
- [[.test_invalid_url_without_netloc_ignored()]] - `method` [EXTRACTED]
- [[.test_list_inherits_parent_key()]] - `method` [EXTRACTED]
- [[.test_non_matching_text_in_destination_field()]] - `method` [EXTRACTED]
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
