---
source_file: "gateway/tests/test_security_audit_advanced.py"
type: "rationale"
community: "Session Manager & PII/Context Guard"
location: "L274"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Session_Manager__PII/Context_Guard
---

# Sessions shouldn't leak data under concurrent access.

## Connections
- [[dot-test_context_guard_session_isolation_under_load()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Session_Manager__PII/Context_Guard