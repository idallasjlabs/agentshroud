---
source_file: "gateway/approval_queue/queue.py"
type: "code"
community: "ingest_api/config.py"
location: "L31"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/ingest_api/configpy
---

# ApprovalQueue

## Connections
- [[dot-__init__()_92]] - `method` [EXTRACTED]
- [[dot-_append_audit_event()]] - `method` [EXTRACTED]
- [[dot-_expire_stale()]] - `method` [EXTRACTED]
- [[dot-_load_pending_store()]] - `method` [EXTRACTED]
- [[dot-_persist_pending_store()]] - `method` [EXTRACTED]
- [[dot-broadcast()_1]] - `method` [EXTRACTED]
- [[dot-cleanup_decided()]] - `method` [EXTRACTED]
- [[dot-connect()]] - `method` [EXTRACTED]
- [[dot-decide()_1]] - `method` [EXTRACTED]
- [[dot-disabled_client()]] - `calls` [EXTRACTED]
- [[dot-disconnect()]] - `method` [EXTRACTED]
- [[dot-get_item()_2]] - `method` [EXTRACTED]
- [[dot-get_pending()_2]] - `method` [EXTRACTED]
- [[dot-no_approval_client()]] - `calls` [EXTRACTED]
- [[dot-submit()_1]] - `method` [EXTRACTED]
- [[ApprovalQueueConfig]] - `uses` [INFERRED]
- [[ApprovalQueueItem]] - `uses` [INFERRED]
- [[ApprovalRequest]] - `uses` [INFERRED]
- [[In-memory approval queue with WebSocket notifications Actions requiring…]] - `rationale_for` [EXTRACTED]
- [[MFAGuard]] - `uses` [INFERRED]
- [[TestSSHDisabledEndpoint]] - `uses` [INFERRED]
- [[TestSSHRequireApprovalFalse]] - `uses` [INFERRED]
- [[_queue()]] - `calls` [EXTRACTED]
- [[_submit_high_risk()]] - `uses` [INFERRED]
- [[approval_queue()]] - `uses` [INFERRED]
- [[approval_queue()_1]] - `uses` [INFERRED]
- [[client()_14]] - `uses` [INFERRED]
- [[client()_15]] - `uses` [INFERRED]
- [[queue()]] - `uses` [INFERRED]
- [[queue.py]] - `contains` [EXTRACTED]
- [[run()]] - `calls` [INFERRED]
- [[test_approval_queue.py]] - `imports` [EXTRACTED]
- [[test_approval_stress.py]] - `imports` [EXTRACTED]
- [[test_cleanup_decided_persists_removal_to_disk()]] - `uses` [INFERRED]
- [[test_mfa_guard.py]] - `imports` [EXTRACTED]
- [[test_persist_pending_store_writes_atomically()]] - `uses` [INFERRED]
- [[test_security_integration.py]] - `imports` [EXTRACTED]
- [[test_ssh_endpoints.py]] - `imports` [EXTRACTED]
- [[test_ssh_write_file_endpoint.py]] - `imports` [EXTRACTED]
- [[test_store_persists_submit_and_decision()]] - `uses` [INFERRED]
- [[test_store_restores_items_on_init()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/ingest_api/configpy
