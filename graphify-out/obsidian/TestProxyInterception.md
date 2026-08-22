---
source_file: "gateway/tests/test_mcp_proxy.py"
type: "code"
community: "Mcp Permissions (proxy)"
location: "L442"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Mcp_Permissions_proxy
---

# TestProxyInterception

## Connections
- [[.test_audit_entry_created()]] - `method` [EXTRACTED]
- [[.test_clean_call_allowed()]] - `method` [EXTRACTED]
- [[.test_egress_allows_non_url_tool_call()]] - `method` [EXTRACTED]
- [[.test_egress_denied_blocks_url_tool_call()]] - `method` [EXTRACTED]
- [[.test_injection_blocked()]] - `method` [EXTRACTED]
- [[.test_pii_redacted_in_params()]] - `method` [EXTRACTED]
- [[FindingType]] - `uses` [INFERRED]
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
- [[ThreatLevel]] - `uses` [INFERRED]
- [[test_mcp_proxy.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Mcp_Permissions_proxy