---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "rationale"
community: "_wrap_response()"
location: "L8385"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/_wrap_response
---

# A dropped message past the cooldown window must produce a new notice.

## Connections
- [[.test_suspended_drop_notice_fires_again_after_cooldown()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/_wrap_response