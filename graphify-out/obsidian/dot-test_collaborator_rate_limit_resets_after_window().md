---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "code"
community: "RateLimiter"
location: "L7866"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/RateLimiter
---

# .test_collaborator_rate_limit_resets_after_window()

## Connections
- [[FakeRBAC]] - `calls` [EXTRACTED]
- [[Messages within the window are blocked; after the window passes they succeed.]] - `rationale_for` [EXTRACTED]
- [[PassthroughPipeline]] - `calls` [EXTRACTED]
- [[RateLimiter]] - `calls` [EXTRACTED]
- [[TestCollaboratorRateLimitRecovery]] - `method` [EXTRACTED]
- [[_make_update()]] - `calls` [EXTRACTED]
- [[_wrap_response()]] - `calls` [EXTRACTED]
- [[asyncio_19]] - `references` [EXTRACTED]
- [[fake_rl_notice()_2]] - `contains` [EXTRACTED]
- [[fake_rl_notice()]] - `indirect_call` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/RateLimiter
