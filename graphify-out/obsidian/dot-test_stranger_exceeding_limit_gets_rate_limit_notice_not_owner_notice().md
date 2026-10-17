---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "code"
community: "Unknown/unapproved users have stricter rate limits than collaborators. After…"
location: "L7759"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Unknown/unapproved_users_have_stricter_rate_limits_than_collaborators_After
---

# .test_stranger_exceeding_limit_gets_rate_limit_notice_not_owner_notice()

## Connections
- [[FakeRBAC]] - `calls` [EXTRACTED]
- [[Once stranger exhausts rate limit, they get a rate-limit notice; owner is NOT…]] - `rationale_for` [EXTRACTED]
- [[PassthroughPipeline]] - `calls` [EXTRACTED]
- [[TestStrangerRateLimit]] - `method` [EXTRACTED]
- [[_make_update()]] - `calls` [EXTRACTED]
- [[_wrap_response()]] - `calls` [EXTRACTED]
- [[asyncio]] - `references` [EXTRACTED]
- [[fake_owner_notice()_19]] - `contains` [EXTRACTED]
- [[fake_owner_notice()_4]] - `indirect_call` [INFERRED]
- [[fake_rl_notice()_1]] - `indirect_call` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/Unknown/unapproved_users_have_stricter_rate_limits_than_collaborators_After
