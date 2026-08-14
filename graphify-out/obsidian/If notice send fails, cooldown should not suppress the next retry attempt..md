---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "rationale"
community: "Gateway Test Suite"
location: "L3775"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Gateway_Test_Suite
---

# If notice send fails, cooldown should not suppress the next retry attempt.

## Connections
- [[.test_collaborator_rate_limit_notice_retries_next_message_when_send_fails()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Gateway_Test_Suite