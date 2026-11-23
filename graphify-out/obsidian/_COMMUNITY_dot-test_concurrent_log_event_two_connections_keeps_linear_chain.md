---
type: community
members: 7
---

# .test_concurrent_log_event_two_connections_keeps_linear_chain

**Members:** 7 nodes

## Members
- [[dot-test_concurrent_log_event_single_store_keeps_linear_chain()]] - code - gateway/tests/test_audit_export.py
- [[dot-test_concurrent_log_event_two_connections_keeps_linear_chain()]] - code - gateway/tests/test_audit_export.py
- [[Concurrent log_event calls must not fork the SHA-256 chain (SCRUM-204).]] - rationale - gateway/tests/test_audit_export.py
- [[TestAuditStoreConcurrentAppend]] - code - gateway/tests/test_audit_export.py
- [[Two stores sharing one SQLite file (e.g. two workers) must not fork the chain.]] - rationale - gateway/tests/test_audit_export.py
- [[_assert_linear_chain()]] - code - gateway/tests/test_audit_export.py
- [[_chain_rows()]] - code - gateway/tests/test_audit_export.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_concurrent_log_event_two_connections_keeps_linear_chain
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_AuditEvent]]
- 3 edges to [[_COMMUNITY_AuditStore]]
- 2 edges to [[_COMMUNITY_asyncio_6]]

## Top bridge nodes
- [[dot-test_concurrent_log_event_two_connections_keeps_linear_chain()]] - degree 6, connects to 2 communities
- [[TestAuditStoreConcurrentAppend]] - degree 5, connects to 2 communities
- [[dot-test_concurrent_log_event_single_store_keeps_linear_chain()]] - degree 5, connects to 2 communities
- [[_assert_linear_chain()]] - degree 3, connects to 1 community
- [[_chain_rows()]] - degree 3, connects to 1 community
