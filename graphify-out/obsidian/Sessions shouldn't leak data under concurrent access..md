---
source_file: "gateway/tests/test_security_audit_advanced.py"
type: "rationale"
community: "Security Module Middleware"
location: "L274"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Security_Module_Middleware
---

# Sessions shouldn't leak data under concurrent access.

## Connections
- [[.test_context_guard_session_isolation_under_load()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Security_Module_Middleware