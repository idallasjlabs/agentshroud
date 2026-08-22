---
source_file: "gateway/tests/test_group_isolation.py"
type: "rationale"
community: "Shared Memory Write Acl"
location: "L158"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Shared_Memory_Write_Acl
---

# Content written to a user DM must not appear in any group memory.

## Connections
- [[.test_user_dm_write_invisible_from_group()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Shared_Memory_Write_Acl