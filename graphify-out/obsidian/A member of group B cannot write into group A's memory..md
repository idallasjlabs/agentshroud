---
source_file: "gateway/tests/test_shared_memory_write_acl.py"
type: "rationale"
community: "Shared Memory Write Acl"
location: "L107"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Shared_Memory_Write_Acl
---

# A member of group B cannot write into group A's memory.

## Connections
- [[.test_cross_group_member_write_is_blocked()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Shared_Memory_Write_Acl