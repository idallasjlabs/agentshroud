---
source_file: "gateway/tests/test_security_audit.py"
type: "rationale"
community: "_wrap_response()"
location: "L528"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/_wrap_response
---

# Access to /proc/self/environ exposes env vars — must be blocked.

## Connections
- [[dot-test_proc_self_environ_blocked()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/_wrap_response
