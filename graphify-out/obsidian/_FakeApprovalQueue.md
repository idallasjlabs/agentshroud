---
source_file: "gateway/tests/test_mcp_policy.py"
type: "code"
community: "Community 34"
location: "L272"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Community_34
---

# _FakeApprovalQueue

## Connections
- [[.__init__()_172]] - `method` [EXTRACTED]
- [[.submit_tool_request()_3]] - `method` [EXTRACTED]
- [[.wait_for_decision()_3]] - `method` [EXTRACTED]
- [[ApprovalQueueConfig_2]] - `uses` [INFERRED]
- [[ApprovalStore_1]] - `uses` [INFERRED]
- [[EnhancedApprovalQueue]] - `uses` [INFERRED]
- [[MCPPolicyAction]] - `uses` [INFERRED]
- [[MCPPolicyConfig]] - `uses` [INFERRED]
- [[MCPPolicyDecision]] - `uses` [INFERRED]
- [[MCPPolicyEngine]] - `uses` [INFERRED]
- [[MCPProxy]] - `uses` [INFERRED]
- [[MCPToolCall]] - `uses` [INFERRED]
- [[MCPToolResult]] - `uses` [INFERRED]
- [[Minimal stand-in for EnhancedApprovalQueue.      Records submissions and returns]] - `rationale_for` [EXTRACTED]
- [[RBACConfig_1]] - `uses` [INFERRED]
- [[ToolRiskConfig_1]] - `uses` [INFERRED]
- [[test_enforce_high_risk_denied_on_rejection()]] - `calls` [EXTRACTED]
- [[test_enforce_high_risk_enqueues_and_allows_on_approval()]] - `calls` [EXTRACTED]
- [[test_enforce_high_risk_queue_no_wait_denies_closed()]] - `calls` [EXTRACTED]
- [[test_mcp_policy.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Community_34