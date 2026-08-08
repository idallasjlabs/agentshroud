---
source_file: "gateway/security/shared_memory.py"
type: "rationale"
community: "Group Workspace Isolation"
location: "L148"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Group_Workspace_Isolation
---

# Read raw private memory for a user.          Args:             user_id: The user

## Connections
- [[.get_user_memory()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Group_Workspace_Isolation