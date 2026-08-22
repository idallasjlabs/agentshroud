---
source_file: "gateway/tests/test_shared_memory_write_acl.py"
type: "rationale"
community: "Shared Memory Write Acl"
location: "L95"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Shared_Memory_Write_Acl
---

# A user who is NOT a member of the target group cannot poison its memory.

## Connections
- [[.test_non_member_write_is_blocked()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Shared_Memory_Write_Acl