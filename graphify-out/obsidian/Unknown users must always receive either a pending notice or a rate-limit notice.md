---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "rationale"
community: "Telegram Inbound Tests"
location: "L7875"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Telegram_Inbound_Tests
---

# Unknown users must always receive either a pending notice or a rate-limit notice

## Connections
- [[.test_unknown_user_always_gets_pending_or_rate_limit_notice()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Telegram_Inbound_Tests