---
source_file: "gateway/security/group_config.py"
type: "rationale"
community: "Group Workspace Isolation"
location: "L319"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Group_Workspace_Isolation
---

# Persist a runtime group creation so it survives container restarts.

## Connections
- [[persist_group_create()]] - `rationale_for` [EXTRACTED]
- [[persist_group_delete()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Group_Workspace_Isolation