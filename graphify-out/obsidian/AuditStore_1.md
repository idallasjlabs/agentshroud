---
source_file: "gateway/security/audit_store.py"
type: "code"
community: "Community 254"
location: "L123"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Community_254
---

# AuditStore

## Connections
- [[.__init__()_73]] - `method` [EXTRACTED]
- [[._get_latest_hash()]] - `method` [EXTRACTED]
- [[.audit_store()_1]] - `calls` [EXTRACTED]
- [[.audit_store()]] - `calls` [EXTRACTED]
- [[.close()_11]] - `method` [EXTRACTED]
- [[.get_recent_entries()]] - `method` [EXTRACTED]
- [[.get_stats()_14]] - `method` [EXTRACTED]
- [[.initialize()_3]] - `method` [EXTRACTED]
- [[.log_event()]] - `method` [EXTRACTED]
- [[.query_events()]] - `method` [EXTRACTED]
- [[.store()_1]] - `calls` [EXTRACTED]
- [[.store()]] - `calls` [EXTRACTED]
- [[.test_concurrent_log_event_single_store_keeps_linear_chain()]] - `calls` [EXTRACTED]
- [[.test_concurrent_log_event_two_connections_keeps_linear_chain()]] - `calls` [EXTRACTED]
- [[.test_migration_adds_bot_id_column()]] - `calls` [EXTRACTED]
- [[.verify_hash_chain()]] - `method` [EXTRACTED]
- [[ApprovalQueueItem_4]] - `uses` [INFERRED]
- [[AuditEvent]] - `uses` [INFERRED]
- [[AuditEvent_1]] - `calls` [EXTRACTED]
- [[AuditExportConfig_1]] - `uses` [INFERRED]
- [[AuditExporter]] - `uses` [INFERRED]
- [[AuditStore]] - `uses` [INFERRED]
- [[Clock_1]] - `uses` [INFERRED]
- [[Facade_1]] - `uses` [INFERRED]
- [[FakeFacade]] - `uses` [INFERRED]
- [[MemoryTokenStorage]] - `uses` [INFERRED]
- [[Path_26]] - `uses` [INFERRED]
- [[SQLite-backed audit event store with tamper-evident hash chain.]] - `rationale_for` [EXTRACTED]
- [[TestAuditEvent]] - `uses` [INFERRED]
- [[TestAuditExporter]] - `uses` [INFERRED]
- [[TestAuditRecord]] - `uses` [INFERRED]
- [[TestAuditStore]] - `uses` [INFERRED]
- [[TestAuditStoreAnchoredVerify]] - `uses` [INFERRED]
- [[TestAuditStoreBotId]] - `uses` [INFERRED]
- [[TestAuditStoreConcurrentAppend]] - `uses` [INFERRED]
- [[TestCommandCenterStats]] - `uses` [INFERRED]
- [[TestMonitorMode]] - `uses` [INFERRED]
- [[TestT1ToolAbuse]] - `uses` [INFERRED]
- [[TestT2Exfiltration]] - `uses` [INFERRED]
- [[TestT3Writes]] - `uses` [INFERRED]
- [[TestT4AuthN]] - `uses` [INFERRED]
- [[TestT9Abuse]] - `uses` [INFERRED]
- [[TestToolListing]] - `uses` [INFERRED]
- [[TextIO]] - `uses` [INFERRED]
- [[archive_old_events()]] - `references` [EXTRACTED]
- [[audit_export.py]] - `imports` [EXTRACTED]
- [[audit_store.py]] - `contains` [EXTRACTED]
- [[edge()_1]] - `calls` [EXTRACTED]
- [[enforcement-audit-script.py]] - `imports` [EXTRACTED]
- [[lifespan()_1]] - `calls` [EXTRACTED]
- [[lifespan.py]] - `imports` [EXTRACTED]
- [[run()_3]] - `calls` [EXTRACTED]
- [[stack()]] - `calls` [EXTRACTED]
- [[test_approval_store.py]] - `imports` [EXTRACTED]
- [[test_audit_export.py]] - `imports` [EXTRACTED]
- [[test_audit_store_initialize_is_idempotent()]] - `calls` [EXTRACTED]
- [[test_edge_e2e_sdk.py]] - `imports` [EXTRACTED]
- [[test_edge_pipeline.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Community_254