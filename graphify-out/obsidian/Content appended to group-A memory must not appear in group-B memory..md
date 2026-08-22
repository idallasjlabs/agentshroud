---
source_file: "gateway/tests/test_group_isolation.py"
type: "rationale"
community: "Shared Memory Write Acl"
location: "L99"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Shared_Memory_Write_Acl
---

# Content appended to group-A memory must not appear in group-B memory.

## Connections
- [[.test_group_a_write_invisible_from_group_b()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Shared_Memory_Write_Acl