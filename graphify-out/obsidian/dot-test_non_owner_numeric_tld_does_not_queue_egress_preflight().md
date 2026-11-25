---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "code"
community: "_wrap_response"
location: "L6349"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/_wrap_response
---

# .test_non_owner_numeric_tld_does_not_queue_egress_preflight()

## Connections
- [[Approval preflight should reject domains with non-alphabetic TLDs.]] - `rationale_for` [EXTRACTED]
- [[FakeRBAC]] - `calls` [EXTRACTED]
- [[PassthroughPipeline]] - `calls` [EXTRACTED]
- [[TestInboundPipelineOnGetUpdates]] - `method` [EXTRACTED]
- [[_make_update()]] - `calls` [EXTRACTED]
- [[_wrap_response()]] - `calls` [EXTRACTED]
- [[asyncio_19]] - `references` [EXTRACTED]
- [[check_async()_15]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/_wrap_response
