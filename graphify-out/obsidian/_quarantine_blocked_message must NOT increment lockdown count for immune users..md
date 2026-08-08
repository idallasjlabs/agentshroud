---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "rationale"
community: "Telegram Inbound Tests"
location: "L8417"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Telegram_Inbound_Tests
---

# _quarantine_blocked_message must NOT increment lockdown count for immune users.

## Connections
- [[.test_immune_user_lockdown_not_incremented()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Telegram_Inbound_Tests