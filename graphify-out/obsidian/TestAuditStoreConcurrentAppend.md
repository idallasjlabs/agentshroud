---
source_file: "gateway/tests/test_audit_export.py"
type: "code"
community: "Community 254"
location: "L407"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Community_254
---

# TestAuditStoreConcurrentAppend

## Connections
- [[.test_concurrent_log_event_single_store_keeps_linear_chain()]] - `method` [EXTRACTED]
- [[.test_concurrent_log_event_two_connections_keeps_linear_chain()]] - `method` [EXTRACTED]
- [[AuditEvent_1]] - `uses` [INFERRED]
- [[AuditExportConfig_1]] - `uses` [INFERRED]
- [[AuditExporter]] - `uses` [INFERRED]
- [[AuditStore_1]] - `uses` [INFERRED]
- [[Concurrent log_event calls must not fork the SHA-256 chain (SCRUM-204).]] - `rationale_for` [EXTRACTED]
- [[test_audit_export.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Community_254