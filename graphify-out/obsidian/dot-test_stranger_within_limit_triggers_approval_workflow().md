---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "code"
community: ".test_stranger_within_limit_triggers_approval_workflow()"
location: "L7731"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/test_stranger_within_limit_triggers_approval_workflow
---

# .test_stranger_within_limit_triggers_approval_workflow()

## Connections
- [[FakeRBAC]] - `calls` [EXTRACTED]
- [[First message from unknown user (within limit) queues approval flow.]] - `rationale_for` [EXTRACTED]
- [[PassthroughPipeline]] - `calls` [EXTRACTED]
- [[TestStrangerRateLimit]] - `method` [EXTRACTED]
- [[_make_update()]] - `calls` [EXTRACTED]
- [[_wrap_response()]] - `calls` [EXTRACTED]
- [[asyncio_3]] - `references` [EXTRACTED]
- [[fake_owner_notice()_20]] - `contains` [EXTRACTED]
- [[fake_owner_notice()_4]] - `indirect_call` [INFERRED]
- [[fake_pending_notice()_3]] - `contains` [EXTRACTED]
- [[fake_pending_notice()_1]] - `indirect_call` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/test_stranger_within_limit_triggers_approval_workflow
