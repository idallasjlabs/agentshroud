---
source_file: "gateway/security/shared_memory.py"
type: "rationale"
community: "Group Workspace Isolation"
location: "L78"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Group_Workspace_Isolation
---

# Return True if ``author_id`` may WRITE to ``group_id`` shared memory.          R

## Connections
- [[._is_authorized_group_writer()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Group_Workspace_Isolation