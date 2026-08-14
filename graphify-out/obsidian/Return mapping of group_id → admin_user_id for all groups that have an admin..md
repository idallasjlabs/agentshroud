---
source_file: "gateway/security/group_config.py"
type: "rationale"
community: "Group Workspace Isolation"
location: "L151"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Group_Workspace_Isolation
---

# Return mapping of group_id → admin_user_id for all groups that have an admin.

## Connections
- [[.get_group_admin_ids()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Group_Workspace_Isolation