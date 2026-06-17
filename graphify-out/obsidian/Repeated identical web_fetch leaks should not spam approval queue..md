---
source_file: "gateway/tests/test_telegram_proxy_outbound.py"
type: "rationale"
community: "Telegram Outbound Test Coverage"
location: "L2647"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Telegram_Outbound_Test_Coverage
---

# Repeated identical web_fetch leaks should not spam approval queue.

## Connections
- [[.test_raw_web_fetch_json_approval_queue_is_cooldown_deduped()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Telegram_Outbound_Test_Coverage