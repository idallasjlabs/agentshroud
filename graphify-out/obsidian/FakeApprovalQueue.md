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
- [[dot-__init__()_46]] - `method` [EXTRACTED]
- [[dot-get_item()]] - `method` [EXTRACTED]
- [[dot-submit_tool_request()]] - `method` [EXTRACTED]
- [[dot-test_allowlisted_domain_still_prompts_when_approval_all_enabled()]] - `calls` [INFERRED]
- [[dot-test_approved_decision_allows()]] - `calls` [EXTRACTED]
- [[dot-test_denied_decision_blocks_with_item_status()]] - `calls` [EXTRACTED]
- [[dot-test_denied_decision_with_missing_item_defaults_denied()]] - `calls` [EXTRACTED]
- [[dot-test_process_tool_call_blocks_on_denial()]] - `calls` [EXTRACTED]
- [[dot-test_tool_not_requiring_approval_allowed()]] - `calls` [EXTRACTED]
- [[dot-test_unknown_domain_allowed_when_approved()]] - `calls` [INFERRED]
- [[dot-test_unknown_domain_denied_when_denied()]] - `calls` [INFERRED]
- [[dot-wait_for_decision()]] - `method` [EXTRACTED]
- [[ConnectionPool]] - `uses` [INFERRED]
- [[HttpSseConnection]] - `uses` [INFERRED]
- [[MCPAuditTrail]] - `uses` [INFERRED]
- [[MCPInspector]] - `uses` [INFERRED]
- [[MCPPermissionManager_1]] - `uses` [INFERRED]
- [[MCPProxy_1]] - `uses` [INFERRED]
- [[MCPProxyConfig_3]] - `uses` [INFERRED]
- [[MCPServerConfig_2]] - `uses` [INFERRED]
- [[MCPToolCall]] - `uses` [INFERRED]
- [[MCPToolConfig]] - `uses` [INFERRED]
- [[MCPToolResult]] - `uses` [INFERRED]
- [[MCPTransport]] - `uses` [INFERRED]
- [[PermissionLevel]] - `uses` [INFERRED]
- [[StdioConnection]] - `uses` [INFERRED]
- [[test_mcp_proxy_coverage.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/StdioConnection
