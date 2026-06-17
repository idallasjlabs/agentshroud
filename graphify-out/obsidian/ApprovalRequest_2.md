---
source_file: "gateway/ingest_api/models.py"
type: "code"
community: "Enhanced Approval Queue"
location: "L71"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Enhanced_Approval_Queue
---

# ApprovalRequest

## Connections
- [[.test_concurrent_submit_and_decide()]] - `calls` [EXTRACTED]
- [[.test_double_decide_raises()]] - `calls` [EXTRACTED]
- [[.test_expired_request_cannot_be_decided()]] - `calls` [EXTRACTED]
- [[.test_get_pending_expires_stale()]] - `calls` [EXTRACTED]
- [[.test_timeout_auto_deny()]] - `calls` [EXTRACTED]
- [[Any]] - `uses` [INFERRED]
- [[ApprovalQueueConfig]] - `uses` [INFERRED]
- [[ApprovalQueueItem]] - `uses` [INFERRED]
- [[ApprovalRequest]] - `uses` [INFERRED]
- [[ApprovalStore]] - `uses` [INFERRED]
- [[AuthRequired]] - `uses` [INFERRED]
- [[BaseModel]] - `inherits` [EXTRACTED]
- [[EnhancedApprovalQueue]] - `uses` [INFERRED]
- [[Exception]] - `uses` [INFERRED]
- [[MCPProxyRequest]] - `uses` [INFERRED]
- [[MCPResultRequest]] - `uses` [INFERRED]
- [[OpProxyRequest]] - `uses` [INFERRED]
- [[Request]] - `uses` [INFERRED]
- [[Request for human approval of a sensitive action      Submitted by an agent when]] - `rationale_for` [EXTRACTED]
- [[SSHExecRequest]] - `uses` [INFERRED]
- [[TestApprovalStorePersistence]] - `uses` [INFERRED]
- [[TestApprovalTimeout]] - `uses` [INFERRED]
- [[TestApprovalWorkflow]] - `uses` [INFERRED]
- [[TestAutoExpire]] - `uses` [INFERRED]
- [[TestConcurrentApprovalRequests]] - `uses` [INFERRED]
- [[TestMCPProxyIntegration]] - `uses` [INFERRED]
- [[TestPersistence]] - `uses` [INFERRED]
- [[TestToolRiskClassification]] - `uses` [INFERRED]
- [[ToolRiskConfig]] - `uses` [INFERRED]
- [[ToolRiskPolicy]] - `uses` [INFERRED]
- [[WebSocket]] - `uses` [INFERRED]
- [[WebSocket_2]] - `uses` [INFERRED]
- [[approval.py]] - `imports` [EXTRACTED]
- [[email_send()]] - `calls` [EXTRACTED]
- [[enhanced_queue.py]] - `imports` [EXTRACTED]
- [[forward.py]] - `imports` [EXTRACTED]
- [[main.py_2]] - `imports` [EXTRACTED]
- [[mcp_proxy_endpoint()]] - `calls` [EXTRACTED]
- [[models.py]] - `contains` [EXTRACTED]
- [[queue.py]] - `imports` [EXTRACTED]
- [[ssh_exec()]] - `calls` [EXTRACTED]
- [[test_approval_queue.py]] - `imports` [EXTRACTED]
- [[test_approval_request_valid()]] - `calls` [EXTRACTED]
- [[test_approval_stress.py]] - `imports` [EXTRACTED]
- [[test_cleanup_decided_keeps_pending_items()]] - `calls` [EXTRACTED]
- [[test_cleanup_decided_keeps_recent_decided_items()]] - `calls` [EXTRACTED]
- [[test_cleanup_decided_removes_old_decided_items()]] - `calls` [EXTRACTED]
- [[test_concurrent_decisions()]] - `calls` [EXTRACTED]
- [[test_decide_already_decided()]] - `calls` [EXTRACTED]
- [[test_decide_approval_approve()]] - `calls` [EXTRACTED]
- [[test_decide_approval_reject()]] - `calls` [EXTRACTED]
- [[test_decide_expired_request()]] - `calls` [EXTRACTED]
- [[test_enhanced_approval.py]] - `imports` [EXTRACTED]
- [[test_get_item()]] - `calls` [EXTRACTED]
- [[test_get_pending()]] - `calls` [EXTRACTED]
- [[test_get_pending_excludes_decided()]] - `calls` [EXTRACTED]
- [[test_main_simple.py]] - `imports` [EXTRACTED]
- [[test_request_expiration()]] - `calls` [EXTRACTED]
- [[test_store_persists_submit_and_decision()]] - `calls` [EXTRACTED]
- [[test_submit_approval_request()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Enhanced_Approval_Queue