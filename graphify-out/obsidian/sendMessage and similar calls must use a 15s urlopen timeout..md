---
source_file: "gateway/tests/test_telegram_proxy_outbound.py"
type: "rationale"
community: "TestForwardToTelegramTimeouts"
location: "L4493"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/TestForwardToTelegramTimeouts
---

# sendMessage and similar calls must use a 15s urlopen timeout.

## Connections
- [[.test_non_long_poll_timeout_is_15s()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/TestForwardToTelegramTimeouts