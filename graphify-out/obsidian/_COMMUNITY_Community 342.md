---
type: community
cohesion: 0.09
members: 25
---

# Community 342

**Cohesion:** 0.09 - loosely connected
**Members:** 25 nodes

## Members
- [[.__init__()_56]] - code - gateway/security/audit_export.py
- [[.__init__()_57]] - code - gateway/security/audit_store.py
- [[._generate_event_id()]] - code - gateway/security/audit_store.py
- [[._get_latest_hash()]] - code - gateway/security/audit_store.py
- [[.compute_content_hash()]] - code - gateway/security/audit_store.py
- [[.compute_entry_hash()]] - code - gateway/security/audit_store.py
- [[.log_event()]] - code - gateway/security/audit_store.py
- [[.test_content_hash()]] - code - gateway/tests/test_audit_export.py
- [[.test_entry_hash_chain()]] - code - gateway/tests/test_audit_export.py
- [[.test_event_creation()]] - code - gateway/tests/test_audit_export.py
- [[.to_dict()_5]] - code - gateway/security/audit_store.py
- [[.verify_hash_chain()]] - code - gateway/security/audit_store.py
- [[AuditEvent_1]] - code - gateway/security/audit_store.py
- [[AuditStore]] - code - gateway/security/audit_export.py
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
TABLE source_file, type FROM #community/Community_342
SORT file.name ASC
```

## Connections to other communities
- 9 edges to [[_COMMUNITY_Community 258]]
- 9 edges to [[_COMMUNITY_Community 208]]
- 2 edges to [[_COMMUNITY_RBAC & SOC Realtime]]
- 2 edges to [[_COMMUNITY_Community 831]]

## Top bridge nodes
- [[AuditEvent_1]] - degree 25, connects to 4 communities
- [[.__init__()_56]] - degree 3, connects to 2 communities
- [[.log_event()]] - degree 5, connects to 1 community
- [[.verify_hash_chain()]] - degree 4, connects to 1 community
- [[AuditStore]] - degree 3, connects to 1 community