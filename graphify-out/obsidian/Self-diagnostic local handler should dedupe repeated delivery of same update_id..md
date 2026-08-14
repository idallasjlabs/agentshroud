---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "rationale"
community: "PII Config & Test Fixtures"
location: "L5315"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/PII_Config__Test_Fixtures
---

# Self-diagnostic local handler should dedupe repeated delivery of same update_id.

## Connections
- [[.test_self_diagnose_local_notice_is_deduped_per_update()]] - `rationale_for` [EXTRACTED]
- [[.test_self_diagnostic_local_notice_is_deduped_per_update()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/PII_Config__Test_Fixtures