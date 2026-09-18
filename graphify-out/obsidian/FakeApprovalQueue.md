---
source_file: "gateway/tests/test_mcp_proxy_coverage.py"
type: "code"
community: "StdioConnection"
location: "L444"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/StdioConnection
---

# FakeApprovalQueue

## Connections
- [[.__init__()_62]] - `method` [EXTRACTED]
- [[.get_item()]] - `method` [EXTRACTED]
- [[.submit_tool_request()]] - `method` [EXTRACTED]
- [[.test_allowlisted_domain_still_prompts_when_approval_all_enabled()]] - `calls` [INFERRED]
- [[.test_approved_decision_allows()]] - `calls` [EXTRACTED]
- [[.test_denied_decision_blocks_with_item_status()]] - `calls` [EXTRACTED]
- [[.test_denied_decision_with_missing_item_defaults_denied()]] - `calls` [EXTRACTED]
- [[.test_process_tool_call_blocks_on_denial()]] - `calls` [EXTRACTED]
- [[.test_tool_not_requiring_approval_allowed()]] - `calls` [EXTRACTED]
- [[.test_unknown_domain_allowed_when_approved()]] - `calls` [INFERRED]
- [[.test_unknown_domain_denied_when_denied()]] - `calls` [INFERRED]
- [[.wait_for_decision()]] - `method` [EXTRACTED]
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