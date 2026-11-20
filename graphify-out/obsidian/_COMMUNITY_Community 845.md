---
type: community
members: 12
---

# Community 845

**Members:** 12 nodes

## Members
- [[.store()_1]] - code - gateway/tests/test_audit_export.py
- [[.test_verify_after_archival_uses_explicit_anchor()]] - code - gateway/tests/test_audit_export.py
- [[.test_verify_after_archival_without_anchor_fails_closed()]] - code - gateway/tests/test_audit_export.py
- [[.test_verify_from_first_row_keeps_genesis_semantics()]] - code - gateway/tests/test_audit_export.py
- [[.test_verify_from_mid_chain_detects_relinked_first_row()]] - code - gateway/tests/test_audit_export.py
- [[.test_verify_from_mid_chain_detects_tampered_row()]] - code - gateway/tests/test_audit_export.py
- [[.test_verify_from_mid_chain_start_id_succeeds()]] - code - gateway/tests/test_audit_export.py
- [[.test_verify_unknown_start_id_fails_closed()]] - code - gateway/tests/test_audit_export.py
- [[After the head is archived, the archived predecessor's entry_hash is the anchor.]] - rationale - gateway/tests/test_audit_export.py
- [[Rewriting the first examined row's prev_hash must not be self-anchoring.]] - rationale - gateway/tests/test_audit_export.py
- [[TestAuditStoreAnchoredVerify]] - code - gateway/tests/test_audit_export.py
- [[verify_hash_chain(start_id=X) anchors on X's predecessor (SCRUM-204).]] - rationale - gateway/tests/test_audit_export.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_845
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_Community 254]]

## Top bridge nodes
- [[TestAuditStoreAnchoredVerify]] - degree 14, connects to 1 community
- [[.store()_1]] - degree 2, connects to 1 community