---
source_file: "gateway/approval_queue/queue.py"
type: "code"
community: "Approval Queue (WebSocket)"
location: "L31"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Approval_Queue_WebSocket
---

# ApprovalQueue

## Connections
- [[dot-__init__()_40]] - `method` [EXTRACTED]
- [[dot-_append_audit_event()]] - `method` [EXTRACTED]
- [[dot-_expire_stale()]] - `method` [EXTRACTED]
- [[dot-_load_pending_store()]] - `method` [EXTRACTED]
- [[dot-_persist_pending_store()]] - `method` [EXTRACTED]
- [[dot-broadcast()_1]] - `method` [EXTRACTED]
- [[dot-cleanup_decided()]] - `method` [EXTRACTED]
- [[dot-connect()_2]] - `method` [EXTRACTED]
- [[dot-decide()_1]] - `method` [EXTRACTED]
- [[dot-disabled_client()]] - `calls` [EXTRACTED]
- [[dot-disconnect()_1]] - `method` [EXTRACTED]
- [[dot-get_item()_2]] - `method` [EXTRACTED]
- [[dot-get_pending()_1]] - `method` [EXTRACTED]
- [[dot-no_approval_client()]] - `calls` [EXTRACTED]
- [[dot-submit()_1]] - `method` [EXTRACTED]
- [[ApprovalQueue]] - `uses` [INFERRED]
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
- [[_HangingWebSocket_1]] - `uses` [INFERRED]
- [[_queue()]] - `calls` [EXTRACTED]
- [[approval_queue()_1]] - `calls` [EXTRACTED]
- [[approval_queue()]] - `calls` [EXTRACTED]
- [[client()_19]] - `calls` [EXTRACTED]
- [[client()_20]] - `calls` [EXTRACTED]
- [[queue()]] - `calls` [EXTRACTED]
- [[queue.py]] - `contains` [EXTRACTED]
- [[test_approval_queue.py]] - `imports` [EXTRACTED]
- [[test_approval_stress.py]] - `imports` [EXTRACTED]
- [[test_cleanup_decided_persists_removal_to_disk()]] - `calls` [EXTRACTED]
- [[test_mfa_guard.py]] - `imports` [EXTRACTED]
- [[test_persist_pending_store_writes_atomically()]] - `calls` [EXTRACTED]
- [[test_security_integration.py]] - `imports` [EXTRACTED]
- [[test_ssh_endpoints.py]] - `imports` [EXTRACTED]
- [[test_ssh_write_file_endpoint.py]] - `imports` [EXTRACTED]
- [[test_store_persists_submit_and_decision()]] - `calls` [EXTRACTED]
- [[test_store_restores_items_on_init()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Approval_Queue_WebSocket