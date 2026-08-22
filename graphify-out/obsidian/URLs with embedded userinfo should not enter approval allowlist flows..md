---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "rationale"
community: "Telegram Inbound Proxy Tests"
location: "L6118"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Telegram_Inbound_Proxy_Tests
---

# URLs with embedded userinfo should not enter approval allowlist flows.

## Connections
- [[.test_non_owner_userinfo_url_does_not_queue_egress_preflight()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Telegram_Inbound_Proxy_Tests