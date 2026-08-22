---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "rationale"
community: "Telegram Proxy Inbound"
location: "L7772"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Telegram_Proxy_Inbound
---

# Repeated rate-limited messages within the cooldown window send at most one notic

## Connections
- [[.test_stranger_rate_limit_cooldown_suppresses_repeated_notices()]] - `rationale_for` [EXTRACTED]
- [[.test_stranger_rate_limit_notice_includes_reset_time()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Telegram_Proxy_Inbound