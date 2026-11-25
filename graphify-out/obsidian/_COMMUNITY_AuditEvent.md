---
type: community
members: 21
---

# AuditEvent

**Members:** 21 nodes

## Members
- [[dot-__init__()_200]] - code - gateway/security/audit_store.py
- [[dot-_generate_event_id()]] - code - gateway/security/audit_store.py
- [[dot-compute_content_hash()]] - code - gateway/security/audit_store.py
- [[dot-compute_entry_hash()]] - code - gateway/security/audit_store.py
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
- [[Represents a single audit event. The ``bot_id`` field identifies which bot…]] - rationale - gateway/security/audit_store.py
- [[Test AuditEvent functionality.]] - rationale - gateway/tests/test_audit_export.py
- [[Test basic audit event creation.]] - rationale - gateway/tests/test_audit_export.py
- [[Test content hash computation.]] - rationale - gateway/tests/test_audit_export.py
- [[Test hash chain computation.]] - rationale - gateway/tests/test_audit_export.py
- [[TestAuditEvent]] - code - gateway/tests/test_audit_export.py
- [[Verify the integrity of the hash chain. The first examined row's prev_hash must…]] - rationale - gateway/security/audit_store.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/AuditEvent
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_AuditExporter]]
- 4 edges to [[_COMMUNITY_test_audit_export.py]]
- 3 edges to [[_COMMUNITY_AuditStore]]

## Top bridge nodes
- [[AuditEvent]] - degree 20, connects to 3 communities
- [[TestAuditEvent]] - degree 6, connects to 1 community
- [[dot-verify_hash_chain()]] - degree 3, connects to 1 community
