---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "code"
community: "RateLimiter"
location: "L3690"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/RateLimiter
---

# .test_collaborator_rate_limit_notice_includes_retry_window()

## Connections
- [[FakeRBAC]] - `calls` [EXTRACTED]
- [[PassthroughPipeline]] - `calls` [EXTRACTED]
- [[Rate-limited collaborators should receive a deterministic retry-window notice.]] - `rationale_for` [EXTRACTED]
- [[RateLimiter]] - `calls` [EXTRACTED]
- [[TestInboundPipelineOnGetUpdates]] - `method` [EXTRACTED]
- [[_make_update()]] - `calls` [EXTRACTED]
- [[_wrap_response()]] - `calls` [EXTRACTED]
- [[asyncio_19]] - `references` [EXTRACTED]
- [[fake_urlopen()_21]] - `contains` [EXTRACTED]
- [[fake_urlopen()_48]] - `indirect_call` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/RateLimiter
