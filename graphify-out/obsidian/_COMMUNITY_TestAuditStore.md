---
type: community
cohesion: 0.17
members: 12
---

# TestAuditStore

**Cohesion:** 0.17 - loosely connected
**Members:** 12 nodes

## Members
- [[.audit_store()_1]] - code - gateway/tests/test_audit_export.py
- [[.test_hash_chain_integrity()]] - code - gateway/tests/test_audit_export.py
- [[.test_log_event()]] - code - gateway/tests/test_audit_export.py
- [[.test_query_events()]] - code - gateway/tests/test_audit_export.py
- [[.test_stats()]] - code - gateway/tests/test_audit_export.py
- [[Create in-memory audit store for testing.]] - rationale - gateway/tests/test_audit_export.py
- [[Test AuditStore functionality.]] - rationale - gateway/tests/test_audit_export.py
- [[Test audit store statistics.]] - rationale - gateway/tests/test_audit_export.py
- [[Test hash chain maintains integrity.]] - rationale - gateway/tests/test_audit_export.py
- [[Test logging audit events.]] - rationale - gateway/tests/test_audit_export.py
- [[Test querying events with filters.]] - rationale - gateway/tests/test_audit_export.py
- [[TestAuditStore]] - code - gateway/tests/test_audit_export.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestAuditStore
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_AuditExporter]]
- 3 edges to [[_COMMUNITY_AuditStore]]
- 1 edge to [[_COMMUNITY_AuditExportConfig]]

## Top bridge nodes
- [[TestAuditStore]] - degree 12, connects to 3 communities
- [[.audit_store()_1]] - degree 3, connects to 1 community