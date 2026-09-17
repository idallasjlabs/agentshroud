---
source_file: "gateway/tests/test_mcp_proxy_coverage.py"
type: "code"
community: "StdioConnection"
location: "L462"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/StdioConnection
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
- [[StdioConnection]] - `uses` [INFERRED]
- [[test_mcp_proxy_coverage.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/StdioConnection