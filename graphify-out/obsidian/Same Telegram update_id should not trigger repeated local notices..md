---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "rationale"
community: "PII Config & Test Fixtures"
location: "L5196"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/PII_Config__Test_Fixtures
---

# Same Telegram update_id should not trigger repeated local notices.

## Connections
- [[.test_healthcheck_local_notice_is_deduped_per_update()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/PII_Config__Test_Fixtures