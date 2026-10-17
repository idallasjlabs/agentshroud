---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "code"
community: "Unknown/unapproved users have stricter rate limits than collaborators. After…"
location: "L7866"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Unknown/unapproved_users_have_stricter_rate_limits_than_collaborators_After
---

# .test_collaborator_rate_limit_resets_after_window()

## Connections
- [[FakeRBAC]] - `calls` [EXTRACTED]
- [[Messages within the window are blocked; after the window passes they succeed.]] - `rationale_for` [EXTRACTED]
- [[PassthroughPipeline]] - `calls` [EXTRACTED]
- [[TestCollaboratorRateLimitRecovery]] - `method` [EXTRACTED]
- [[_make_update()]] - `calls` [EXTRACTED]
- [[_wrap_response()]] - `calls` [EXTRACTED]
- [[asyncio]] - `references` [EXTRACTED]
- [[fake_rl_notice()]] - `contains` [EXTRACTED]
- [[fake_rl_notice()_1]] - `indirect_call` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/Unknown/unapproved_users_have_stricter_rate_limits_than_collaborators_After
