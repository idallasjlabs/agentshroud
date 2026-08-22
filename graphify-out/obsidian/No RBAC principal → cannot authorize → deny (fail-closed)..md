---
source_file: "gateway/tests/test_shared_memory_write_acl.py"
type: "rationale"
community: "Shared Memory Write Acl"
location: "L213"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Shared_Memory_Write_Acl
---

# No RBAC principal → cannot authorize → deny (fail-closed).

## Connections
- [[.test_missing_rbac_is_denied()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Shared_Memory_Write_Acl