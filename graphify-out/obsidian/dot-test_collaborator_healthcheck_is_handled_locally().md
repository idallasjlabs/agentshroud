---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "code"
community: "fake_urlopen"
location: "L4522"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/fake_urlopen
---

# .test_collaborator_healthcheck_is_handled_locally()

## Connections
- [[Collaborator healthcheck should be handled by gateway, not model.]] - `rationale_for` [EXTRACTED]
- [[FakeRBAC]] - `calls` [EXTRACTED]
- [[PassthroughPipeline]] - `calls` [EXTRACTED]
- [[TestInboundPipelineOnGetUpdates]] - `method` [EXTRACTED]
- [[_make_update()]] - `calls` [EXTRACTED]
- [[_wrap_response()]] - `calls` [EXTRACTED]
- [[asyncio_21]] - `references` [EXTRACTED]
- [[fake_urlopen()_55]] - `contains` [EXTRACTED]
- [[fake_urlopen()_62]] - `indirect_call` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/fake_urlopen
