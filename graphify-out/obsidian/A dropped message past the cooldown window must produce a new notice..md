---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "rationale"
community: "._make_proxy()"
location: "L8403"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/_make_proxy
---

# A dropped message past the cooldown window must produce a new notice.

## Connections
- [[dot-test_suspended_drop_notice_fires_again_after_cooldown()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/_make_proxy
