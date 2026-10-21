---
source_file: "gateway/tests/test_mcp_policy.py"
type: "code"
community: "ToolResultSanitizer"
location: "L272"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/ToolResultSanitizer
---

# _FakeApprovalQueue

## Connections
- [[dot-__init__()_126]] - `method` [EXTRACTED]
- [[dot-submit_tool_request()_1]] - `method` [EXTRACTED]
- [[dot-wait_for_decision()_1]] - `method` [EXTRACTED]
- [[ApprovalQueueConfig_1]] - `uses` [INFERRED]
- [[ApprovalStore]] - `uses` [INFERRED]
- [[EnhancedApprovalQueue_1]] - `uses` [INFERRED]
- [[MCPPolicyAction]] - `uses` [INFERRED]
- [[MCPPolicyConfig_1]] - `uses` [INFERRED]
- [[MCPPolicyDecision]] - `uses` [INFERRED]
- [[MCPPolicyEngine_1]] - `uses` [INFERRED]
- [[MCPProxy_1]] - `uses` [INFERRED]
- [[MCPToolCall_1]] - `uses` [INFERRED]
- [[MCPToolResult]] - `uses` [INFERRED]
- [[Minimal stand-in for EnhancedApprovalQueue.      Records submissions and returns]] - `rationale_for` [EXTRACTED]
- [[RBACConfig_3]] - `uses` [INFERRED]
- [[ToolRiskConfig]] - `uses` [INFERRED]
- [[test_enforce_high_risk_denied_on_rejection()]] - `calls` [EXTRACTED]
- [[test_enforce_high_risk_enqueues_and_allows_on_approval()]] - `calls` [EXTRACTED]
- [[test_enforce_high_risk_queue_no_wait_denies_closed()]] - `calls` [EXTRACTED]
- [[test_mcp_policy.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/ToolResultSanitizer
