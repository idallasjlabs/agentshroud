---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "code"
community: "Gateway Test Suite"
location: "L7813"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Gateway_Test_Suite
---

# TestCollaboratorRateLimitRecovery

## Connections
- [[.test_collaborator_rate_limit_resets_after_window()]] - `method` [EXTRACTED]
- [[.test_owner_unaffected_by_collaborator_rate_limiter()]] - `method` [EXTRACTED]
- [[After the rate-limit window expires, collaborator messages go through normally.]] - `rationale_for` [EXTRACTED]
- [[MiddlewareResult]] - `uses` [INFERRED]
- [[RateLimiter]] - `uses` [INFERRED]
- [[TelegramAPIProxy]] - `uses` [INFERRED]
- [[test_telegram_proxy_inbound.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Gateway_Test_Suite