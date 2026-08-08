---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "rationale"
community: "Telegram Proxy Test Suite"
location: "L5914"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Telegram_Proxy_Test_Suite
---

# Non-http schemes should not be treated as web-fetch preflight targets.

## Connections
- [[.test_non_owner_non_http_scheme_does_not_queue_egress_preflight()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Telegram_Proxy_Test_Suite