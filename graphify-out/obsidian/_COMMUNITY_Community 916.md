---
type: community
members: 10
---

# Community 916

**Members:** 10 nodes

## Members
- [[.store()]] - code - gateway/tests/test_audit_export.py
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
TABLE source_file, type FROM #community/Community_916
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_Community 89]]
- 3 edges to [[_COMMUNITY_Community 232]]
- 1 edge to [[_COMMUNITY_Community 9]]

## Top bridge nodes
- [[TestAuditStoreBotId]] - degree 13, connects to 3 communities
- [[.test_migration_adds_bot_id_column()]] - degree 3, connects to 1 community
- [[.store()]] - degree 2, connects to 1 community