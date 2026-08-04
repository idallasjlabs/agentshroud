---
source_file: "gateway/tests/test_mcp_proxy_coverage.py"
type: "code"
community: "Module Group 124"
location: "L444"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Module_Group_124
---

# FakeApprovalQueue

## Connections
- [[.__init__()_128]] - `method` [EXTRACTED]
- [[.get_item()_2]] - `method` [EXTRACTED]
- [[.submit_tool_request()_1]] - `method` [EXTRACTED]
- [[.test_allowlisted_domain_still_prompts_when_approval_all_enabled()]] - `calls` [INFERRED]
- [[.test_approved_decision_allows()]] - `calls` [EXTRACTED]
- [[.test_denied_decision_blocks_with_item_status()]] - `calls` [EXTRACTED]
- [[.test_denied_decision_with_missing_item_defaults_denied()]] - `calls` [EXTRACTED]
- [[.test_process_tool_call_blocks_on_denial()]] - `calls` [EXTRACTED]
- [[.test_tool_not_requiring_approval_allowed()]] - `calls` [EXTRACTED]
- [[.test_unknown_domain_allowed_when_approved()]] - `calls` [INFERRED]
- [[.test_unknown_domain_denied_when_denied()]] - `calls` [INFERRED]
- [[.wait_for_decision()_1]] - `method` [EXTRACTED]
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

#graphify/code #graphify/INFERRED #community/Module_Group_124
