---
source_file: "gateway/security/audit_store.py"
type: "code"
community: "AuditStore"
location: "L54"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/AuditStore
---

# AuditEvent

## Connections
- [[.__init__()_140]] - `method` [EXTRACTED]
- [[._generate_event_id()]] - `method` [EXTRACTED]
- [[.compute_content_hash()]] - `method` [EXTRACTED]
- [[.compute_entry_hash()]] - `method` [EXTRACTED]
- [[.log_event()_2]] - `references` [EXTRACTED]
- [[.query_events()]] - `references` [EXTRACTED]
- [[.test_content_hash()]] - `calls` [EXTRACTED]
- [[.test_entry_hash_chain()]] - `calls` [EXTRACTED]
- [[.test_event_creation()]] - `calls` [EXTRACTED]
- [[.to_dict()_11]] - `method` [EXTRACTED]
- [[.verify_hash_chain()]] - `calls` [EXTRACTED]
- [[AuditEvent_1]] - `uses` [INFERRED]
- [[AuditExportConfig]] - `uses` [INFERRED]
- [[AuditExporter]] - `uses` [INFERRED]
- [[AuditStore]] - `uses` [INFERRED]
- [[AuditStore_1]] - `calls` [EXTRACTED]
- [[Represents a single audit event.      The ``bot_id`` field identifies which bot]] - `rationale_for` [EXTRACTED]
- [[TestAuditEvent]] - `uses` [INFERRED]
- [[TestAuditExporter]] - `uses` [INFERRED]
- [[TestAuditStore]] - `uses` [INFERRED]
- [[TestAuditStoreBotId]] - `uses` [INFERRED]
- [[TextIO]] - `uses` [INFERRED]
- [[audit_export.py]] - `imports` [EXTRACTED]
- [[audit_store.py]] - `contains` [EXTRACTED]
- [[test_audit_export.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/AuditStore