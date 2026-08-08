---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "rationale"
community: "Telegram Inbound Tests"
location: "L8314"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Telegram_Inbound_Tests
---

# Immune user must not be dropped by the suspension path (stub must not appear).

## Connections
- [[.test_immune_user_message_passes_through_when_suspended()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Telegram_Inbound_Tests