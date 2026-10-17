---
type: community
members: 32
---

# AuditExporter

**Members:** 32 nodes

## Members
- [[dot-_export_cef()]] - code - gateway/security/audit_export.py
- [[dot-_export_json()]] - code - gateway/security/audit_export.py
- [[dot-_export_jsonld()]] - code - gateway/security/audit_export.py
- [[dot-_parse_cef_for_verification()]] - code - gateway/security/audit_export.py
- [[dot-audit_store()]] - code - gateway/tests/test_audit_export.py
- [[dot-export_events()]] - code - gateway/security/audit_export.py
- [[dot-test_export_cef()]] - code - gateway/tests/test_audit_export.py
- [[dot-test_export_filtering()]] - code - gateway/tests/test_audit_export.py
- [[dot-test_export_json()]] - code - gateway/tests/test_audit_export.py
- [[dot-test_export_json_ld()]] - code - gateway/tests/test_audit_export.py
- [[dot-test_tamper_detection()]] - code - gateway/tests/test_audit_export.py
- [[dot-test_verify_export_integrity()]] - code - gateway/tests/test_audit_export.py
- [[dot-verify_export_integrity()]] - code - gateway/security/audit_export.py
- [[AuditEvent]] - code - gateway/security/audit_export.py
- [[AuditExporter]] - code - gateway/security/audit_export.py
- [[Create audit store with test data.]] - rationale - gateway/tests/test_audit_export.py
- [[Export audit events in the specified format.          Args             start_ti]] - rationale - gateway/security/audit_export.py
- [[Export events in Common Event Format (CEF).          CEF Format CEFVersionDev]] - rationale - gateway/security/audit_export.py
- [[Export events in JSON-LD format with security ontology.]] - rationale - gateway/security/audit_export.py
- [[Export events in standard JSON format.]] - rationale - gateway/security/audit_export.py
- [[Exports audit events in various compliance formats.]] - rationale - gateway/security/audit_export.py
- [[Parse CEF lines and extract entryHashpreviousHash for chain verification.]] - rationale - gateway/security/audit_export.py
- [[Test AuditExporter functionality.]] - rationale - gateway/tests/test_audit_export.py
- [[Test CEF export format.]] - rationale - gateway/tests/test_audit_export.py
- [[Test JSON export format.]] - rationale - gateway/tests/test_audit_export.py
- [[Test JSON-LD export format.]] - rationale - gateway/tests/test_audit_export.py
- [[Test export integrity verification.]] - rationale - gateway/tests/test_audit_export.py
- [[Test export with filters.]] - rationale - gateway/tests/test_audit_export.py
- [[Test tamper detection in exports.]] - rationale - gateway/tests/test_audit_export.py
- [[TestAuditExporter]] - code - gateway/tests/test_audit_export.py
- [[TextIO]] - code - gateway/security/audit_export.py
- [[Verify the integrity of an exported audit log.          Args             export]] - rationale - gateway/security/audit_export.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/AuditExporter
SORT file.name ASC
```

## Connections to other communities
- 8 edges to [[_COMMUNITY_AuditStore]]
- 6 edges to [[_COMMUNITY_AuditEvent]]
- 3 edges to [[_COMMUNITY_AuditExporter (3)]]
- 2 edges to [[_COMMUNITY_AuditExporter (2)]]

## Top bridge nodes
- [[AuditExporter]] - degree 22, connects to 4 communities
- [[TestAuditExporter]] - degree 15, connects to 4 communities
- [[AuditEvent]] - degree 6, connects to 2 communities
- [[TextIO]] - degree 3, connects to 2 communities
- [[dot-audit_store()]] - degree 3, connects to 1 community
