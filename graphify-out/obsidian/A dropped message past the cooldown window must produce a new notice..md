---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "rationale"
community: "test_soc_bots.py"
location: "L8385"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/test_soc_botspy
---

# A dropped message past the cooldown window must produce a new notice.

## Connections
- [[.test_suspended_drop_notice_fires_again_after_cooldown()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/test_soc_botspy