---
source_file: "gateway/tests/test_approval_store.py"
type: "code"
community: "ApprovalRequest"
location: "L38"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/ApprovalRequest
---

# Path

## Connections
- [[ApprovalQueueItem_2]] - `uses` [INFERRED]
- [[ApprovalStore]] - `uses` [INFERRED]
- [[AuditStore_1]] - `uses` [INFERRED]
- [[store()_1]] - `references` [EXTRACTED]
- [[test_audit_store_initialize_is_idempotent()]] - `references` [EXTRACTED]
- [[test_decide_persists()]] - `references` [EXTRACTED]
- [[test_expired_items_on_reload()]] - `references` [EXTRACTED]
- [[test_initialize_is_idempotent()_1]] - `references` [EXTRACTED]
- [[test_persist_and_reload()]] - `references` [EXTRACTED]
- [[test_store_survives_restart()]] - `references` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/ApprovalRequest