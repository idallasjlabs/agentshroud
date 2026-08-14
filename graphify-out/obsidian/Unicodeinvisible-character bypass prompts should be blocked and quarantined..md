---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "rationale"
community: "PII Config & Test Fixtures"
location: "L4414"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/PII_Config__Test_Fixtures
---

# Unicode/invisible-character bypass prompts should be blocked and quarantined.

## Connections
- [[.test_collaborator_unicode_bypass_request_is_blocked_and_quarantined()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/PII_Config__Test_Fixtures