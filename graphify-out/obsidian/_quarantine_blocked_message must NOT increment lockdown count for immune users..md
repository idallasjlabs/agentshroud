---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "rationale"
community: "_wrap_response()"
location: "L8587"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/_wrap_response
---

# _quarantine_blocked_message must NOT increment lockdown count for immune users.

## Connections
- [[.test_immune_user_lockdown_not_incremented()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/_wrap_response