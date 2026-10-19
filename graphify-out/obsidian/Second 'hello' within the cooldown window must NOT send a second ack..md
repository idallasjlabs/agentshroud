---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "rationale"
community: "._make_proxy()"
location: "L9339"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/_make_proxy
---

# Second 'hello' within the cooldown window must NOT send a second ack.

## Connections
- [[dot-test_cooldown_suppresses_second_ack()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/_make_proxy
