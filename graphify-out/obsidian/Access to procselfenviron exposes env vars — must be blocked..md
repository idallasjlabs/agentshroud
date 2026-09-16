---
source_file: "gateway/tests/test_security_audit.py"
type: "rationale"
community: "File Sandbox & Privilege Separation Tests"
location: "L528"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/File_Sandbox__Privilege_Separation_Tests
---

# Access to /proc/self/environ exposes env vars — must be blocked.

## Connections
- [[dot-test_proc_self_environ_blocked()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/File_Sandbox__Privilege_Separation_Tests