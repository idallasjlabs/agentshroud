---
source_file: "gateway/tests/test_audit_export.py"
type: "code"
community: "Community 254"
location: "L459"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Community_254
---

# TestAuditStoreAnchoredVerify

## Connections
- [[.store()_1]] - `method` [EXTRACTED]
- [[.test_verify_after_archival_uses_explicit_anchor()]] - `method` [EXTRACTED]
- [[.test_verify_after_archival_without_anchor_fails_closed()]] - `method` [EXTRACTED]
- [[.test_verify_from_first_row_keeps_genesis_semantics()]] - `method` [EXTRACTED]
- [[.test_verify_from_mid_chain_detects_relinked_first_row()]] - `method` [EXTRACTED]
- [[.test_verify_from_mid_chain_detects_tampered_row()]] - `method` [EXTRACTED]
- [[.test_verify_from_mid_chain_start_id_succeeds()]] - `method` [EXTRACTED]
- [[.test_verify_unknown_start_id_fails_closed()]] - `method` [EXTRACTED]
- [[AuditEvent_1]] - `uses` [INFERRED]
- [[AuditExportConfig_1]] - `uses` [INFERRED]
- [[AuditExporter]] - `uses` [INFERRED]
- [[AuditStore_1]] - `uses` [INFERRED]
- [[test_audit_export.py]] - `contains` [EXTRACTED]
- [[verify_hash_chain(start_id=X) anchors on X's predecessor (SCRUM-204).]] - `rationale_for` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Community_254