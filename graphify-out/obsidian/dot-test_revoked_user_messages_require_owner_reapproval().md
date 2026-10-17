---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "code"
community: "Owner /approve should fail closed when target has no pending request."
location: "L1385"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Owner_/approve_should_fail_closed_when_target_has_no_pending_request
---

# .test_revoked_user_messages_require_owner_reapproval()

## Connections
- [[FakeRBAC]] - `calls` [EXTRACTED]
- [[PassthroughPipeline]] - `calls` [EXTRACTED]
- [[Revoked users should be routed into owner re-approval workflow.]] - `rationale_for` [EXTRACTED]
- [[TestInboundPipelineOnGetUpdates]] - `method` [EXTRACTED]
- [[_make_update()]] - `calls` [EXTRACTED]
- [[_wrap_response()]] - `calls` [EXTRACTED]
- [[asyncio]] - `references` [EXTRACTED]
- [[fake_owner_notice()_16]] - `contains` [EXTRACTED]
- [[fake_owner_notice()_4]] - `indirect_call` [INFERRED]
- [[fake_pending_notice()]] - `contains` [EXTRACTED]
- [[fake_pending_notice()_1]] - `indirect_call` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/Owner_/approve_should_fail_closed_when_target_has_no_pending_request
