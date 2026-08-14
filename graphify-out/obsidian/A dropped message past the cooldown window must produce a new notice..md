---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "rationale"
community: "Group RBAC Roles"
location: "L8284"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Group_RBAC_Roles
---

# A dropped message past the cooldown window must produce a new notice.

## Connections
- [[.test_suspended_drop_notice_fires_again_after_cooldown()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Group_RBAC_Roles