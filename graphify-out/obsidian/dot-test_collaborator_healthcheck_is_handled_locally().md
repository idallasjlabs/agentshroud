---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "code"
community: "TestInboundPipelineOnGetUpdates"
location: "L4522"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/TestInboundPipelineOnGetUpdates
---

# .test_collaborator_healthcheck_is_handled_locally()

## Connections
- [[Collaborator healthcheck should be handled by gateway, not model.]] - `rationale_for` [EXTRACTED]
- [[FakeRBAC]] - `calls` [EXTRACTED]
- [[PassthroughPipeline]] - `calls` [EXTRACTED]
- [[TestInboundPipelineOnGetUpdates]] - `method` [EXTRACTED]
- [[_make_update()]] - `calls` [EXTRACTED]
- [[_wrap_response()]] - `calls` [EXTRACTED]
- [[asyncio_3]] - `references` [EXTRACTED]
- [[fake_urlopen()_29]] - `contains` [EXTRACTED]
- [[fake_urlopen()_40]] - `indirect_call` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/TestInboundPipelineOnGetUpdates
