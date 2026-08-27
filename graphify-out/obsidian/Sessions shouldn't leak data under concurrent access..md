---
source_file: "gateway/tests/test_security_audit_advanced.py"
type: "rationale"
community: "Community 6"
location: "L274"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Community_6
---

# Sessions shouldn't leak data under concurrent access.

## Connections
- [[.test_context_guard_session_isolation_under_load()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Community_6