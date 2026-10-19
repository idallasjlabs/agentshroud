---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "code"
community: "TestFullAccessMiddlewareBypass"
location: "L9505"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/TestFullAccessMiddlewareBypass
---

# .test_project_scoped_collaborator_still_blocked_by_middleware()

## Connections
- [[FakeRBAC]] - `calls` [EXTRACTED]
- [[TestFullAccessMiddlewareBypass]] - `method` [EXTRACTED]
- [[_make_update()]] - `calls` [EXTRACTED]
- [[_wrap_response()]] - `calls` [EXTRACTED]
- [[asyncio_3]] - `references` [EXTRACTED]
- [[fake_notify_blocked()_2]] - `contains` [EXTRACTED]
- [[fake_notify_blocked()]] - `indirect_call` [INFERRED]
- [[process_request()_2]] - `contains` [EXTRACTED]
- [[project_scoped collaborators are still blocked when middleware blocks (non-…]] - `rationale_for` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/TestFullAccessMiddlewareBypass
