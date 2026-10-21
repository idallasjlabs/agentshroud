---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "rationale"
community: ".test_collaborator_rate_limit_notice_is_sent_for_each_limited_message()"
location: "L3824"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/test_collaborator_rate_limit_notice_is_sent_for_each_limited_message
---

# If notice send fails, cooldown should not suppress the next retry attempt.

## Connections
- [[dot-test_collaborator_rate_limit_notice_retries_next_message_when_send_fails()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/test_collaborator_rate_limit_notice_is_sent_for_each_limited_message
