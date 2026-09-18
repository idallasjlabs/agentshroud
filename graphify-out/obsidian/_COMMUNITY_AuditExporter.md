---
type: community
cohesion: 0.10
members: 27
---

# AuditExporter

**Cohesion:** 0.10 - loosely connected
**Members:** 27 nodes

## Members
- [[.audit_store()]] - code - gateway/tests/test_audit_export.py
- [[.test_content_hash()]] - code - gateway/tests/test_audit_export.py
- [[.test_entry_hash_chain()]] - code - gateway/tests/test_audit_export.py
- [[.test_event_creation()]] - code - gateway/tests/test_audit_export.py
- [[.test_export_cef()]] - code - gateway/tests/test_audit_export.py
- [[.test_export_filtering()]] - code - gateway/tests/test_audit_export.py
- [[.test_export_json()]] - code - gateway/tests/test_audit_export.py
- [[.test_export_json_ld()]] - code - gateway/tests/test_audit_export.py
- [[.test_tamper_detection()]] - code - gateway/tests/test_audit_export.py
- [[.test_verify_export_integrity()]] - code - gateway/tests/test_audit_export.py
- [[AuditExporter]] - code - gateway/security/audit_export.py
- [[Create audit store with test data.]] - rationale - gateway/tests/test_audit_export.py
- [[Exports audit events in various compliance formats.]] - rationale - gateway/security/audit_export.py
- [[Test AuditEvent functionality.]] - rationale - gateway/tests/test_audit_export.py
- [[Test AuditExporter functionality.]] - rationale - gateway/tests/test_audit_export.py
- [[Test CEF export format.]] - rationale - gateway/tests/test_audit_export.py
- [[Test JSON export format.]] - rationale - gateway/tests/test_audit_export.py
- [[Test JSON-LD export format.]] - rationale - gateway/tests/test_audit_export.py
- [[Test basic audit event creation.]] - rationale - gateway/tests/test_audit_export.py
- [[Test content hash computation.]] - rationale - gateway/tests/test_audit_export.py
- [[Test export integrity verification.]] - rationale - gateway/tests/test_audit_export.py
- [[Test export with filters.]] - rationale - gateway/tests/test_audit_export.py
- [[Test hash chain computation.]] - rationale - gateway/tests/test_audit_export.py
- [[Test tamper detection in exports.]] - rationale - gateway/tests/test_audit_export.py
- [[TestAuditEvent]] - code - gateway/tests/test_audit_export.py
- [[TestAuditExporter]] - code - gateway/tests/test_audit_export.py
- [[test_audit_export.py]] - code - gateway/tests/test_audit_export.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/AuditExporter
SORT file.name ASC
```

## Connections to other communities
- 13 edges to [[_COMMUNITY_AuditStore]]
- 10 edges to [[_COMMUNITY_ingest_apimain.py]]
- 6 edges to [[_COMMUNITY_AuditExportConfig]]
- 6 edges to [[_COMMUNITY_AuditEvent]]
- 3 edges to [[_COMMUNITY_TestAuditStore]]
- 2 edges to [[_COMMUNITY_TestAuditStoreBotId]]

## Top bridge nodes
- [[AuditExporter]] - degree 33, connects to 6 communities
- [[test_audit_export.py]] - degree 8, connects to 4 communities
- [[TestAuditExporter]] - degree 15, connects to 3 communities
- [[TestAuditEvent]] - degree 9, connects to 2 communities
- [[.test_content_hash()]] - degree 3, connects to 1 community