---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "code"
community: "Owner /approve should fail closed when target has no pending request."
location: "L1343"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Owner_/approve_should_fail_closed_when_target_has_no_pending_request
---

# .test_unknown_user_repeated_start_still_gets_pending_notice()

## Connections
- [[FakeRBAC]] - `calls` [EXTRACTED]
- [[PassthroughPipeline]] - `calls` [EXTRACTED]
- [[TestInboundPipelineOnGetUpdates]] - `method` [EXTRACTED]
- [[Unknown users should still receive pending notice on repeated start during…]] - `rationale_for` [EXTRACTED]
- [[_make_update()]] - `calls` [EXTRACTED]
- [[_wrap_response()]] - `calls` [EXTRACTED]
- [[asyncio]] - `references` [EXTRACTED]
- [[fake_owner_notice()_18]] - `contains` [EXTRACTED]
- [[fake_owner_notice()_4]] - `indirect_call` [INFERRED]
- [[fake_pending_notice()_2]] - `contains` [EXTRACTED]
- [[fake_pending_notice()_1]] - `indirect_call` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/Owner_/approve_should_fail_closed_when_target_has_no_pending_request
