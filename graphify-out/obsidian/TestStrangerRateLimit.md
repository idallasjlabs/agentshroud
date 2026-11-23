---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "code"
community: "test_telegram_proxy_inbound.py"
location: "L7722"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/test_telegram_proxy_inboundpy
---

# TestStrangerRateLimit

## Connections
- [[dot-test_stranger_exceeding_limit_gets_rate_limit_notice_not_owner_notice()]] - `method` [EXTRACTED]
- [[dot-test_stranger_rate_limit_cooldown_suppresses_repeated_notices()]] - `method` [EXTRACTED]
- [[dot-test_stranger_rate_limit_notice_includes_reset_time()]] - `method` [EXTRACTED]
- [[dot-test_stranger_within_limit_triggers_approval_workflow()]] - `method` [EXTRACTED]
- [[TelegramAPIProxy]] - `uses` [INFERRED]
- [[Unknownunapproved users have stricter rate limits than collaborators. After…]] - `rationale_for` [EXTRACTED]
- [[test_telegram_proxy_inbound.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/test_telegram_proxy_inboundpy
