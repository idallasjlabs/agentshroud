---
source_file: "gateway/tests/test_group_isolation.py"
type: "rationale"
community: "Shared Memory Write Acl"
location: "L106"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Shared_Memory_Write_Acl
---

# Content appended to group-B must not appear in group-A memory.

## Connections
- [[.test_group_b_write_invisible_from_group_a()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Shared_Memory_Write_Acl