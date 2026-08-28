---
source_file: "gateway/tests/test_telegram_proxy_outbound.py"
type: "rationale"
community: "Community 1135"
location: "L4510"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Community_1135
---

# getUpdates must use a 60s urlopen timeout so the long-poll is not aborted early.

## Connections
- [[.test_long_poll_timeout_remains_60s()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Community_1135