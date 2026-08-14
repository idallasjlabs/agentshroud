---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "rationale"
community: "Group RBAC Roles"
location: "L7989"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Group_RBAC_Roles
---

# /unlock <uid> must call reset() on the lockdown module and confirm to owner.

## Connections
- [[.test_unlock_calls_reset_on_lockdown()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Group_RBAC_Roles