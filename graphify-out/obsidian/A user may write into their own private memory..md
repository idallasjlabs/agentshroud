---
source_file: "gateway/tests/test_shared_memory_write_acl.py"
type: "rationale"
community: "test_security_audit.py"
location: "L178"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/test_security_auditpy
---

# A user may write into their own private memory.

## Connections
- [[.test_self_write_succeeds()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/test_security_auditpy