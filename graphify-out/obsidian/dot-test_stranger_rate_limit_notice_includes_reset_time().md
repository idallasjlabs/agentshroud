---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "code"
community: "Unknown/unapproved users have stricter rate limits than collaborators. After…"
location: "L7820"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Unknown/unapproved_users_have_stricter_rate_limits_than_collaborators_After
---

# .test_stranger_rate_limit_notice_includes_reset_time()

## Connections
- [[FakeRBAC]] - `calls` [EXTRACTED]
- [[PassthroughPipeline]] - `calls` [EXTRACTED]
- [[TestStrangerRateLimit]] - `method` [EXTRACTED]
- [[_send_stranger_rate_limit_notice must include a reset time in HHMM UTC format.]] - `rationale_for` [EXTRACTED]
- [[asyncio]] - `references` [EXTRACTED]
- [[fake_urlopen()_60]] - `contains` [EXTRACTED]
- [[fake_urlopen()_20]] - `indirect_call` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/Unknown/unapproved_users_have_stricter_rate_limits_than_collaborators_After
