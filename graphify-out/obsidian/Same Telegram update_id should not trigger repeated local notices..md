---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "rationale"
community: "_make_update"
location: "L5245"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/_make_update
---

# Same Telegram update_id should not trigger repeated local notices.

## Connections
- [[dot-test_healthcheck_local_notice_is_deduped_per_update()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/_make_update
