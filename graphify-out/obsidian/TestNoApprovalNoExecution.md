---
source_file: "gateway/tests/test_edge_approvals.py"
type: "code"
community: "Community 25"
location: "L67"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Community_25
---

# TestNoApprovalNoExecution

## Connections
- [[.test_approved_executes_exactly_once()]] - `method` [EXTRACTED]
- [[.test_concurrent_redeem_executes_once()]] - `method` [EXTRACTED]
- [[.test_expired_is_denied()]] - `method` [EXTRACTED]
- [[.test_first_call_returns_pending_ticket_and_notifies()]] - `method` [EXTRACTED]
- [[.test_queue_timeout_is_deny()]] - `method` [EXTRACTED]
- [[.test_rejected_is_denied()]] - `method` [EXTRACTED]
- [[.test_unapproved_ticket_is_pending_not_executed()]] - `method` [EXTRACTED]
- [[ApprovalContext]] - `uses` [INFERRED]
- [[ApprovalDenied]] - `uses` [INFERRED]
- [[ApprovalPending]] - `uses` [INFERRED]
- [[ApprovalQueueConfig_2]] - `uses` [INFERRED]
- [[ApprovalStore_1]] - `uses` [INFERRED]
- [[EdgeApprovals]] - `uses` [INFERRED]
- [[EdgePrincipal_1]] - `uses` [INFERRED]
- [[EnhancedApprovalQueue]] - `uses` [INFERRED]
- [[MFAGuard_2]] - `uses` [INFERRED]
- [[TelegramAPIProxy]] - `uses` [INFERRED]
- [[ToolRiskConfig_1]] - `uses` [INFERRED]
- [[test_edge_approvals.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Community_25