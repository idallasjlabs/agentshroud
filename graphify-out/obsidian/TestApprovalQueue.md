---
source_file: "gateway/tests/test_mcp_proxy_coverage.py"
type: "code"
community: "Community 1339"
location: "L462"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Community_1339
---

# TestApprovalQueue

## Connections
- [[.test_approved_decision_allows()]] - `method` [EXTRACTED]
- [[.test_denied_decision_blocks_with_item_status()]] - `method` [EXTRACTED]
- [[.test_denied_decision_with_missing_item_defaults_denied()]] - `method` [EXTRACTED]
- [[.test_no_queue_allows_by_default()]] - `method` [EXTRACTED]
- [[.test_process_tool_call_blocks_on_denial()]] - `method` [EXTRACTED]
- [[.test_tool_not_requiring_approval_allowed()]] - `method` [EXTRACTED]
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

#graphify/code #graphify/INFERRED #community/Community_1339