---
type: community
cohesion: 0.09
members: 25
---

# AlertDispatcher (5)

**Cohesion:** 0.09 - loosely connected
**Members:** 25 nodes

## Members
- [[dot-__init__()_139]] - code - gateway/security/audit_store.py
- [[dot-close()_11]] - code - gateway/security/audit_store.py
- [[dot-get_recent_entries()_1]] - code - gateway/security/audit_store.py
- [[dot-get_stats()_13]] - code - gateway/security/audit_store.py
- [[dot-initialize()_2]] - code - gateway/security/audit_store.py
- [[dot-query_events()]] - code - gateway/security/audit_store.py
- [[dot-store()_1]] - code - gateway/tests/test_audit_export.py
- [[dot-test_event_to_dict_includes_bot_id()]] - code - gateway/tests/test_audit_export.py
- [[dot-test_log_event_default_bot_id_is_openclaw()]] - code - gateway/tests/test_audit_export.py
- [[dot-test_log_event_stores_bot_id()]] - code - gateway/tests/test_audit_export.py
- [[dot-test_migration_adds_bot_id_column()]] - code - gateway/tests/test_audit_export.py
- [[dot-test_query_events_bot_filter()]] - code - gateway/tests/test_audit_export.py
- [[dot-test_query_events_bot_filter_combined_with_severity()]] - code - gateway/tests/test_audit_export.py
- [[AuditStore]] - code - gateway/security/audit_store.py
- [[Close the database connection._1]] - rationale - gateway/security/audit_store.py
- [[Get audit store statistics.]] - rationale - gateway/security/audit_store.py
- [[Open the database, create the schema, and run column migrations.          Initia]] - rationale - gateway/security/audit_store.py
- [[Opening a pre-migration DB (no bot_id column) should auto-migrate.]] - rationale - gateway/tests/test_audit_export.py
- [[Path_37]] - code - gateway/security/audit_store.py
- [[Query audit events with optional filters.          Args             bot_id Whe]] - rationale - gateway/security/audit_store.py
- [[Return the most recent audit entries (alias for query_events with limit).]] - rationale - gateway/security/audit_store.py
- [[SQLite-backed audit event store with tamper-evident hash chain.]] - rationale - gateway/security/audit_store.py
- [[TestAuditStoreBotId]] - code - gateway/tests/test_audit_export.py
- [[Verify per-bot filtering in AuditStore (v1.1.0 multi-bot support).]] - rationale - gateway/tests/test_audit_export.py
- [[test_audit_export.py]] - code - gateway/tests/test_audit_export.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/AlertDispatcher_5
SORT file.name ASC
```

## Connections to other communities
- 11 edges to [[_COMMUNITY_EnhancedApprovalQueue (`enhanced_queue.py`)]]
- 8 edges to [[_COMMUNITY_AuditExporter (2)]]
- 4 edges to [[_COMMUNITY_ApprovalStore]]
- 4 edges to [[_COMMUNITY_AuditExportConfig]]
- 3 edges to [[_COMMUNITY_The 8D Investigation Process]]
- 2 edges to [[_COMMUNITY_Any]]
- 1 edge to [[_COMMUNITY_archive_old_events]]

## Top bridge nodes
- [[AuditStore]] - degree 34, connects to 7 communities
- [[test_audit_export.py]] - degree 8, connects to 4 communities
- [[TestAuditStoreBotId]] - degree 13, connects to 3 communities
- [[dot-query_events()]] - degree 4, connects to 1 community
