---
source_file: "gateway/security/audit_store.py"
type: "code"
community: "Audit Store & Ledger"
location: "L54"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Audit_Store__Ledger
---

# AuditEvent

## Connections
- [[.__init__()_46]] - `method` [EXTRACTED]
- [[._generate_event_id()]] - `method` [EXTRACTED]
- [[.compute_content_hash()]] - `method` [EXTRACTED]
- [[.compute_entry_hash()]] - `method` [EXTRACTED]
- [[.log_event()]] - `references` [EXTRACTED]
- [[.query_events()]] - `references` [EXTRACTED]
- [[.test_content_hash()]] - `calls` [EXTRACTED]
- [[.test_entry_hash_chain()]] - `calls` [EXTRACTED]
- [[.test_event_creation()]] - `calls` [EXTRACTED]
- [[.to_dict()_4]] - `method` [EXTRACTED]
- [[.verify_hash_chain()]] - `calls` [EXTRACTED]
- [[AuditEvent]] - `uses` [INFERRED]
- [[AuditExportConfig_1]] - `uses` [INFERRED]
- [[AuditExporter]] - `uses` [INFERRED]
- [[AuditStore]] - `uses` [INFERRED]
- [[Represents a single audit event.      The ``bot_id`` field identifies which bot]] - `rationale_for` [EXTRACTED]
- [[TestAuditEvent]] - `uses` [INFERRED]
- [[TestAuditExporter]] - `uses` [INFERRED]
- [[TestAuditStore]] - `uses` [INFERRED]
- [[TestAuditStoreBotId]] - `uses` [INFERRED]
- [[TextIO]] - `uses` [INFERRED]
- [[audit_export.py]] - `imports` [EXTRACTED]
- [[audit_store.py]] - `contains` [EXTRACTED]
- [[test_audit_export.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Audit_Store__Ledger