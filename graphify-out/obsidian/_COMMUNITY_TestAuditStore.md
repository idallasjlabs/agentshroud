---
type: community
members: 10
---

# TestAuditStore

**Members:** 10 nodes

## Members
- [[dot-test_hash_chain_integrity()]] - code - gateway/tests/test_audit_export.py
- [[dot-test_log_event()]] - code - gateway/tests/test_audit_export.py
- [[dot-test_query_events()]] - code - gateway/tests/test_audit_export.py
- [[dot-test_stats()_2]] - code - gateway/tests/test_audit_export.py
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
- 4 edges to [[_COMMUNITY_asyncio_6]]
- 2 edges to [[_COMMUNITY_AuditStore]]
- 1 edge to [[_COMMUNITY_AuditEvent]]

## Top bridge nodes
- [[TestAuditStore]] - degree 8, connects to 2 communities
- [[dot-test_hash_chain_integrity()]] - degree 3, connects to 1 community
- [[dot-test_log_event()]] - degree 3, connects to 1 community
- [[dot-test_query_events()]] - degree 3, connects to 1 community
- [[dot-test_stats()_2]] - degree 3, connects to 1 community
