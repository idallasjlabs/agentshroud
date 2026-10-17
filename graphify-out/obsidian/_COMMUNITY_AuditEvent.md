---
type: community
members: 27
---

# AuditEvent

**Members:** 27 nodes

## Members
- [[dot-__init__()_124]] - code - gateway/security/audit_store.py
- [[dot-_generate_event_id()]] - code - gateway/security/audit_store.py
- [[dot-_get_latest_hash()]] - code - gateway/security/audit_store.py
- [[dot-compute_content_hash()]] - code - gateway/security/audit_store.py
- [[dot-compute_entry_hash()]] - code - gateway/security/audit_store.py
- [[dot-log_event()_1]] - code - gateway/security/audit_store.py
- [[dot-test_content_hash()]] - code - gateway/tests/test_audit_export.py
- [[dot-test_entry_hash_chain()]] - code - gateway/tests/test_audit_export.py
- [[dot-test_event_creation()]] - code - gateway/tests/test_audit_export.py
- [[dot-to_dict()_9]] - code - gateway/security/audit_store.py
- [[dot-verify_hash_chain()]] - code - gateway/security/audit_store.py
- [[AuditEvent_1]] - code - gateway/security/audit_store.py
- [[Compute SHA-256 hash of event content (excluding hashes).]] - rationale - gateway/security/audit_store.py
- [[Compute entry hash including previous hash (chain).]] - rationale - gateway/security/audit_store.py
- [[Convert to dictionary representation.]] - rationale - gateway/security/audit_store.py
- [[Generate a unique event ID based on timestamp + random.]] - rationale - gateway/security/audit_store.py
- [[Get the entry_hash of the most recent event for chain continuation.]] - rationale - gateway/security/audit_store.py
- [[Log a new audit event with hash chain integrity.          Args             bot_]] - rationale - gateway/security/audit_store.py
- [[Represents a single audit event.      The ``bot_id`` field identifies which bot]] - rationale - gateway/security/audit_store.py
- [[Test AuditEvent functionality.]] - rationale - gateway/tests/test_audit_export.py
- [[Test basic audit event creation.]] - rationale - gateway/tests/test_audit_export.py
- [[Test content hash computation.]] - rationale - gateway/tests/test_audit_export.py
- [[Test hash chain computation.]] - rationale - gateway/tests/test_audit_export.py
- [[TestAuditEvent]] - code - gateway/tests/test_audit_export.py
- [[Verify the integrity of the hash chain.          Args             start_id Sta]] - rationale - gateway/security/audit_store.py
- [[audit_export.py]] - code - gateway/security/audit_export.py
- [[audit_store.py]] - code - gateway/security/audit_store.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/AuditEvent
SORT file.name ASC
```

## Connections to other communities
- 11 edges to [[_COMMUNITY_AuditStore]]
- 6 edges to [[_COMMUNITY_AuditExporter]]
- 4 edges to [[_COMMUNITY_AuditExporter (3)]]
- 2 edges to [[_COMMUNITY_agentshroud-blueteamSKILL]]
- 1 edge to [[_COMMUNITY_02-infrastructure.md (2)]]
- 1 edge to [[_COMMUNITY_egress_filter.py (3)]]
- 1 edge to [[_COMMUNITY_IEC 62443 Compliance Matrix — AgentShroud]]
- 1 edge to [[_COMMUNITY_AuditExporter (2)]]

## Top bridge nodes
- [[AuditEvent_1]] - degree 25, connects to 4 communities
- [[audit_export.py]] - degree 7, connects to 4 communities
- [[audit_store.py]] - degree 6, connects to 4 communities
- [[TestAuditEvent]] - degree 9, connects to 3 communities
- [[dot-log_event()_1]] - degree 5, connects to 1 community
