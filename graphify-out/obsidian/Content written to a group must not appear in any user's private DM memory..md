---
source_file: "gateway/tests/test_group_isolation.py"
type: "rationale"
community: "Shared Memory Write Acl"
location: "L151"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Shared_Memory_Write_Acl
---

# Content written to a group must not appear in any user's private DM memory.

## Connections
- [[.test_group_write_invisible_from_user_dm()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Shared_Memory_Write_Acl