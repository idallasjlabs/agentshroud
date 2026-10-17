---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "code"
community: "Rate-limit notice path should key retry window by user_id, not chat_id."
location: "L3755"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Rate-limit_notice_path_should_key_retry_window_by_user_id_not_chat_id
---

# fake_rate_notice()

## Connections
- [[dot-test_collaborator_rate_limit_notice_is_sent_for_each_limited_message()]] - `indirect_call` [INFERRED]
- [[dot-test_collaborator_rate_limit_notice_retries_next_message_when_send_fails()]] - `indirect_call` [INFERRED]
- [[dot-test_collaborator_rate_limit_uses_user_id_when_chat_id_differs()]] - `indirect_call` [INFERRED]

#graphify/code #graphify/INFERRED #community/Rate-limit_notice_path_should_key_retry_window_by_user_id_not_chat_id
