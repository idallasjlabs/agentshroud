---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "rationale"
community: "PII Config & Test Fixtures"
location: "L5353"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/PII_Config__Test_Fixtures
---

# When update_id is missing, same message_id should dedupe self-diagnostic notices

## Connections
- [[.test_self_diagnose_dedupe_handles_missing_update_id_same_message()]] - `rationale_for` [EXTRACTED]
- [[.test_self_diagnostic_dedupe_handles_missing_update_id_same_message()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/PII_Config__Test_Fixtures