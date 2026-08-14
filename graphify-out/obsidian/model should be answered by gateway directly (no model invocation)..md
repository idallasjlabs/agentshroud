---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "rationale"
community: "PII Config & Test Fixtures"
location: "L4622"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/PII_Config__Test_Fixtures
---

# /model should be answered by gateway directly (no model invocation).

## Connections
- [[.test_model_status_command_is_handled_locally()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/PII_Config__Test_Fixtures