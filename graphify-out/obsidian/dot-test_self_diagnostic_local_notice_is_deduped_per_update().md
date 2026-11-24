---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "code"
community: "_make_update"
location: "L5363"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/_make_update
---

# .test_self_diagnostic_local_notice_is_deduped_per_update()

## Connections
- [[FakeRBAC]] - `calls` [EXTRACTED]
- [[PassthroughPipeline]] - `calls` [EXTRACTED]
- [[Self-diagnostic local handler should dedupe repeated delivery of same update_id.]] - `rationale_for` [EXTRACTED]
- [[TestInboundPipelineOnGetUpdates]] - `method` [EXTRACTED]
- [[_make_update()]] - `calls` [EXTRACTED]
- [[_wrap_response()]] - `calls` [EXTRACTED]
- [[asyncio_22]] - `references` [EXTRACTED]
- [[fake_urlopen()_79]] - `contains` [EXTRACTED]
- [[fake_urlopen()_51]] - `indirect_call` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/_make_update
