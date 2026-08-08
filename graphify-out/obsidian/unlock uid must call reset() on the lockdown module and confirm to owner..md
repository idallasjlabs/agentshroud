---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "rationale"
community: "Telegram Inbound Tests"
location: "L7920"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Telegram_Inbound_Tests
---

# /unlock <uid> must call reset() on the lockdown module and confirm to owner.

## Connections
- [[.test_unlock_calls_reset_on_lockdown()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Telegram_Inbound_Tests