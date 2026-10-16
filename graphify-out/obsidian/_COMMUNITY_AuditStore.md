---
type: community
cohesion: 0.08
members: 30
---

# AuditStore

**Cohesion:** 0.08 - loosely connected
**Members:** 30 nodes

## Members
- [[dot-__init__()_101]] - code - gateway/security/audit_store.py
- [[dot-audit_store()]] - code - gateway/tests/test_audit_export.py
- [[dot-audit_store()_1]] - code - gateway/tests/test_audit_export.py
- [[dot-close()_8]] - code - gateway/security/audit_store.py
- [[dot-get_recent_entries()_1]] - code - gateway/security/audit_store.py
- [[dot-get_stats()_11]] - code - gateway/security/audit_store.py
- [[dot-initialize()_1]] - code - gateway/security/audit_store.py
- [[dot-query_events()]] - code - gateway/security/audit_store.py
- [[dot-store()_2]] - code - gateway/tests/test_audit_export.py
- [[dot-test_event_to_dict_includes_bot_id()]] - code - gateway/tests/test_audit_export.py
- [[dot-test_log_event_default_bot_id_is_openclaw()]] - code - gateway/tests/test_audit_export.py
- [[dot-test_log_event_stores_bot_id()]] - code - gateway/tests/test_audit_export.py
- [[dot-test_migration_adds_bot_id_column()]] - code - gateway/tests/test_audit_export.py
- [[dot-test_query_events_bot_filter()]] - code - gateway/tests/test_audit_export.py
- [[dot-test_query_events_bot_filter_combined_with_severity()]] - code - gateway/tests/test_audit_export.py
- [[AuditStore_1]] - code - gateway/security/audit_store.py
- [[Close the database connection.]] - rationale - gateway/security/audit_store.py
- [[Create audit store with test data.]] - rationale - gateway/tests/test_audit_export.py
- [[Create in-memory audit store for testing.]] - rationale - gateway/tests/test_audit_export.py
- [[Get audit store statistics.]] - rationale - gateway/security/audit_store.py
- [[Open the database, create the schema, and run column migrations.          Initia]] - rationale - gateway/security/audit_store.py
- [[Opening a pre-migration DB (no bot_id column) should auto-migrate.]] - rationale - gateway/tests/test_audit_export.py
- [[Path_28]] - code - gateway/security/audit_store.py
- [[Query audit events with optional filters.          Args             bot_id Whe]] - rationale - gateway/security/audit_store.py
- [[Return the most recent audit entries (alias for query_events with limit).]] - rationale - gateway/security/audit_store.py
- [[SQLite-backed audit event store with tamper-evident hash chain.]] - rationale - gateway/security/audit_store.py
- [[TestAuditStoreBotId]] - code - gateway/tests/test_audit_export.py
- [[Verify per-bot filtering in AuditStore (v1.1.0 multi-bot support).]] - rationale - gateway/tests/test_audit_export.py
- [[audit_export.py]] - code - gateway/security/audit_export.py
- [[audit_store.py]] - code - gateway/security/audit_store.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/AuditStore
SORT file.name ASC
```

## Connections to other communities
- 14 edges to [[_COMMUNITY_AuditExporter]]
- 8 edges to [[_COMMUNITY_AuditEvent]]
- 4 edges to [[_COMMUNITY_ApprovalQueueConfig]]
- 2 edges to [[_COMMUNITY_AgentRegistry]]
- 2 edges to [[_COMMUNITY_InjectionAction]]
- 2 edges to [[_COMMUNITY_MiddlewareManager]]
- 2 edges to [[_COMMUNITY_AuditEvent_1]]
- 1 edge to [[_COMMUNITY_All Dependencies_1]]
- 1 edge to [[_COMMUNITY_AgentShroud macOS App Icon (1024x1024, Rounded Squircle)]]
- 1 edge to [[_COMMUNITY_IEC 62443 Compliance Matrix — AgentShroud]]
- 1 edge to [[_COMMUNITY_archive_old_events]]

## Top bridge nodes
- [[AuditStore_1]] - degree 36, connects to 7 communities
- [[audit_store.py]] - degree 6, connects to 4 communities
- [[audit_export.py]] - degree 7, connects to 3 communities
- [[TestAuditStoreBotId]] - degree 13, connects to 2 communities
- [[dot-query_events()]] - degree 4, connects to 1 community
