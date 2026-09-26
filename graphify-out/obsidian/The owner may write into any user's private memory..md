---
source_file: "gateway/tests/test_shared_memory_write_acl.py"
type: "rationale"
community: "test_security_audit.py"
location: "L189"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/test_security_auditpy
---

# The owner may write into any user's private memory.

## Connections
- [[.test_owner_write_into_user_memory_succeeds()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/test_security_auditpy