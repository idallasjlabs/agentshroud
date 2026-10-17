---
source_file: "gateway/tests/test_security_audit.py"
type: "rationale"
community: "AlertDispatcher (2)"
location: "L528"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/AlertDispatcher_2
---

# Access to /proc/self/environ exposes env vars — must be blocked.

## Connections
- [[dot-test_proc_self_environ_blocked()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/AlertDispatcher_2
