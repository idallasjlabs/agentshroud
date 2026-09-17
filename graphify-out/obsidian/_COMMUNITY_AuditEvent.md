---
type: community
cohesion: 0.18
members: 13
---

# AuditEvent

**Cohesion:** 0.18 - loosely connected
**Members:** 13 nodes

## Members
- [[._export_cef()]] - code - gateway/security/audit_export.py
- [[._export_json()]] - code - gateway/security/audit_export.py
- [[._export_jsonld()]] - code - gateway/security/audit_export.py
- [[._parse_cef_for_verification()]] - code - gateway/security/audit_export.py
- [[.export_events()]] - code - gateway/security/audit_export.py
- [[.verify_export_integrity()]] - code - gateway/security/audit_export.py
- [[AuditEvent_1]] - code - gateway/security/audit_export.py
- [[Export audit events in the specified format.          Args             start_ti]] - rationale - gateway/security/audit_export.py
- [[Export events in Common Event Format (CEF).          CEF Format CEFVersionDev]] - rationale - gateway/security/audit_export.py
- [[Export events in JSON-LD format with security ontology.]] - rationale - gateway/security/audit_export.py
- [[Export events in standard JSON format.]] - rationale - gateway/security/audit_export.py
- [[Parse CEF lines and extract entryHashpreviousHash for chain verification.]] - rationale - gateway/security/audit_export.py
- [[Verify the integrity of an exported audit log.          Args             export]] - rationale - gateway/security/audit_export.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/AuditEvent
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_AuditExporter]]
- 3 edges to [[_COMMUNITY_AuditStore]]

## Top bridge nodes
- [[.export_events()]] - degree 6, connects to 2 communities
- [[AuditEvent_1]] - degree 6, connects to 1 community
- [[._export_cef()]] - degree 4, connects to 1 community
- [[._export_json()]] - degree 4, connects to 1 community
- [[._export_jsonld()]] - degree 4, connects to 1 community