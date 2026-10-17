---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "code"
community: "Owner /approve should fail closed when target has no pending request."
location: "L847"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Owner_/approve_should_fail_closed_when_target_has_no_pending_request
---

# .test_owner_deny_command_denies_pending_user()

## Connections
- [[FakeRBAC]] - `calls` [EXTRACTED]
- [[Owner deny should deny pending collaborator and notify both parties.]] - `rationale_for` [EXTRACTED]
- [[PassthroughPipeline]] - `calls` [EXTRACTED]
- [[TestInboundPipelineOnGetUpdates]] - `method` [EXTRACTED]
- [[_make_update()]] - `calls` [EXTRACTED]
- [[_wrap_response()]] - `calls` [EXTRACTED]
- [[asyncio]] - `references` [EXTRACTED]
- [[fake_owner_notice()_11]] - `contains` [EXTRACTED]
- [[fake_owner_notice()_4]] - `indirect_call` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/Owner_/approve_should_fail_closed_when_target_has_no_pending_request
