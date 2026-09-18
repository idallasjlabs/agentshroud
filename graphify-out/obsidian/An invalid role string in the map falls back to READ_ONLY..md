---
source_file: "gateway/tests/test_group_rbac.py"
type: "rationale"
community: "GroupRoleResolver"
location: "L417"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/GroupRoleResolver
---

# An invalid role string in the map falls back to READ_ONLY.

## Connections
- [[.test_get_role_invalid_string_defaults_to_readonly()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/GroupRoleResolver