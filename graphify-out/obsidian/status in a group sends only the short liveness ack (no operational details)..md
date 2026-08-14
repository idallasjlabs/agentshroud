---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "rationale"
community: "Group RBAC Roles"
location: "L9151"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Group_RBAC_Roles
---

# /status in a group sends only the short liveness ack (no operational details).

## Connections
- [[.test_cooldown_suppresses_second_ack()]] - `rationale_for` [EXTRACTED]
- [[.test_status_in_group_sends_short_ack_not_full_status()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Group_RBAC_Roles