---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "code"
community: "full_access collaborators must pass through middleware and secondary pipeline…"
location: "L9505"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/full_access_collaborators_must_pass_through_middleware_and_secondary_pipeline
---

# .test_project_scoped_collaborator_still_blocked_by_middleware()

## Connections
- [[FakeRBAC]] - `calls` [EXTRACTED]
- [[TestFullAccessMiddlewareBypass]] - `method` [EXTRACTED]
- [[_make_update()]] - `calls` [EXTRACTED]
- [[_wrap_response()]] - `calls` [EXTRACTED]
- [[asyncio]] - `references` [EXTRACTED]
- [[fake_notify_blocked()_2]] - `contains` [EXTRACTED]
- [[fake_notify_blocked()]] - `indirect_call` [INFERRED]
- [[process_request()_2]] - `contains` [EXTRACTED]
- [[project_scoped collaborators are still blocked when middleware blocks (non-…]] - `rationale_for` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/full_access_collaborators_must_pass_through_middleware_and_secondary_pipeline
