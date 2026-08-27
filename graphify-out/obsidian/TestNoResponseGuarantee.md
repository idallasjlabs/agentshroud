---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "code"
community: "Community 124"
location: "L7927"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Community_124
---

# TestNoResponseGuarantee

## Connections
- [[.test_collaborator_always_gets_response_for_generic_message()]] - `method` [EXTRACTED]
- [[.test_collaborator_blocked_command_always_gets_notice()]] - `method` [EXTRACTED]
- [[.test_unknown_user_always_gets_pending_or_rate_limit_notice()]] - `method` [EXTRACTED]
- [[Every collaborator message must produce a response — never a silent drop.]] - `rationale_for` [EXTRACTED]
- [[MiddlewareResult]] - `uses` [INFERRED]
- [[Owner messages are never rate-limited by the collaborator limiter.]] - `rationale_for` [EXTRACTED]
- [[RateLimiter]] - `uses` [INFERRED]
- [[TelegramAPIProxy]] - `uses` [INFERRED]
- [[test_telegram_proxy_inbound.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Community_124