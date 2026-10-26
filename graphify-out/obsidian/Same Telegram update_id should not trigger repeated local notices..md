---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "rationale"
community: "Community 2388"
location: "L5245"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Community_2388
---

# Same Telegram update_id should not trigger repeated local notices.

## Connections
- [[.test_healthcheck_local_notice_is_deduped_per_update()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Community_2388