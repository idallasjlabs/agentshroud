---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "code"
community: "PassthroughPipeline"
location: "L5032"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/PassthroughPipeline
---

# .test_self_diagnostic_command_is_handled_locally_for_owner()

## Connections
- [[FakeRBAC]] - `calls` [EXTRACTED]
- [[Owner self-diagnostic should be handled locally by gateway.]] - `rationale_for` [EXTRACTED]
- [[PassthroughPipeline]] - `calls` [EXTRACTED]
- [[TestInboundPipelineOnGetUpdates]] - `method` [EXTRACTED]
- [[_make_update()]] - `calls` [EXTRACTED]
- [[_wrap_response()]] - `calls` [EXTRACTED]
- [[asyncio_19]] - `references` [EXTRACTED]
- [[fake_urlopen()_75]] - `contains` [EXTRACTED]
- [[fake_urlopen()_48]] - `indirect_call` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/PassthroughPipeline
