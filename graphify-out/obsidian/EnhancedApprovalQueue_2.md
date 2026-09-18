---
source_file: "gateway/tests/test_mfa_guard.py"
type: "code"
community: "ApprovalRequest"
location: "L410"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/ApprovalRequest
---

# EnhancedApprovalQueue

## Connections
- [[ApprovalQueue_1]] - `uses` [INFERRED]
- [[ApprovalQueueConfig_2]] - `uses` [INFERRED]
- [[ApprovalRequest_2]] - `uses` [INFERRED]
- [[ApprovalStore]] - `uses` [INFERRED]
- [[EnhancedApprovalQueue_1]] - `uses` [INFERRED]
- [[MFAGuard_2]] - `uses` [INFERRED]
- [[MFAResult]] - `uses` [INFERRED]
- [[ToolRiskConfig]] - `uses` [INFERRED]
- [[_submit_enhanced_high_risk()]] - `references` [EXTRACTED]
- [[_submit_tool_call()]] - `references` [EXTRACTED]
- [[enhanced_mfa_queue()]] - `calls` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/ApprovalRequest