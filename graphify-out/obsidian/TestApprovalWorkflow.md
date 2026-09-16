---
source_file: "gateway/tests/test_enhanced_approval.py"
type: "code"
community: "Enhanced Approval Queue"
location: "L143"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Enhanced_Approval_Queue
---

# TestApprovalWorkflow

## Connections
- [[dot-test_critical_tool_approval_flow()]] - `method` [EXTRACTED]
- [[dot-test_critical_tool_denial_flow()]] - `method` [EXTRACTED]
- [[dot-test_low_risk_tool_no_approval()]] - `method` [EXTRACTED]
- [[dot-test_timeout_auto_deny()]] - `method` [EXTRACTED]
- [[dot-test_wait_for_decision()]] - `method` [EXTRACTED]
- [[ApprovalQueueConfig_2]] - `uses` [INFERRED]
- [[ApprovalRequest_2]] - `uses` [INFERRED]
- [[ApprovalStore]] - `uses` [INFERRED]
- [[EnhancedApprovalQueue_1]] - `uses` [INFERRED]
- [[MCPProxy_1]] - `uses` [INFERRED]
- [[MCPToolCall_1]] - `uses` [INFERRED]
- [[Test the complete approval workflow.]] - `rationale_for` [EXTRACTED]
- [[ToolRiskConfig]] - `uses` [INFERRED]
- [[ToolRiskPolicy]] - `uses` [INFERRED]
- [[test_enhanced_approval.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Enhanced_Approval_Queue