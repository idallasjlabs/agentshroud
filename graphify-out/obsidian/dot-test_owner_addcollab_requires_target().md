---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "code"
community: "fake_owner_notice()"
location: "L1180"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/fake_owner_notice
---

# .test_owner_addcollab_requires_target()

## Connections
- [[FakeRBAC]] - `calls` [EXTRACTED]
- [[Owner addcollab without target should return usage guidance.]] - `rationale_for` [EXTRACTED]
- [[PassthroughPipeline]] - `calls` [EXTRACTED]
- [[TestInboundPipelineOnGetUpdates]] - `method` [EXTRACTED]
- [[_make_update()]] - `calls` [EXTRACTED]
- [[_wrap_response()]] - `calls` [EXTRACTED]
- [[asyncio_3]] - `references` [EXTRACTED]
- [[fake_owner_notice()_2]] - `contains` [EXTRACTED]
- [[fake_owner_notice()_4]] - `indirect_call` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/fake_owner_notice
