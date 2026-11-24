---
type: community
members: 22
---

# AuditEvent

**Members:** 22 nodes

## Members
- [[dot-__init__()_196]] - code - gateway/security/audit_store.py
- [[dot-_generate_event_id()]] - code - gateway/security/audit_store.py
- [[dot-compute_content_hash()]] - code - gateway/security/audit_store.py
- [[dot-compute_entry_hash()]] - code - gateway/security/audit_store.py
- [[dot-test_content_hash()]] - code - gateway/tests/test_audit_export.py
- [[dot-test_entry_hash_chain()]] - code - gateway/tests/test_audit_export.py
- [[dot-test_event_creation()]] - code - gateway/tests/test_audit_export.py
- [[dot-to_dict()_13]] - code - gateway/security/audit_store.py
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
- [[audit_export.py]] - code - gateway/security/audit_export.py
- [[audit_store.py]] - code - gateway/security/audit_store.py
- [[test_audit_export.py]] - code - gateway/tests/test_audit_export.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/AuditEvent
SORT file.name ASC
```

## Connections to other communities
- 7 edges to [[_COMMUNITY_AuditExporter]]
- 6 edges to [[_COMMUNITY_AuditStore]]
- 3 edges to [[_COMMUNITY_dot-test_concurrent_log_event_two_connections_keeps_linear_chain]]
- 2 edges to [[_COMMUNITY_AuditExportConfig]]
- 2 edges to [[_COMMUNITY_asyncio_6]]
- 2 edges to [[_COMMUNITY_test_edge_e2e_sdk.py]]
- 1 edge to [[_COMMUNITY_TestAuditStore]]
- 1 edge to [[_COMMUNITY_GatewayConfig]]

## Top bridge nodes
- [[test_audit_export.py]] - degree 14, connects to 6 communities
- [[audit_store.py]] - degree 7, connects to 3 communities
- [[audit_export.py]] - degree 6, connects to 3 communities
- [[AuditEvent]] - degree 20, connects to 2 communities
