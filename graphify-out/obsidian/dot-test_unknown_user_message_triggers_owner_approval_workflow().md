---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "code"
community: "fake_owner_notice()"
location: "L1309"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/fake_owner_notice
---

# .test_unknown_user_message_triggers_owner_approval_workflow()

## Connections
- [[FakeRBAC]] - `calls` [EXTRACTED]
- [[PassthroughPipeline]] - `calls` [EXTRACTED]
- [[TestInboundPipelineOnGetUpdates]] - `method` [EXTRACTED]
- [[Unknown non-owner user should trigger pending approval workflow and not forward.]] - `rationale_for` [EXTRACTED]
- [[_make_update()]] - `calls` [EXTRACTED]
- [[_wrap_response()]] - `calls` [EXTRACTED]
- [[asyncio_3]] - `references` [EXTRACTED]
- [[fake_owner_notice()_17]] - `contains` [EXTRACTED]
- [[fake_owner_notice()_4]] - `indirect_call` [INFERRED]
- [[fake_pending_notice()_1]] - `indirect_call` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/fake_owner_notice
