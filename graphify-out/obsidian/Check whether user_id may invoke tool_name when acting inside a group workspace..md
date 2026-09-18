---
source_file: "gateway/security/tool_acl.py"
type: "rationale"
community: "._can_use_tool_impl()"
location: "L377"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/_can_use_tool_impl
---

# Check whether user_id may invoke tool_name when acting inside a group workspace.

## Connections
- [[.can_use_tool_in_group_context()_1]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/_can_use_tool_impl