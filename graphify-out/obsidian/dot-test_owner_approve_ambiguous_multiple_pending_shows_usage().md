---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "code"
community: "Owner /approve should fail closed when target has no pending request."
location: "L943"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Owner_/approve_should_fail_closed_when_target_has_no_pending_request
---

# .test_owner_approve_ambiguous_multiple_pending_shows_usage()

## Connections
- [[FakeRBAC]] - `calls` [EXTRACTED]
- [[Owner approve without target, with 2+ pending collaborator requests, is…]] - `rationale_for` [EXTRACTED]
- [[PassthroughPipeline]] - `calls` [EXTRACTED]
- [[TestInboundPipelineOnGetUpdates]] - `method` [EXTRACTED]
- [[_make_update()]] - `calls` [EXTRACTED]
- [[_wrap_response()]] - `calls` [EXTRACTED]
- [[asyncio]] - `references` [EXTRACTED]
- [[fake_owner_notice()_3]] - `contains` [EXTRACTED]
- [[fake_owner_notice()_4]] - `indirect_call` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/Owner_/approve_should_fail_closed_when_target_has_no_pending_request
