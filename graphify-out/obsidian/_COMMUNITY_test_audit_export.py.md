---
type: community
members: 17
---

# test_audit_export.py

**Members:** 17 nodes

## Members
- [[dot-__init__()_60]] - code - gateway/security/audit_export.py
- [[dot-_default_jsonld_context()]] - code - gateway/security/audit_export.py
- [[dot-export_config()]] - code - gateway/tests/test_audit_export.py
- [[dot-test_concurrent_log_event_single_store_keeps_linear_chain()]] - code - gateway/tests/test_audit_export.py
- [[dot-test_concurrent_log_event_two_connections_keeps_linear_chain()]] - code - gateway/tests/test_audit_export.py
- [[AuditExportConfig]] - code - gateway/security/audit_export.py
- [[Concurrent log_event calls must not fork the SHA-256 chain (SCRUM-204).]] - rationale - gateway/tests/test_audit_export.py
- [[Configuration for audit export functionality.]] - rationale - gateway/security/audit_export.py
- [[Create test export configuration.]] - rationale - gateway/tests/test_audit_export.py
- [[Default JSON-LD context for security ontology.]] - rationale - gateway/security/audit_export.py
- [[TestAuditStoreConcurrentAppend]] - code - gateway/tests/test_audit_export.py
- [[Two stores sharing one SQLite file (e.g. two workers) must not fork the chain.]] - rationale - gateway/tests/test_audit_export.py
- [[_assert_linear_chain()]] - code - gateway/tests/test_audit_export.py
- [[_chain_rows()]] - code - gateway/tests/test_audit_export.py
- [[audit_export.py]] - code - gateway/security/audit_export.py
- [[audit_store.py]] - code - gateway/security/audit_store.py
- [[test_audit_export.py]] - code - gateway/tests/test_audit_export.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_audit_exportpy
SORT file.name ASC
```

## Connections to other communities
- 7 edges to [[_COMMUNITY_AuditStore]]
- 6 edges to [[_COMMUNITY_AuditExporter]]
- 4 edges to [[_COMMUNITY_AuditEvent]]
- 4 edges to [[_COMMUNITY_asyncio_6]]
- 2 edges to [[_COMMUNITY_ingest_apimain.py]]
- 1 edge to [[_COMMUNITY_TestAuditStore]]
- 1 edge to [[_COMMUNITY_aiosqlite]]
- 1 edge to [[_COMMUNITY_test_edge_e2e_sdk.py]]
- 1 edge to [[_COMMUNITY_test_edge_pipeline.py]]

## Top bridge nodes
- [[test_audit_export.py]] - degree 14, connects to 5 communities
- [[audit_store.py]] - degree 7, connects to 5 communities
- [[audit_export.py]] - degree 6, connects to 3 communities
- [[AuditExportConfig]] - degree 10, connects to 2 communities
- [[dot-test_concurrent_log_event_two_connections_keeps_linear_chain()]] - degree 6, connects to 2 communities
