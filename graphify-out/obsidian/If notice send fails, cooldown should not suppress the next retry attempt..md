---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "rationale"
community: "Rate-limit notice path should key retry window by user_id, not chat_id."
location: "L3824"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Rate-limit_notice_path_should_key_retry_window_by_user_id_not_chat_id
---

# If notice send fails, cooldown should not suppress the next retry attempt.

## Connections
- [[dot-test_collaborator_rate_limit_notice_retries_next_message_when_send_fails()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Rate-limit_notice_path_should_key_retry_window_by_user_id_not_chat_id
