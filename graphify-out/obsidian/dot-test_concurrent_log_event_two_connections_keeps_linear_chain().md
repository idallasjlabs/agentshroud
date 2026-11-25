---
source_file: "gateway/tests/test_audit_export.py"
type: "code"
community: "test_audit_export.py"
location: "L432"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/test_audit_exportpy
---

# .test_concurrent_log_event_two_connections_keeps_linear_chain()

## Connections
- [[AuditStore]] - `calls` [EXTRACTED]
- [[TestAuditStoreConcurrentAppend]] - `method` [EXTRACTED]
- [[Two stores sharing one SQLite file (e.g. two workers) must not fork the chain.]] - `rationale_for` [EXTRACTED]
- [[_assert_linear_chain()]] - `calls` [EXTRACTED]
- [[_chain_rows()]] - `calls` [EXTRACTED]
- [[asyncio_80]] - `references` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/test_audit_exportpy
