---
type: community
cohesion: 0.17
members: 12
---

# The 8D Investigation Process

**Cohesion:** 0.17 - loosely connected
**Members:** 12 nodes

## Members
- [[dot-audit_store()_1]] - code - gateway/tests/test_audit_export.py
- [[dot-test_hash_chain_integrity()]] - code - gateway/tests/test_audit_export.py
- [[dot-test_log_event()]] - code - gateway/tests/test_audit_export.py
- [[dot-test_query_events()]] - code - gateway/tests/test_audit_export.py
- [[dot-test_stats()_1]] - code - gateway/tests/test_audit_export.py
- [[Create in-memory audit store for testing.]] - rationale - gateway/tests/test_audit_export.py
- [[Test AuditStore functionality.]] - rationale - gateway/tests/test_audit_export.py
- [[Test audit store statistics.]] - rationale - gateway/tests/test_audit_export.py
- [[Test hash chain maintains integrity.]] - rationale - gateway/tests/test_audit_export.py
- [[Test logging audit events.]] - rationale - gateway/tests/test_audit_export.py
- [[Test querying events with filters.]] - rationale - gateway/tests/test_audit_export.py
- [[TestAuditStore]] - code - gateway/tests/test_audit_export.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/The_8D_Investigation_Process
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_AlertDispatcher (5)]]
- 2 edges to [[_COMMUNITY_AuditExporter (2)]]
- 1 edge to [[_COMMUNITY_EnhancedApprovalQueue (`enhanced_queue.py`)]]
- 1 edge to [[_COMMUNITY_AuditExportConfig]]

## Top bridge nodes
- [[TestAuditStore]] - degree 12, connects to 4 communities
- [[dot-audit_store()_1]] - degree 3, connects to 1 community
