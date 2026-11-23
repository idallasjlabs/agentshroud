---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "code"
community: ".test_collaborator_rate_limit_notice_includes_retry_window"
location: "L3690"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/test_collaborator_rate_limit_notice_includes_retry_window
---

# .test_collaborator_rate_limit_notice_includes_retry_window()

## Connections
- [[FakeRBAC]] - `calls` [EXTRACTED]
- [[PassthroughPipeline]] - `calls` [EXTRACTED]
- [[Rate-limited collaborators should receive a deterministic retry-window notice.]] - `rationale_for` [EXTRACTED]
- [[RateLimiter_1]] - `calls` [EXTRACTED]
- [[TestInboundPipelineOnGetUpdates]] - `method` [EXTRACTED]
- [[_make_update()]] - `calls` [EXTRACTED]
- [[_wrap_response()]] - `calls` [EXTRACTED]
- [[asyncio_21]] - `references` [EXTRACTED]
- [[fake_urlopen()_36]] - `contains` [EXTRACTED]
- [[fake_urlopen()_62]] - `indirect_call` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/test_collaborator_rate_limit_notice_includes_retry_window
