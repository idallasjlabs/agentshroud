---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "rationale"
community: "._make_proxy()"
location: "L8605"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/_make_proxy
---

# _quarantine_blocked_message must NOT increment lockdown count for immune users.

## Connections
- [[dot-test_immune_user_lockdown_not_incremented()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/_make_proxy
