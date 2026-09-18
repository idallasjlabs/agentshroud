---
type: community
cohesion: 0.22
members: 10
---

# AuditExportConfig

**Cohesion:** 0.22 - loosely connected
**Members:** 10 nodes

## Members
- [[.__init__()_8]] - code - gateway/security/audit_export.py
- [[.__init__()_38]] - code - gateway/security/audit_export.py
- [[._default_jsonld_context()]] - code - gateway/security/audit_export.py
- [[.export_config()]] - code - gateway/tests/test_audit_export.py
- [[AuditExportConfig]] - code - gateway/security/audit_export.py
- [[Configuration for audit export functionality.]] - rationale - gateway/security/audit_export.py
- [[Create test export configuration.]] - rationale - gateway/tests/test_audit_export.py
- [[Default JSON-LD context for security ontology.]] - rationale - gateway/security/audit_export.py
- [[Export tamper-evident audit events in SOCSIEM formats.]] - rationale - gateway/ingest_api/main.py
- [[soc_export()]] - code - gateway/ingest_api/main.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/AuditExportConfig
SORT file.name ASC
```

## Connections to other communities
- 12 edges to [[_COMMUNITY_ingest_apimain.py]]
- 6 edges to [[_COMMUNITY_AuditExporter]]
- 4 edges to [[_COMMUNITY_AuditStore]]
- 1 edge to [[_COMMUNITY_TestAuditStore]]
- 1 edge to [[_COMMUNITY_TestAuditStoreBotId]]

## Top bridge nodes
- [[AuditExportConfig]] - degree 24, connects to 5 communities
- [[soc_export()]] - degree 5, connects to 2 communities
- [[.__init__()_38]] - degree 3, connects to 2 communities
- [[.export_config()]] - degree 3, connects to 1 community