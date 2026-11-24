---
type: community
members: 21
---

# asyncio

**Members:** 21 nodes

## Members
- [[dot-test_event_to_dict_includes_bot_id()]] - code - gateway/tests/test_audit_export.py
- [[dot-test_log_event_default_bot_id_is_openclaw()]] - code - gateway/tests/test_audit_export.py
- [[dot-test_log_event_stores_bot_id()]] - code - gateway/tests/test_audit_export.py
- [[dot-test_migration_adds_bot_id_column()]] - code - gateway/tests/test_audit_export.py
- [[dot-test_query_events_bot_filter()]] - code - gateway/tests/test_audit_export.py
- [[dot-test_query_events_bot_filter_combined_with_severity()]] - code - gateway/tests/test_audit_export.py
- [[dot-test_verify_after_archival_uses_explicit_anchor()]] - code - gateway/tests/test_audit_export.py
- [[dot-test_verify_after_archival_without_anchor_fails_closed()]] - code - gateway/tests/test_audit_export.py
- [[dot-test_verify_from_first_row_keeps_genesis_semantics()]] - code - gateway/tests/test_audit_export.py
- [[dot-test_verify_from_mid_chain_detects_relinked_first_row()]] - code - gateway/tests/test_audit_export.py
- [[dot-test_verify_from_mid_chain_detects_tampered_row()]] - code - gateway/tests/test_audit_export.py
- [[dot-test_verify_from_mid_chain_start_id_succeeds()]] - code - gateway/tests/test_audit_export.py
- [[dot-test_verify_unknown_start_id_fails_closed()]] - code - gateway/tests/test_audit_export.py
- [[After the head is archived, the archived predecessor's entry_hash is the anchor.]] - rationale - gateway/tests/test_audit_export.py
- [[Opening a pre-migration DB (no bot_id column) should auto-migrate.]] - rationale - gateway/tests/test_audit_export.py
- [[Rewriting the first examined row's prev_hash must not be self-anchoring.]] - rationale - gateway/tests/test_audit_export.py
- [[TestAuditStoreAnchoredVerify]] - code - gateway/tests/test_audit_export.py
- [[TestAuditStoreBotId]] - code - gateway/tests/test_audit_export.py
- [[Verify per-bot filtering in AuditStore (v1.1.0 multi-bot support).]] - rationale - gateway/tests/test_audit_export.py
- [[asyncio_79]] - code
- [[verify_hash_chain(start_id=X) anchors on X's predecessor (SCRUM-204).]] - rationale - gateway/tests/test_audit_export.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/asyncio
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_AuditExporter]]
- 5 edges to [[_COMMUNITY_AuditStore]]
- 4 edges to [[_COMMUNITY_TestAuditStore]]
- 2 edges to [[_COMMUNITY_AuditEvent]]
- 2 edges to [[_COMMUNITY_dot-test_concurrent_log_event_two_connections_keeps_linear_chain]]

## Top bridge nodes
- [[asyncio_79]] - degree 25, connects to 3 communities
- [[TestAuditStoreAnchoredVerify]] - degree 11, connects to 2 communities
- [[TestAuditStoreBotId]] - degree 10, connects to 2 communities
- [[dot-test_migration_adds_bot_id_column()]] - degree 4, connects to 1 community
