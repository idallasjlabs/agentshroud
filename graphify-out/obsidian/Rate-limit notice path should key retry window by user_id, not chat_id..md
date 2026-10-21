---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "rationale"
community: ".test_collaborator_rate_limit_notice_is_sent_for_each_limited_message()"
location: "L3739"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/test_collaborator_rate_limit_notice_is_sent_for_each_limited_message
---

# Rate-limit notice path should key retry window by user_id, not chat_id.

## Connections
- [[dot-test_collaborator_rate_limit_uses_user_id_when_chat_id_differs()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/test_collaborator_rate_limit_notice_is_sent_for_each_limited_message
