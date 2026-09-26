---
source_file: "gateway/security/shared_memory.py"
type: "rationale"
community: "test_security_audit.py"
location: "L78"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/test_security_auditpy
---

# Return True if ``author_id`` may WRITE to ``group_id`` shared memory.          R

## Connections
- [[._is_authorized_group_writer()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/test_security_auditpy