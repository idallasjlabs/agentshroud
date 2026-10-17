---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "code"
community: "full_access collaborators must pass through middleware and secondary pipeline…"
location: "L9450"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/full_access_collaborators_must_pass_through_middleware_and_secondary_pipeline
---

# .test_full_access_collaborator_passes_despite_multi_turn_middleware_block_without_interrogative()

## Connections
- [[FakeRBAC]] - `calls` [EXTRACTED]
- [[TestFullAccessMiddlewareBypass]] - `method` [EXTRACTED]
- [[_make_update()]] - `calls` [EXTRACTED]
- [[_wrap_response()]] - `calls` [EXTRACTED]
- [[asyncio]] - `references` [EXTRACTED]
- [[fake_notify_blocked()_1]] - `contains` [EXTRACTED]
- [[fake_notify_blocked()]] - `indirect_call` [INFERRED]
- [[full_access bypass applies even when the message has no interrogative marker.…]] - `rationale_for` [EXTRACTED]
- [[process_request()_1]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/full_access_collaborators_must_pass_through_middleware_and_secondary_pipeline
