---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "code"
community: "fake_urlopen"
location: "L750"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/fake_urlopen
---

# .test_owner_revoke_command_cannot_revoke_owner()

## Connections
- [[FakeRBAC]] - `calls` [EXTRACTED]
- [[Owner revoke must fail safely when target is owner id.]] - `rationale_for` [EXTRACTED]
- [[PassthroughPipeline]] - `calls` [EXTRACTED]
- [[TestInboundPipelineOnGetUpdates]] - `method` [EXTRACTED]
- [[_make_update()]] - `calls` [EXTRACTED]
- [[_wrap_response()]] - `calls` [EXTRACTED]
- [[asyncio_21]] - `references` [EXTRACTED]
- [[fake_urlopen()_72]] - `contains` [EXTRACTED]
- [[fake_urlopen()_62]] - `indirect_call` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/fake_urlopen
