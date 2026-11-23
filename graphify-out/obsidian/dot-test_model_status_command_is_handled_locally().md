---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "code"
community: "_wrap_response"
location: "L4670"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/_wrap_response
---

# .test_model_status_command_is_handled_locally()

## Connections
- [[model should be answered by gateway directly (no model invocation).]] - `rationale_for` [EXTRACTED]
- [[FakeRBAC]] - `calls` [EXTRACTED]
- [[PassthroughPipeline]] - `calls` [EXTRACTED]
- [[TestInboundPipelineOnGetUpdates]] - `method` [EXTRACTED]
- [[_make_update()]] - `calls` [EXTRACTED]
- [[_wrap_response()]] - `calls` [EXTRACTED]
- [[asyncio_21]] - `references` [EXTRACTED]
- [[fake_urlopen()_30]] - `contains` [EXTRACTED]
- [[fake_urlopen()_62]] - `indirect_call` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/_wrap_response
