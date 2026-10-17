---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "rationale"
community: "Rate-limit notice path should key retry window by user_id, not chat_id."
location: "L3739"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Rate-limit_notice_path_should_key_retry_window_by_user_id_not_chat_id
---

# Rate-limit notice path should key retry window by user_id, not chat_id.

## Connections
- [[dot-test_collaborator_rate_limit_uses_user_id_when_chat_id_differs()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Rate-limit_notice_path_should_key_retry_window_by_user_id_not_chat_id
