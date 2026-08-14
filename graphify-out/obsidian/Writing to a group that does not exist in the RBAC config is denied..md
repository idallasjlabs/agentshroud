---
source_file: "gateway/tests/test_shared_memory_write_acl.py"
type: "rationale"
community: "File Sandbox"
location: "L140"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/File_Sandbox
---

# Writing to a group that does not exist in the RBAC config is denied.

## Connections
- [[.test_unknown_group_write_is_blocked()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/File_Sandbox