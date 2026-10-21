---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "code"
community: "TestFullAccessMiddlewareBypass"
location: "L9410"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/TestFullAccessMiddlewareBypass
---

# .test_full_access_collaborator_passes_despite_middleware_block()

## Connections
- [[FakeRBAC]] - `calls` [EXTRACTED]
- [[Middleware block must be bypassed for full_access collaborators.]] - `rationale_for` [EXTRACTED]
- [[TestFullAccessMiddlewareBypass]] - `method` [EXTRACTED]
- [[_make_update()]] - `calls` [EXTRACTED]
- [[_wrap_response()]] - `calls` [EXTRACTED]
- [[asyncio_3]] - `references` [EXTRACTED]
- [[fake_notify_blocked()]] - `indirect_call` [INFERRED]
- [[process_request()]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/TestFullAccessMiddlewareBypass
