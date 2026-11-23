---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "code"
community: "._make_proxy"
location: "L7914"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/_make_proxy
---

# .test_owner_unaffected_by_collaborator_rate_limiter()

## Connections
- [[FakeRBAC]] - `calls` [EXTRACTED]
- [[Owner messages are never rate-limited by the collaborator limiter.]] - `rationale_for` [EXTRACTED]
- [[PassthroughPipeline]] - `calls` [EXTRACTED]
- [[TestCollaboratorRateLimitRecovery]] - `method` [EXTRACTED]
- [[_make_update()]] - `calls` [EXTRACTED]
- [[_wrap_response()]] - `calls` [EXTRACTED]
- [[asyncio_21]] - `references` [EXTRACTED]
- [[fake_send()_4]] - `contains` [EXTRACTED]
- [[fake_send()_12]] - `indirect_call` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/_make_proxy
