---
source_file: "gateway/ingest_api/models.py"
type: "code"
community: "ApprovalStore"
location: "L181"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/ApprovalStore
---

# ApprovalQueueItem

## Connections
- [[dot-_notify_telegram()]] - `references` [EXTRACTED]
- [[dot-decide()]] - `references` [EXTRACTED]
- [[dot-decide()_1]] - `references` [EXTRACTED]
- [[dot-get_item()_1]] - `references` [EXTRACTED]
- [[dot-get_item()_2]] - `references` [EXTRACTED]
- [[dot-get_pending()_1]] - `references` [EXTRACTED]
- [[dot-get_pending()_2]] - `references` [EXTRACTED]
- [[dot-load_all()]] - `references` [EXTRACTED]
- [[dot-load_pending()]] - `references` [EXTRACTED]
- [[dot-save()_1]] - `references` [EXTRACTED]
- [[dot-submit()]] - `references` [EXTRACTED]
- [[dot-submit()_1]] - `references` [EXTRACTED]
- [[dot-test_store_expires_old_items()]] - `calls` [EXTRACTED]
- [[dot-test_store_persists_across_reopen()]] - `calls` [EXTRACTED]
- [[dot-test_store_save_and_load()]] - `calls` [EXTRACTED]
- [[dot-test_store_update_status()]] - `calls` [EXTRACTED]
- [[A pending approval request in the queue]] - `rationale_for` [EXTRACTED]
- [[ApprovalQueue]] - `uses` [INFERRED]
- [[ApprovalStore]] - `uses` [INFERRED]
- [[BaseModel_3]] - `inherits` [EXTRACTED]
- [[EnhancedApprovalQueue]] - `uses` [INFERRED]
- [[TestApprovalStorePersistence]] - `uses` [INFERRED]
- [[_make_item()]] - `calls` [EXTRACTED]
- [[_pending_item()]] - `calls` [EXTRACTED]
- [[approval.py]] - `imports` [EXTRACTED]
- [[approval_queuestore.py]] - `imports` [EXTRACTED]
- [[enhanced_queue.py]] - `imports` [EXTRACTED]
- [[ingest_apimodels.py]] - `contains` [EXTRACTED]
- [[queue.py]] - `imports` [EXTRACTED]
- [[test_approval_store.py]] - `imports` [EXTRACTED]
- [[test_approval_stress.py]] - `imports` [EXTRACTED]
- [[test_soc_router_coverage.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/ApprovalStore
