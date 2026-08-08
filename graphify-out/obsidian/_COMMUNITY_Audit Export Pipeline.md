---
type: community
cohesion: 0.03
members: 106
---

# Audit Export Pipeline

**Cohesion:** 0.03 - loosely connected
**Members:** 106 nodes

## Members
- [[.__init__()_52]] - code - gateway/security/audit_export.py
- [[.__init__()_53]] - code - gateway/security/audit_export.py
- [[.__init__()_54]] - code - gateway/security/audit_store.py
- [[.__init__()_55]] - code - gateway/security/audit_store.py
- [[._default_jsonld_context()]] - code - gateway/security/audit_export.py
- [[._export_cef()]] - code - gateway/security/audit_export.py
- [[._export_json()]] - code - gateway/security/audit_export.py
- [[._export_jsonld()]] - code - gateway/security/audit_export.py
- [[._generate_event_id()]] - code - gateway/security/audit_store.py
- [[._get_latest_hash()]] - code - gateway/security/audit_store.py
- [[._parse_cef_for_verification()]] - code - gateway/security/audit_export.py
- [[.audit_store()_1]] - code - gateway/tests/test_audit_export.py
- [[.audit_store()]] - code - gateway/tests/test_audit_export.py
- [[.close()_7]] - code - gateway/security/audit_store.py
- [[.compute_content_hash()]] - code - gateway/security/audit_store.py
- [[.compute_entry_hash()]] - code - gateway/security/audit_store.py
- [[.export_config()]] - code - gateway/tests/test_audit_export.py
- [[.export_events()]] - code - gateway/security/audit_export.py
- [[.get_recent_entries()]] - code - gateway/security/audit_store.py
- [[.get_stats()_14]] - code - gateway/security/audit_store.py
- [[.initialize()_3]] - code - gateway/security/audit_store.py
- [[.log_event()]] - code - gateway/security/audit_store.py
- [[.query_events()]] - code - gateway/security/audit_store.py
- [[.store()]] - code - gateway/tests/test_audit_export.py
- [[.test_content_hash()]] - code - gateway/tests/test_audit_export.py
- [[.test_entry_hash_chain()]] - code - gateway/tests/test_audit_export.py
- [[.test_event_creation()]] - code - gateway/tests/test_audit_export.py
- [[.test_event_to_dict_includes_bot_id()]] - code - gateway/tests/test_audit_export.py
- [[.test_export_cef()]] - code - gateway/tests/test_audit_export.py
- [[.test_export_filtering()]] - code - gateway/tests/test_audit_export.py
- [[.test_export_json()]] - code - gateway/tests/test_audit_export.py
- [[.test_export_json_ld()]] - code - gateway/tests/test_audit_export.py
- [[.test_hash_chain_integrity()]] - code - gateway/tests/test_audit_export.py
- [[.test_log_event()]] - code - gateway/tests/test_audit_export.py
- [[.test_log_event_default_bot_id_is_openclaw()]] - code - gateway/tests/test_audit_export.py
- [[.test_log_event_stores_bot_id()]] - code - gateway/tests/test_audit_export.py
- [[.test_migration_adds_bot_id_column()]] - code - gateway/tests/test_audit_export.py
- [[.test_query_events()]] - code - gateway/tests/test_audit_export.py
- [[.test_query_events_bot_filter()]] - code - gateway/tests/test_audit_export.py
- [[.test_query_events_bot_filter_combined_with_severity()]] - code - gateway/tests/test_audit_export.py
- [[.test_stats()]] - code - gateway/tests/test_audit_export.py
- [[.test_tamper_detection()]] - code - gateway/tests/test_audit_export.py
- [[.test_verify_export_integrity()]] - code - gateway/tests/test_audit_export.py
- [[.to_dict()_4]] - code - gateway/security/audit_store.py
- [[.verify_export_integrity()]] - code - gateway/security/audit_export.py
- [[.verify_hash_chain()]] - code - gateway/security/audit_store.py
- [[AuditEvent]] - code - gateway/security/audit_export.py
- [[AuditEvent_1]] - code - gateway/security/audit_store.py
- [[AuditExportConfig_1]] - code - gateway/security/audit_export.py
- [[AuditExporter]] - code - gateway/security/audit_export.py
- [[AuditStore]] - code - gateway/security/audit_export.py
- [[AuditStore_1]] - code - gateway/security/audit_store.py
- [[Close the database connection._1]] - rationale - gateway/security/audit_store.py
- [[Compute SHA-256 hash of event content (excluding hashes).]] - rationale - gateway/security/audit_store.py
- [[Compute entry hash including previous hash (chain).]] - rationale - gateway/security/audit_store.py
- [[Configuration for audit export functionality.]] - rationale - gateway/security/audit_export.py
- [[Convert to dictionary representation.]] - rationale - gateway/security/audit_store.py
- [[Create audit store with test data.]] - rationale - gateway/tests/test_audit_export.py
- [[Create in-memory audit store for testing.]] - rationale - gateway/tests/test_audit_export.py
- [[Create test export configuration.]] - rationale - gateway/tests/test_audit_export.py
- [[Default JSON-LD context for security ontology.]] - rationale - gateway/security/audit_export.py
- [[Export audit events in the specified format.          Args             start_ti]] - rationale - gateway/security/audit_export.py
- [[Export events in Common Event Format (CEF).          CEF Format CEFVersionDev]] - rationale - gateway/security/audit_export.py
- [[Export events in JSON-LD format with security ontology.]] - rationale - gateway/security/audit_export.py
- [[Export events in standard JSON format.]] - rationale - gateway/security/audit_export.py
- [[Exports audit events in various compliance formats.]] - rationale - gateway/security/audit_export.py
- [[Generate a unique event ID based on timestamp + random.]] - rationale - gateway/security/audit_store.py
- [[Get audit store statistics.]] - rationale - gateway/security/audit_store.py
- [[Get the entry_hash of the most recent event for chain continuation.]] - rationale - gateway/security/audit_store.py
- [[Log a new audit event with hash chain integrity.          Args             bot_]] - rationale - gateway/security/audit_store.py
- [[Open the database, create the schema, and run column migrations.          Initia]] - rationale - gateway/security/audit_store.py
- [[Opening a pre-migration DB (no bot_id column) should auto-migrate.]] - rationale - gateway/tests/test_audit_export.py
- [[Parse CEF lines and extract entryHashpreviousHash for chain verification.]] - rationale - gateway/security/audit_export.py
- [[Path_6]] - code - gateway/security/audit_store.py
- [[Query audit events with optional filters.          Args             bot_id Whe]] - rationale - gateway/security/audit_store.py
- [[Represents a single audit event.      The ``bot_id`` field identifies which bot]] - rationale - gateway/security/audit_store.py
- [[Return the most recent audit entries (alias for query_events with limit).]] - rationale - gateway/security/audit_store.py
- [[SQLite-backed audit event store with tamper-evident hash chain.]] - rationale - gateway/security/audit_store.py
- [[Test AuditEvent functionality.]] - rationale - gateway/tests/test_audit_export.py
- [[Test AuditExporter functionality.]] - rationale - gateway/tests/test_audit_export.py
- [[Test AuditStore functionality.]] - rationale - gateway/tests/test_audit_export.py
- [[Test CEF export format.]] - rationale - gateway/tests/test_audit_export.py
- [[Test JSON export format.]] - rationale - gateway/tests/test_audit_export.py
- [[Test JSON-LD export format.]] - rationale - gateway/tests/test_audit_export.py
- [[Test audit store statistics.]] - rationale - gateway/tests/test_audit_export.py
- [[Test basic audit event creation.]] - rationale - gateway/tests/test_audit_export.py
- [[Test content hash computation.]] - rationale - gateway/tests/test_audit_export.py
- [[Test export integrity verification.]] - rationale - gateway/tests/test_audit_export.py
- [[Test export with filters.]] - rationale - gateway/tests/test_audit_export.py
- [[Test hash chain computation.]] - rationale - gateway/tests/test_audit_export.py
- [[Test hash chain maintains integrity.]] - rationale - gateway/tests/test_audit_export.py
- [[Test logging audit events.]] - rationale - gateway/tests/test_audit_export.py
- [[Test querying events with filters.]] - rationale - gateway/tests/test_audit_export.py
- [[Test tamper detection in exports.]] - rationale - gateway/tests/test_audit_export.py
- [[TestAuditEvent]] - code - gateway/tests/test_audit_export.py
- [[TestAuditExporter]] - code - gateway/tests/test_audit_export.py
- [[TestAuditStore]] - code - gateway/tests/test_audit_export.py
- [[TestAuditStoreBotId]] - code - gateway/tests/test_audit_export.py
- [[TextIO]] - code - gateway/security/audit_export.py
- [[Verify per-bot filtering in AuditStore (v1.1.0 multi-bot support).]] - rationale - gateway/tests/test_audit_export.py
- [[Verify the integrity of an exported audit log.          Args             export]] - rationale - gateway/security/audit_export.py
- [[Verify the integrity of the hash chain.          Args             start_id Sta]] - rationale - gateway/security/audit_store.py
- [[audit_export.py]] - code - gateway/security/audit_export.py
- [[audit_store.py]] - code - gateway/security/audit_store.py
- [[soc_export()]] - code - gateway/ingest_api/main.py
- [[test_audit_export.py]] - code - gateway/tests/test_audit_export.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Audit_Export_Pipeline
SORT file.name ASC
```

## Connections to other communities
- 19 edges to [[_COMMUNITY_Auth & Exception Types]]
- 18 edges to [[_COMMUNITY_Egress & RBAC Security Core]]
- 6 edges to [[_COMMUNITY_Approval & FastAPI Ingest]]
- 4 edges to [[_COMMUNITY_Gateway Test Suite]]
- 2 edges to [[_COMMUNITY_Security Module Middleware]]
- 1 edge to [[_COMMUNITY_Gateway Security Module]]
- 1 edge to [[_COMMUNITY_Gateway Test Suite]]

## Top bridge nodes
- [[AuditExporter]] - degree 42, connects to 4 communities
- [[AuditExportConfig_1]] - degree 33, connects to 4 communities
- [[AuditStore_1]] - degree 34, connects to 3 communities
- [[soc_export()]] - degree 5, connects to 2 communities
- [[audit_export.py]] - degree 6, connects to 1 community