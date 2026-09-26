---
source_file: "gateway/security/group_workspace.py"
type: "rationale"
community: "test_security_audit.py"
location: "L236"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/test_security_auditpy
---

# Read a group's shared memory, gated by member access (fail-closed).

## Connections
- [[.read_group_memory()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/test_security_auditpy