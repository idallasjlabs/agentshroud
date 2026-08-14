---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "rationale"
community: "Group RBAC Roles"
location: "L9220"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Group_RBAC_Roles
---

# Second 'hello' within the cooldown window must NOT send a second ack.

## Connections
- [[.test_cooldown_suppresses_second_ack()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Group_RBAC_Roles