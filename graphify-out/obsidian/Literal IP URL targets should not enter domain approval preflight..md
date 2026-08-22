---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "rationale"
community: "Telegram Inbound Proxy Tests"
location: "L6540"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Telegram_Inbound_Proxy_Tests
---

# Literal IP URL targets should not enter domain approval preflight.

## Connections
- [[.test_non_owner_ip_url_does_not_queue_egress_preflight()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Telegram_Inbound_Proxy_Tests