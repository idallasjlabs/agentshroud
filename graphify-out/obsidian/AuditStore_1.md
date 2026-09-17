---
source_file: "gateway/security/audit_store.py"
type: "code"
community: "AuditStore"
location: "L122"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/AuditStore
---

# AuditStore

## Connections
- [[.__init__()_39]] - `method` [EXTRACTED]
- [[._get_latest_hash()]] - `method` [EXTRACTED]
- [[.audit_store()]] - `calls` [EXTRACTED]
- [[.audit_store()_1]] - `calls` [EXTRACTED]
- [[.close()_3]] - `method` [EXTRACTED]
- [[.get_recent_entries()]] - `method` [EXTRACTED]
- [[.get_stats()_4]] - `method` [EXTRACTED]
- [[.initialize()]] - `method` [EXTRACTED]
- [[.log_event()_2]] - `method` [EXTRACTED]
- [[.query_events()]] - `method` [EXTRACTED]
- [[.store()_2]] - `calls` [EXTRACTED]
- [[.test_migration_adds_bot_id_column()]] - `calls` [EXTRACTED]
- [[.verify_hash_chain()]] - `method` [EXTRACTED]
- [[ApprovalQueueItem_4]] - `uses` [INFERRED]
- [[AuditEvent_1]] - `uses` [INFERRED]
- [[AuditEvent]] - `calls` [EXTRACTED]
- [[AuditExportConfig]] - `uses` [INFERRED]
- [[AuditExporter]] - `uses` [INFERRED]
- [[AuditStore]] - `uses` [INFERRED]
- [[Path_36]] - `uses` [INFERRED]
- [[SQLite-backed audit event store with tamper-evident hash chain.]] - `rationale_for` [EXTRACTED]
- [[TestAuditEvent]] - `uses` [INFERRED]
- [[TestAuditExporter]] - `uses` [INFERRED]
- [[TestAuditStore]] - `uses` [INFERRED]
- [[TestAuditStoreBotId]] - `uses` [INFERRED]
- [[TextIO]] - `uses` [INFERRED]
- [[archive_old_events()]] - `references` [EXTRACTED]
- [[audit_export.py]] - `imports` [EXTRACTED]
- [[audit_store.py]] - `contains` [EXTRACTED]
- [[enforcement-audit-script.py]] - `imports` [EXTRACTED]
- [[lifespan()]] - `calls` [EXTRACTED]
- [[lifespan.py]] - `imports` [EXTRACTED]
- [[run()_4]] - `calls` [EXTRACTED]
- [[test_approval_store.py]] - `imports` [EXTRACTED]
- [[test_audit_export.py]] - `imports` [EXTRACTED]
- [[test_audit_store_initialize_is_idempotent()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/AuditStore