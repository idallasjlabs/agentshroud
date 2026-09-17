---
type: community
cohesion: 0.10
members: 23
---

# Community 387

**Cohesion:** 0.10 - loosely connected
**Members:** 23 nodes

## Members
- [[dot-__init__()_140]] - code - gateway/security/audit_store.py
- [[dot-_generate_event_id()]] - code - gateway/security/audit_store.py
- [[dot-_get_latest_hash()]] - code - gateway/security/audit_store.py
- [[dot-compute_content_hash()]] - code - gateway/security/audit_store.py
- [[dot-compute_entry_hash()]] - code - gateway/security/audit_store.py
- [[dot-log_event()_2]] - code - gateway/security/audit_store.py
- [[dot-test_content_hash()]] - code - gateway/tests/test_audit_export.py
- [[dot-test_entry_hash_chain()]] - code - gateway/tests/test_audit_export.py
- [[dot-test_event_creation()]] - code - gateway/tests/test_audit_export.py
- [[dot-to_dict()_11]] - code - gateway/security/audit_store.py
- [[dot-verify_hash_chain()]] - code - gateway/security/audit_store.py
- [[AuditEvent]] - code - gateway/security/audit_store.py
- [[Compute SHA-256 hash of event content (excluding hashes).]] - rationale - gateway/security/audit_store.py
- [[Compute entry hash including previous hash (chain).]] - rationale - gateway/security/audit_store.py
- [[Convert to dictionary representation.]] - rationale - gateway/security/audit_store.py
- [[Generate a unique event ID based on timestamp + random.]] - rationale - gateway/security/audit_store.py
- [[Get the entry_hash of the most recent event for chain continuation.]] - rationale - gateway/security/audit_store.py
- [[Log a new audit event with hash chain integrity.          Args             bot_]] - rationale - gateway/security/audit_store.py
- [[Represents a single audit event.      The ``bot_id`` field identifies which bot]] - rationale - gateway/security/audit_store.py
- [[Test basic audit event creation.]] - rationale - gateway/tests/test_audit_export.py
- [[Test content hash computation.]] - rationale - gateway/tests/test_audit_export.py
- [[Test hash chain computation.]] - rationale - gateway/tests/test_audit_export.py
- [[Verify the integrity of the hash chain.          Args             start_id Sta]] - rationale - gateway/security/audit_store.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_387
SORT file.name ASC
```

## Connections to other communities
- 15 edges to [[_COMMUNITY_Community 112]]
- 2 edges to [[_COMMUNITY_Community 675]]
- 1 edge to [[_COMMUNITY_Ingest API & RBAC Core]]
- 1 edge to [[_COMMUNITY_Community 1397]]
- 1 edge to [[_COMMUNITY_Community 906]]

## Top bridge nodes
- [[AuditEvent]] - degree 25, connects to 5 communities
- [[dot-log_event()_2]] - degree 5, connects to 1 community
- [[dot-verify_hash_chain()]] - degree 4, connects to 1 community
- [[dot-_get_latest_hash()]] - degree 3, connects to 1 community
- [[dot-test_content_hash()]] - degree 3, connects to 1 community