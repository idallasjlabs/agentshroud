---
type: community
cohesion: 0.08
members: 30
---

# Community 258

**Cohesion:** 0.08 - loosely connected
**Members:** 30 nodes

## Members
- [[.__init__()_58]] - code - gateway/security/audit_store.py
- [[.audit_store()_1]] - code - gateway/tests/test_audit_export.py
- [[.audit_store()]] - code - gateway/tests/test_audit_export.py
- [[.close()_9]] - code - gateway/security/audit_store.py
- [[.get_recent_entries()]] - code - gateway/security/audit_store.py
- [[.get_stats()_14]] - code - gateway/security/audit_store.py
- [[.initialize()_3]] - code - gateway/security/audit_store.py
- [[.query_events()]] - code - gateway/security/audit_store.py
- [[.store()]] - code - gateway/tests/test_audit_export.py
- [[.test_event_to_dict_includes_bot_id()]] - code - gateway/tests/test_audit_export.py
- [[.test_log_event_default_bot_id_is_openclaw()]] - code - gateway/tests/test_audit_export.py
- [[.test_log_event_stores_bot_id()]] - code - gateway/tests/test_audit_export.py
- [[.test_migration_adds_bot_id_column()]] - code - gateway/tests/test_audit_export.py
- [[.test_query_events_bot_filter()]] - code - gateway/tests/test_audit_export.py
- [[.test_query_events_bot_filter_combined_with_severity()]] - code - gateway/tests/test_audit_export.py
- [[AuditStore_1]] - code - gateway/security/audit_store.py
- [[Close the database connection._1]] - rationale - gateway/security/audit_store.py
- [[Create audit store with test data.]] - rationale - gateway/tests/test_audit_export.py
- [[Create in-memory audit store for testing.]] - rationale - gateway/tests/test_audit_export.py
- [[Get audit store statistics.]] - rationale - gateway/security/audit_store.py
- [[Open the database, create the schema, and run column migrations.          Initia]] - rationale - gateway/security/audit_store.py
- [[Opening a pre-migration DB (no bot_id column) should auto-migrate.]] - rationale - gateway/tests/test_audit_export.py
- [[Path_7]] - code - gateway/security/audit_store.py
- [[Query audit events with optional filters.          Args             bot_id Whe]] - rationale - gateway/security/audit_store.py
- [[Return the most recent audit entries (alias for query_events with limit).]] - rationale - gateway/security/audit_store.py
- [[SQLite-backed audit event store with tamper-evident hash chain.]] - rationale - gateway/security/audit_store.py
- [[TestAuditStoreBotId]] - code - gateway/tests/test_audit_export.py
- [[Verify per-bot filtering in AuditStore (v1.1.0 multi-bot support).]] - rationale - gateway/tests/test_audit_export.py
- [[audit_export.py]] - code - gateway/security/audit_export.py
- [[audit_store.py]] - code - gateway/security/audit_store.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_258
SORT file.name ASC
```

## Connections to other communities
- 10 edges to [[_COMMUNITY_Community 208]]
- 9 edges to [[_COMMUNITY_Community 342]]
- 4 edges to [[_COMMUNITY_Memory Lifecycle & Egress Filtering]]
- 4 edges to [[_COMMUNITY_Community 125]]
- 3 edges to [[_COMMUNITY_RBAC & SOC Realtime]]
- 2 edges to [[_COMMUNITY_Community 46]]
- 2 edges to [[_COMMUNITY_Community 831]]
- 1 edge to [[_COMMUNITY_Community 359]]
- 1 edge to [[_COMMUNITY_Community 289]]
- 1 edge to [[_COMMUNITY_Community 137]]
- 1 edge to [[_COMMUNITY_Community 519]]

## Top bridge nodes
- [[AuditStore_1]] - degree 36, connects to 7 communities
- [[audit_export.py]] - degree 7, connects to 4 communities
- [[audit_store.py]] - degree 6, connects to 4 communities
- [[TestAuditStoreBotId]] - degree 13, connects to 3 communities
- [[.query_events()]] - degree 4, connects to 1 community