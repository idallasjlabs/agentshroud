---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "rationale"
community: "Rate-limit notice path should key retry window by user_id, not chat_id."
location: "L3778"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Rate-limit_notice_path_should_key_retry_window_by_user_id_not_chat_id
---

# Repeated rate-limited messages should each receive a deterministic notice.

## Connections
- [[dot-test_collaborator_rate_limit_notice_is_sent_for_each_limited_message()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Rate-limit_notice_path_should_key_retry_window_by_user_id_not_chat_id
