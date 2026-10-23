---
source_file: "gateway/security/audit_store.py"
type: "code"
community: "AlertDispatcher (5)"
location: "L122"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/AlertDispatcher_5
---

# AuditStore

## Connections
- [[dot-__init__()_139]] - `method` [EXTRACTED]
- [[dot-_get_latest_hash()]] - `method` [EXTRACTED]
- [[dot-audit_store()]] - `calls` [EXTRACTED]
- [[dot-audit_store()_1]] - `calls` [EXTRACTED]
- [[dot-close()_11]] - `method` [EXTRACTED]
- [[dot-get_recent_entries()_1]] - `method` [EXTRACTED]
- [[dot-get_stats()_13]] - `method` [EXTRACTED]
- [[dot-initialize()_2]] - `method` [EXTRACTED]
- [[dot-log_event()_2]] - `method` [EXTRACTED]
- [[dot-query_events()]] - `method` [EXTRACTED]
- [[dot-store()_1]] - `calls` [EXTRACTED]
- [[dot-test_migration_adds_bot_id_column()]] - `calls` [EXTRACTED]
- [[dot-verify_hash_chain()]] - `method` [EXTRACTED]
- [[ApprovalQueueItem_1]] - `uses` [INFERRED]
- [[AuditEvent]] - `uses` [INFERRED]
- [[AuditEvent_1]] - `calls` [EXTRACTED]
- [[AuditExportConfig_1]] - `uses` [INFERRED]
- [[AuditExporter]] - `uses` [INFERRED]
- [[AuditStore_1]] - `uses` [INFERRED]
- [[Path_24]] - `uses` [INFERRED]
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
- [[run()_5]] - `calls` [EXTRACTED]
- [[test_approval_store.py]] - `imports` [EXTRACTED]
- [[test_audit_export.py]] - `imports` [EXTRACTED]
- [[test_audit_store_initialize_is_idempotent()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/AlertDispatcher_5
