---
source_file: "gateway/tests/test_security_audit.py"
type: "rationale"
community: "test_security_audit.py"
location: "L528"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/test_security_auditpy
---

# Access to /proc/self/environ exposes env vars — must be blocked.

## Connections
- [[dot-test_proc_self_environ_blocked()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/test_security_auditpy
