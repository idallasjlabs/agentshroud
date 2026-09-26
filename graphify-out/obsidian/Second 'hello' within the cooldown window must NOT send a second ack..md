---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "rationale"
community: "test_soc_bots.py"
location: "L9321"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/test_soc_botspy
---

# Second 'hello' within the cooldown window must NOT send a second ack.

## Connections
- [[.test_cooldown_suppresses_second_ack()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/test_soc_botspy