---
source_file: "gateway/tests/test_security_audit_advanced.py"
type: "rationale"
community: "Alert Dispatcher"
location: "L280"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Alert_Dispatcher
---

# Sessions shouldn't leak data under concurrent access.

## Connections
- [[.test_context_guard_session_isolation_under_load()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Alert_Dispatcher