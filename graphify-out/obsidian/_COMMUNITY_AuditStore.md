---
type: community
members: 27
---

# AuditStore

**Members:** 27 nodes

## Members
- [[dot-__init__()_174]] - code - gateway/security/audit_store.py
- [[dot-_get_latest_hash()]] - code - gateway/security/audit_store.py
- [[dot-audit_store()]] - code - gateway/tests/test_audit_export.py
- [[dot-audit_store()_1]] - code - gateway/tests/test_audit_export.py
- [[dot-close()_15]] - code - gateway/security/audit_store.py
- [[dot-get_recent_entries()_1]] - code - gateway/security/audit_store.py
- [[dot-get_stats()_13]] - code - gateway/security/audit_store.py
- [[dot-initialize()_3]] - code - gateway/security/audit_store.py
- [[dot-log_event()_1]] - code - gateway/security/audit_store.py
- [[dot-query_events()]] - code - gateway/security/audit_store.py
- [[dot-store()_2]] - code - gateway/tests/test_audit_export.py
- [[dot-store()_3]] - code - gateway/tests/test_audit_export.py
- [[dot-verify_hash_chain()]] - code - gateway/security/audit_store.py
- [[AuditStore]] - code - gateway/security/audit_store.py
- [[Close the database connection._1]] - rationale - gateway/security/audit_store.py
- [[Create audit store with test data.]] - rationale - gateway/tests/test_audit_export.py
- [[Create in-memory audit store for testing.]] - rationale - gateway/tests/test_audit_export.py
- [[Get audit store statistics.]] - rationale - gateway/security/audit_store.py
- [[Get the entry_hash of the most recent event for chain continuation.]] - rationale - gateway/security/audit_store.py
- [[Log a new audit event with hash chain integrity. Args bot_id Identifier of…]] - rationale - gateway/security/audit_store.py
- [[Open the database, create the schema, and run column migrations. Initialization…]] - rationale - gateway/security/audit_store.py
- [[Path_60]] - code
- [[Query audit events with optional filters. Args bot_id When set, restricts…]] - rationale - gateway/security/audit_store.py
- [[Return the most recent audit entries (alias for query_events with limit).]] - rationale - gateway/security/audit_store.py
- [[SQLite-backed audit event store with tamper-evident hash chain.]] - rationale - gateway/security/audit_store.py
- [[Verify the integrity of the hash chain. The first examined row's prev_hash must…]] - rationale - gateway/security/audit_store.py
- [[fixture_116]] - code

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/AuditStore
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_AuditEvent]]
- 5 edges to [[_COMMUNITY_asyncio_6]]
- 4 edges to [[_COMMUNITY_test_edge_e2e_sdk.py]]
- 3 edges to [[_COMMUNITY_dot-test_concurrent_log_event_two_connections_keeps_linear_chain]]
- 3 edges to [[_COMMUNITY_AuditExporter]]
- 2 edges to [[_COMMUNITY_TestAuditStore]]
- 2 edges to [[_COMMUNITY_run]]
- 2 edges to [[_COMMUNITY_test_mfa_guard.py]]
- 2 edges to [[_COMMUNITY_AuditExportConfig]]
- 1 edge to [[_COMMUNITY_lifespan.py]]
- 1 edge to [[_COMMUNITY_lifespan]]

## Top bridge nodes
- [[AuditStore]] - degree 37, connects to 11 communities
- [[fixture_116]] - degree 5, connects to 1 community
- [[dot-log_event()_1]] - degree 4, connects to 1 community
- [[dot-query_events()]] - degree 4, connects to 1 community
- [[dot-audit_store()]] - degree 4, connects to 1 community
