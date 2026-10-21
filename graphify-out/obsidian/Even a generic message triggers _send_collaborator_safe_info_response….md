---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "rationale"
community: ".test_unknown_user_always_gets_pending_or_rate_limit_notice()"
location: "L7950"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/test_unknown_user_always_gets_pending_or_rate_limit_notice
---

# Even a generic message triggers _send_collaborator_safe_info_response…

## Connections
- [[dot-test_collaborator_always_gets_response_for_generic_message()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/test_unknown_user_always_gets_pending_or_rate_limit_notice
