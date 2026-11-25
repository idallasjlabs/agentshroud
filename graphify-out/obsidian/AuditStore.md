---
source_file: "gateway/security/audit_store.py"
type: "code"
community: "AuditStore"
location: "L123"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/AuditStore
---

# AuditStore

## Connections
- [[dot-__init__()_182]] - `references` [EXTRACTED]
- [[dot-__init__()_177]] - `method` [EXTRACTED]
- [[dot-_get_latest_hash()]] - `method` [EXTRACTED]
- [[dot-audit_store()]] - `calls` [EXTRACTED]
- [[dot-audit_store()_1]] - `calls` [EXTRACTED]
- [[dot-close()_14]] - `method` [EXTRACTED]
- [[dot-get_recent_entries()_1]] - `method` [EXTRACTED]
- [[dot-get_stats()_14]] - `method` [EXTRACTED]
- [[dot-initialize()_3]] - `method` [EXTRACTED]
- [[dot-log_event()_1]] - `method` [EXTRACTED]
- [[dot-query_events()]] - `method` [EXTRACTED]
- [[dot-store()_1]] - `calls` [EXTRACTED]
- [[dot-store()_2]] - `calls` [EXTRACTED]
- [[dot-test_concurrent_log_event_single_store_keeps_linear_chain()]] - `calls` [EXTRACTED]
- [[dot-test_concurrent_log_event_two_connections_keeps_linear_chain()]] - `calls` [EXTRACTED]
- [[dot-test_migration_adds_bot_id_column()]] - `calls` [EXTRACTED]
- [[dot-verify_hash_chain()]] - `method` [EXTRACTED]
- [[AuditExporter]] - `uses` [INFERRED]
- [[SQLite-backed audit event store with tamper-evident hash chain.]] - `rationale_for` [EXTRACTED]
- [[TestAuditExporter]] - `uses` [INFERRED]
- [[TestAuditStore]] - `uses` [INFERRED]
- [[TestAuditStoreAnchoredVerify]] - `uses` [INFERRED]
- [[TestAuditStoreBotId]] - `uses` [INFERRED]
- [[TestAuditStoreConcurrentAppend]] - `uses` [INFERRED]
- [[audit_export.py]] - `imports` [EXTRACTED]
- [[audit_store.py]] - `contains` [EXTRACTED]
- [[edge()]] - `uses` [INFERRED]
- [[enforcement-audit-script.py]] - `imports` [EXTRACTED]
- [[lifespan()]] - `uses` [INFERRED]
- [[lifespan.py]] - `imports` [EXTRACTED]
- [[run()]] - `calls` [EXTRACTED]
- [[stack()]] - `uses` [INFERRED]
- [[test_approval_store.py]] - `imports` [EXTRACTED]
- [[test_audit_export.py]] - `imports` [EXTRACTED]
- [[test_audit_store_initialize_is_idempotent()]] - `uses` [INFERRED]
- [[test_edge_e2e_sdk.py]] - `imports` [EXTRACTED]
- [[test_edge_pipeline.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/AuditStore
