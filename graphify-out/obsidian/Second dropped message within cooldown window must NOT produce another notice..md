---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "rationale"
community: "Group RBAC Roles"
location: "L8253"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Group_RBAC_Roles
---

# Second dropped message within cooldown window must NOT produce another notice.

## Connections
- [[.test_suspended_drop_notice_respects_cooldown()_1]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Group_RBAC_Roles