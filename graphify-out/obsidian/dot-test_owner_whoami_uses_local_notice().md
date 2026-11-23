---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "code"
community: "asyncio"
location: "L547"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/asyncio
---

# .test_owner_whoami_uses_local_notice()

## Connections
- [[FakeRBAC]] - `calls` [EXTRACTED]
- [[Owner whoami should be handled locally and include owner role + user id.]] - `rationale_for` [EXTRACTED]
- [[PassthroughPipeline]] - `calls` [EXTRACTED]
- [[TestInboundPipelineOnGetUpdates]] - `method` [EXTRACTED]
- [[_make_update()]] - `calls` [EXTRACTED]
- [[_wrap_response()]] - `calls` [EXTRACTED]
- [[asyncio_21]] - `references` [EXTRACTED]
- [[fake_urlopen()_26]] - `contains` [EXTRACTED]
- [[fake_urlopen()_62]] - `indirect_call` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/asyncio
