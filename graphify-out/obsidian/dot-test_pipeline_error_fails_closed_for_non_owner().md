---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "code"
community: "_wrap_response()"
location: "L273"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/_wrap_response
---

# .test_pipeline_error_fails_closed_for_non_owner()

## Connections
- [[FakeRBAC]] - `calls` [EXTRACTED]
- [[If pipeline crashes, non-owner messages must be blocked (fail-closed).]] - `rationale_for` [EXTRACTED]
- [[TestInboundPipelineOnGetUpdates]] - `method` [EXTRACTED]
- [[_make_update()]] - `calls` [EXTRACTED]
- [[_wrap_response()]] - `calls` [EXTRACTED]
- [[asyncio_3]] - `references` [EXTRACTED]
- [[process_inbound()_1]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/_wrap_response
