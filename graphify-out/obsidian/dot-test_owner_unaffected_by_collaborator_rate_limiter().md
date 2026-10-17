---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "code"
community: "Unknown/unapproved users have stricter rate limits than collaborators. After…"
location: "L7914"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Unknown/unapproved_users_have_stricter_rate_limits_than_collaborators_After
---

# .test_owner_unaffected_by_collaborator_rate_limiter()

## Connections
- [[FakeRBAC]] - `calls` [EXTRACTED]
- [[Owner messages are never rate-limited by the collaborator limiter.]] - `rationale_for` [EXTRACTED]
- [[PassthroughPipeline]] - `calls` [EXTRACTED]
- [[TestCollaboratorRateLimitRecovery]] - `method` [EXTRACTED]
- [[_make_update()]] - `calls` [EXTRACTED]
- [[_wrap_response()]] - `calls` [EXTRACTED]
- [[asyncio]] - `references` [EXTRACTED]
- [[fake_send()_16]] - `contains` [EXTRACTED]
- [[fake_send()_7]] - `indirect_call` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/Unknown/unapproved_users_have_stricter_rate_limits_than_collaborators_After
