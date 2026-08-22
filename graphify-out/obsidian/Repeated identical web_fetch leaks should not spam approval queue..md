---
source_file: "gateway/tests/test_telegram_proxy_outbound.py"
type: "rationale"
community: "Telegram Outbound Proxy Tests"
location: "L2657"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Telegram_Outbound_Proxy_Tests
---

# Repeated identical web_fetch leaks should not spam approval queue.

## Connections
- [[.test_raw_web_fetch_json_approval_queue_is_cooldown_deduped()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Telegram_Outbound_Proxy_Tests