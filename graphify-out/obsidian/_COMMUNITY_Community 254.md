---
type: community
members: 66
---

# Community 254

**Members:** 66 nodes

## Members
- [[.__init__()_72]] - code - gateway/security/audit_store.py
- [[._generate_event_id()]] - code - gateway/security/audit_store.py
- [[._get_latest_hash()]] - code - gateway/security/audit_store.py
- [[.compute_content_hash()]] - code - gateway/security/audit_store.py
- [[.compute_entry_hash()]] - code - gateway/security/audit_store.py
- [[.log_event()]] - code - gateway/security/audit_store.py
- [[.store()]] - code - gateway/tests/test_audit_export.py
- [[.store()_1]] - code - gateway/tests/test_audit_export.py
- [[.test_concurrent_log_event_single_store_keeps_linear_chain()]] - code - gateway/tests/test_audit_export.py
- [[.test_concurrent_log_event_two_connections_keeps_linear_chain()]] - code - gateway/tests/test_audit_export.py
- [[.test_content_hash()]] - code - gateway/tests/test_audit_export.py
- [[.test_entry_hash_chain()]] - code - gateway/tests/test_audit_export.py
- [[.test_event_creation()]] - code - gateway/tests/test_audit_export.py
- [[.test_event_to_dict_includes_bot_id()]] - code - gateway/tests/test_audit_export.py
- [[.test_log_event_default_bot_id_is_openclaw()]] - code - gateway/tests/test_audit_export.py
- [[.test_log_event_stores_bot_id()]] - code - gateway/tests/test_audit_export.py
- [[.test_migration_adds_bot_id_column()]] - code - gateway/tests/test_audit_export.py
- [[.test_query_events_bot_filter()]] - code - gateway/tests/test_audit_export.py
- [[.test_query_events_bot_filter_combined_with_severity()]] - code - gateway/tests/test_audit_export.py
- [[.test_verify_after_archival_uses_explicit_anchor()]] - code - gateway/tests/test_audit_export.py
- [[.test_verify_after_archival_without_anchor_fails_closed()]] - code - gateway/tests/test_audit_export.py
- [[.test_verify_from_first_row_keeps_genesis_semantics()]] - code - gateway/tests/test_audit_export.py
- [[.test_verify_from_mid_chain_detects_relinked_first_row()]] - code - gateway/tests/test_audit_export.py
- [[.test_verify_from_mid_chain_detects_tampered_row()]] - code - gateway/tests/test_audit_export.py
- [[.test_verify_from_mid_chain_start_id_succeeds()]] - code - gateway/tests/test_audit_export.py
- [[.test_verify_unknown_start_id_fails_closed()]] - code - gateway/tests/test_audit_export.py
- [[.to_dict()_5]] - code - gateway/security/audit_store.py
- [[.verify_hash_chain()]] - code - gateway/security/audit_store.py
- [[After the head is archived, the archived predecessor's entry_hash is the anchor.]] - rationale - gateway/tests/test_audit_export.py
- [[Audit Ledger Module Badge Icon]] - image - branding/icons/modules/audit-ledger-256x256.png
- [[AuditEvent_1]] - code - gateway/security/audit_store.py
- [[AuditStore]] - code - gateway/security/audit_export.py
- [[Compute SHA-256 hash of event content (excluding hashes).]] - rationale - gateway/security/audit_store.py
- [[Compute entry hash including previous hash (chain).]] - rationale - gateway/security/audit_store.py
- [[Concurrent log_event calls must not fork the SHA-256 chain (SCRUM-204).]] - rationale - gateway/tests/test_audit_export.py
- [[Convert to dictionary representation.]] - rationale - gateway/security/audit_store.py
- [[Database Files]] - document - docs/vault/05 - Dependencies/aiosqlite.md
- [[Generate a unique event ID based on timestamp + random.]] - rationale - gateway/security/audit_store.py
- [[Get the entry_hash of the most recent event for chain continuation.]] - rationale - gateway/security/audit_store.py
- [[Log a new audit event with hash chain integrity.          Args             bot_]] - rationale - gateway/security/audit_store.py
- [[Opening a pre-migration DB (no bot_id column) should auto-migrate.]] - rationale - gateway/tests/test_audit_export.py
- [[Purpose_184]] - document - docs/vault/05 - Dependencies/aiosqlite.md
- [[Related Notes_39]] - document - docs/vault/05 - Dependencies/aiosqlite.md
- [[Represents a single audit event.      The ``bot_id`` field identifies which bot]] - rationale - gateway/security/audit_store.py
- [[Rewriting the first examined row's prev_hash must not be self-anchoring.]] - rationale - gateway/tests/test_audit_export.py
- [[Test AuditEvent functionality.]] - rationale - gateway/tests/test_audit_export.py
- [[Test basic audit event creation.]] - rationale - gateway/tests/test_audit_export.py
- [[Test content hash computation.]] - rationale - gateway/tests/test_audit_export.py
- [[Test hash chain computation.]] - rationale - gateway/tests/test_audit_export.py
- [[TestAuditEvent]] - code - gateway/tests/test_audit_export.py
- [[TestAuditStoreAnchoredVerify]] - code - gateway/tests/test_audit_export.py
- [[TestAuditStoreBotId]] - code - gateway/tests/test_audit_export.py
- [[TestAuditStoreConcurrentAppend]] - code - gateway/tests/test_audit_export.py
- [[Two stores sharing one SQLite file (e.g. two workers) must not fork the chain.]] - rationale - gateway/tests/test_audit_export.py
- [[Verify per-bot filtering in AuditStore (v1.1.0 multi-bot support).]] - rationale - gateway/tests/test_audit_export.py
- [[Verify the integrity of the hash chain.          The first examined row's prev_h]] - rationale - gateway/security/audit_store.py
- [[WAL Mode]] - document - docs/vault/05 - Dependencies/aiosqlite.md
- [[Where Used]] - document - docs/vault/05 - Dependencies/aiosqlite.md
- [[_assert_linear_chain()]] - code - gateway/tests/test_audit_export.py
- [[_chain_rows()]] - code - gateway/tests/test_audit_export.py
- [[aiosqlite_1]] - document - docs/vault/05 - Dependencies/aiosqlite.md
- [[aiosqlite]] - document - docs/vault/05 - Dependencies/aiosqlite.md
- [[audit_export.py]] - code - gateway/security/audit_export.py
- [[audit_store.py]] - code - gateway/security/audit_store.py
- [[test_audit_export.py]] - code - gateway/tests/test_audit_export.py
- [[verify_hash_chain(start_id=X) anchors on X's predecessor (SCRUM-204).]] - rationale - gateway/tests/test_audit_export.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_254
SORT file.name ASC
```

## Connections to other communities
- 18 edges to [[_COMMUNITY_Community 32]]
- 15 edges to [[_COMMUNITY_Community 978]]
- 4 edges to [[_COMMUNITY_Community 479]]
- 2 edges to [[_COMMUNITY_Community 1290]]
- 2 edges to [[_COMMUNITY_Community 162]]
- 1 edge to [[_COMMUNITY_Community 333]]
- 1 edge to [[_COMMUNITY_Community 707]]
- 1 edge to [[_COMMUNITY_Community 1214]]
- 1 edge to [[_COMMUNITY_Community 253]]

## Top bridge nodes
- [[AuditEvent_1]] - degree 27, connects to 4 communities
- [[test_audit_export.py]] - degree 12, connects to 3 communities
- [[audit_export.py]] - degree 6, connects to 3 communities
- [[aiosqlite]] - degree 5, connects to 3 communities
- [[TestAuditStoreAnchoredVerify]] - degree 14, connects to 2 communities