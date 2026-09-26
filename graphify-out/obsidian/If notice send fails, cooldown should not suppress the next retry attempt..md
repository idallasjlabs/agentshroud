---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "rationale"
community: "test_a2a_proxy.py"
location: "L3806"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/test_a2a_proxypy
---

# If notice send fails, cooldown should not suppress the next retry attempt.

## Connections
- [[.test_collaborator_rate_limit_notice_retries_next_message_when_send_fails()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/test_a2a_proxypy