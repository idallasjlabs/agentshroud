---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "code"
community: "skills/openclaw"
location: "L7673"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/skills/openclaw
---

# TestStrangerRateLimit

## Connections
- [[.test_stranger_exceeding_limit_gets_rate_limit_notice_not_owner_notice()]] - `method` [EXTRACTED]
- [[.test_stranger_rate_limit_cooldown_suppresses_repeated_notices()]] - `method` [EXTRACTED]
- [[.test_stranger_rate_limit_notice_includes_reset_time()]] - `method` [EXTRACTED]
- [[.test_stranger_within_limit_triggers_approval_workflow()]] - `method` [EXTRACTED]
- [[MiddlewareResult]] - `uses` [INFERRED]
- [[RateLimiter]] - `uses` [INFERRED]
- [[TelegramAPIProxy]] - `uses` [INFERRED]
- [[Unknownunapproved users have stricter rate limits than collaborators.      Afte]] - `rationale_for` [EXTRACTED]
- [[test_telegram_proxy_inbound.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/skills/openclaw