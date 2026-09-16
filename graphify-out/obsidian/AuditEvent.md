---
source_file: "gateway/security/audit_store.py"
type: "code"
community: "Community 387"
location: "L54"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Community_387
---

# AuditEvent

## Connections
- [[dot-__init__()_140]] - `method` [EXTRACTED]
- [[dot-_generate_event_id()]] - `method` [EXTRACTED]
- [[dot-compute_content_hash()]] - `method` [EXTRACTED]
- [[dot-compute_entry_hash()]] - `method` [EXTRACTED]
- [[dot-log_event()_2]] - `references` [EXTRACTED]
- [[dot-query_events()]] - `references` [EXTRACTED]
- [[dot-test_content_hash()]] - `calls` [EXTRACTED]
- [[dot-test_entry_hash_chain()]] - `calls` [EXTRACTED]
- [[dot-test_event_creation()]] - `calls` [EXTRACTED]
- [[dot-to_dict()_11]] - `method` [EXTRACTED]
- [[dot-verify_hash_chain()]] - `calls` [EXTRACTED]
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

#graphify/code #graphify/EXTRACTED #community/Community_387