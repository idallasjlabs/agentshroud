---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "code"
community: "full_access collaborators must pass through middleware and secondary pipeline…"
location: "L9410"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/full_access_collaborators_must_pass_through_middleware_and_secondary_pipeline
---

# .test_full_access_collaborator_passes_despite_middleware_block()

## Connections
- [[FakeRBAC]] - `calls` [EXTRACTED]
- [[Middleware block must be bypassed for full_access collaborators.]] - `rationale_for` [EXTRACTED]
- [[TestFullAccessMiddlewareBypass]] - `method` [EXTRACTED]
- [[_make_update()]] - `calls` [EXTRACTED]
- [[_wrap_response()]] - `calls` [EXTRACTED]
- [[asyncio]] - `references` [EXTRACTED]
- [[fake_notify_blocked()]] - `indirect_call` [INFERRED]
- [[process_request()]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/full_access_collaborators_must_pass_through_middleware_and_secondary_pipeline
