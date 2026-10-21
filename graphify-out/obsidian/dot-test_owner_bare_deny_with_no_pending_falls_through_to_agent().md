---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "code"
community: "fake_owner_notice()"
location: "L1030"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/fake_owner_notice
---

# .test_owner_bare_deny_with_no_pending_falls_through_to_agent()

## Connections
- [[FakeRBAC]] - `calls` [EXTRACTED]
- [[Owner deny with no target and NO pending collaborator request must not be…]] - `rationale_for` [EXTRACTED]
- [[PassthroughPipeline]] - `calls` [EXTRACTED]
- [[TestInboundPipelineOnGetUpdates]] - `method` [EXTRACTED]
- [[_make_update()]] - `calls` [EXTRACTED]
- [[_wrap_response()]] - `calls` [EXTRACTED]
- [[asyncio_3]] - `references` [EXTRACTED]
- [[fake_owner_notice()_9]] - `contains` [EXTRACTED]
- [[fake_owner_notice()_4]] - `indirect_call` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/fake_owner_notice
