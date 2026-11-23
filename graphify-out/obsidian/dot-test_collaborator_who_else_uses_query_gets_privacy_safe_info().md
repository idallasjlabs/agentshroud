---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "code"
community: "fake_urlopen"
location: "L2279"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/fake_urlopen
---

# .test_collaborator_who_else_uses_query_gets_privacy_safe_info()

## Connections
- [[Cross-user activity probes should return privacy-safe collaborator guidance.]] - `rationale_for` [EXTRACTED]
- [[FakeRBAC]] - `calls` [EXTRACTED]
- [[PassthroughPipeline]] - `calls` [EXTRACTED]
- [[TestInboundPipelineOnGetUpdates]] - `method` [EXTRACTED]
- [[_make_update()]] - `calls` [EXTRACTED]
- [[_wrap_response()]] - `calls` [EXTRACTED]
- [[asyncio_21]] - `references` [EXTRACTED]
- [[fake_urlopen()_64]] - `contains` [EXTRACTED]
- [[fake_urlopen()_62]] - `indirect_call` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/fake_urlopen
