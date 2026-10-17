---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "rationale"
community: "Every collaborator message must produce a response — never a silent drop."
location: "L7993"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Every_collaborator_message_must_produce_a_response__never_a_silent_drop
---

# Unknown users must always receive either a pending notice or a rate-limit…

## Connections
- [[dot-test_unknown_user_always_gets_pending_or_rate_limit_notice()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Every_collaborator_message_must_produce_a_response__never_a_silent_drop
