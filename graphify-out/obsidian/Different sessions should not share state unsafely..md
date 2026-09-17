---
source_file: "gateway/tests/test_security_audit.py"
type: "rationale"
community: "test_security_audit.py"
location: "L344"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/test_security_auditpy
---

# Different sessions should not share state unsafely.

## Connections
- [[.test_session_isolation()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/test_security_auditpy