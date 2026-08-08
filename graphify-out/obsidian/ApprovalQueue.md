---
source_file: "gateway/approval_queue/queue.py"
type: "code"
community: "Approval Queue Tests"
location: "L31"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Approval_Queue_Tests
---

# ApprovalQueue

## Connections
- [[.__init__()_9]] - `method` [EXTRACTED]
- [[._append_audit_event()]] - `method` [EXTRACTED]
- [[._expire_stale()]] - `method` [EXTRACTED]
- [[._load_pending_store()]] - `method` [EXTRACTED]
- [[._persist_pending_store()]] - `method` [EXTRACTED]
- [[.broadcast()_1]] - `method` [EXTRACTED]
- [[.cleanup_decided()]] - `method` [EXTRACTED]
- [[.connect()_1]] - `method` [EXTRACTED]
- [[.decide()_1]] - `method` [EXTRACTED]
- [[.disabled_client()]] - `calls` [EXTRACTED]
- [[.disconnect()_1]] - `method` [EXTRACTED]
- [[.get_item()_1]] - `method` [EXTRACTED]
- [[.get_pending()_1]] - `method` [EXTRACTED]
- [[.no_approval_client()]] - `calls` [EXTRACTED]
- [[.submit()_1]] - `method` [EXTRACTED]
- [[ApprovalQueue_1]] - `uses` [INFERRED]
- [[EnhancedApprovalQueue_2]] - `uses` [INFERRED]
- [[In-memory approval queue with WebSocket notifications      Actions requiring app]] - `rationale_for` [EXTRACTED]
- [[TestApprovalStorePersistence]] - `uses` [INFERRED]
- [[TestApprovalTimeout]] - `uses` [INFERRED]
- [[TestAutoExpire]] - `uses` [INFERRED]
- [[TestConcurrentApprovalRequests]] - `uses` [INFERRED]
- [[TestSSHDisabledEndpoint]] - `uses` [INFERRED]
- [[TestSSHExec]] - `uses` [INFERRED]
- [[TestSSHHistory]] - `uses` [INFERRED]
- [[TestSSHHosts]] - `uses` [INFERRED]
- [[TestSSHProxyValidateWriteFile]] - `uses` [INFERRED]
- [[TestSSHProxyWriteFileTransport]] - `uses` [INFERRED]
- [[TestSSHRequireApprovalFalse]] - `uses` [INFERRED]
- [[TestSSHValidateCwd]] - `uses` [INFERRED]
- [[TestSSHWriteFileEndpoint]] - `uses` [INFERRED]
- [[TestSSHWriteFileLedgerAudit]] - `uses` [INFERRED]
- [[TestSSHWriteFileShellMetacharacterContentRoundTrip]] - `uses` [INFERRED]
- [[_queue()]] - `calls` [EXTRACTED]
- [[approval_queue()]] - `calls` [EXTRACTED]
- [[approval_queue()_1]] - `calls` [EXTRACTED]
- [[client()_16]] - `calls` [EXTRACTED]
- [[client()_17]] - `calls` [EXTRACTED]
- [[queue()]] - `calls` [EXTRACTED]
- [[queue.py]] - `contains` [EXTRACTED]
- [[run()_3]] - `calls` [INFERRED]
- [[test_approval_queue.py]] - `implements` [EXTRACTED]
- [[test_approval_stress.py]] - `imports` [EXTRACTED]
- [[test_cleanup_decided_persists_removal_to_disk()]] - `calls` [EXTRACTED]
- [[test_mfa_guard.py]] - `imports` [EXTRACTED]
- [[test_persist_pending_store_writes_atomically()]] - `calls` [EXTRACTED]
- [[test_security_integration.py]] - `imports` [EXTRACTED]
- [[test_ssh_endpoints.py]] - `imports` [EXTRACTED]
- [[test_ssh_write_file_endpoint.py]] - `imports` [EXTRACTED]
- [[test_store_persists_submit_and_decision()]] - `calls` [EXTRACTED]
- [[test_store_restores_items_on_init()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Approval_Queue_Tests