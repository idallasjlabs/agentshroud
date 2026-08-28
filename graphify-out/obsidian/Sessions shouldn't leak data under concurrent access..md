---
source_file: "gateway/tests/test_security_audit_advanced.py"
type: "rationale"
community: "Security Audit & Drift Detection"
location: "L274"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Security_Audit__Drift_Detection
---

# Sessions shouldn't leak data under concurrent access.

## Connections
- [[.test_context_guard_session_isolation_under_load()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Security_Audit__Drift_Detection