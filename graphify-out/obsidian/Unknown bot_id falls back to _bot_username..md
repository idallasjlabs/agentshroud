---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "rationale"
community: "Group RBAC Roles"
location: "L8932"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Group_RBAC_Roles
---

# Unknown bot_id falls back to _bot_username.

## Connections
- [[.test_two_bots_same_group_independent_eligibility()]] - `rationale_for` [EXTRACTED]
- [[.test_username_for_bot_falls_back_to_default()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Group_RBAC_Roles