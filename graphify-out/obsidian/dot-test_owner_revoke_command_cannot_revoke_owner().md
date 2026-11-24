---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "code"
community: "_wrap_response"
location: "L750"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/_wrap_response
---

# .test_owner_revoke_command_cannot_revoke_owner()

## Connections
- [[FakeRBAC]] - `calls` [EXTRACTED]
- [[Owner revoke must fail safely when target is owner id.]] - `rationale_for` [EXTRACTED]
- [[PassthroughPipeline]] - `calls` [EXTRACTED]
- [[TestInboundPipelineOnGetUpdates]] - `method` [EXTRACTED]
- [[_make_update()]] - `calls` [EXTRACTED]
- [[_wrap_response()]] - `calls` [EXTRACTED]
- [[asyncio_22]] - `references` [EXTRACTED]
- [[fake_urlopen()_8]] - `contains` [EXTRACTED]
- [[fake_urlopen()_51]] - `indirect_call` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/_wrap_response
