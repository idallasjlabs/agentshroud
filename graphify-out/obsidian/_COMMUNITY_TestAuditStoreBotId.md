---
type: community
cohesion: 0.20
members: 10
---

# TestAuditStoreBotId

**Cohesion:** 0.20 - loosely connected
**Members:** 10 nodes

## Members
- [[.store()_2]] - code - gateway/tests/test_audit_export.py
- [[.test_event_to_dict_includes_bot_id()]] - code - gateway/tests/test_audit_export.py
- [[.test_log_event_default_bot_id_is_openclaw()]] - code - gateway/tests/test_audit_export.py
- [[.test_log_event_stores_bot_id()]] - code - gateway/tests/test_audit_export.py
- [[.test_migration_adds_bot_id_column()]] - code - gateway/tests/test_audit_export.py
- [[.test_query_events_bot_filter()]] - code - gateway/tests/test_audit_export.py
- [[.test_query_events_bot_filter_combined_with_severity()]] - code - gateway/tests/test_audit_export.py
- [[Opening a pre-migration DB (no bot_id column) should auto-migrate.]] - rationale - gateway/tests/test_audit_export.py
- [[TestAuditStoreBotId]] - code - gateway/tests/test_audit_export.py
- [[Verify per-bot filtering in AuditStore (v1.1.0 multi-bot support).]] - rationale - gateway/tests/test_audit_export.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestAuditStoreBotId
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_AuditStore]]
- 2 edges to [[_COMMUNITY_AuditExporter]]
- 1 edge to [[_COMMUNITY_AuditExportConfig]]

## Top bridge nodes
- [[TestAuditStoreBotId]] - degree 13, connects to 3 communities
- [[.test_migration_adds_bot_id_column()]] - degree 3, connects to 1 community
- [[.store()_2]] - degree 2, connects to 1 community