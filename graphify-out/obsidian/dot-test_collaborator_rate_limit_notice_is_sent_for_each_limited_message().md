---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "code"
community: "RateLimiter"
location: "L3757"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/RateLimiter
---

# .test_collaborator_rate_limit_notice_is_sent_for_each_limited_message()

## Connections
- [[FakeRBAC]] - `calls` [EXTRACTED]
- [[PassthroughPipeline]] - `calls` [EXTRACTED]
- [[RateLimiter_1]] - `calls` [EXTRACTED]
- [[Repeated rate-limited messages should each receive a deterministic notice.]] - `rationale_for` [EXTRACTED]
- [[TelegramAPIProxy_1]] - `calls` [EXTRACTED]
- [[TestInboundPipelineOnGetUpdates]] - `method` [EXTRACTED]
- [[_make_update()]] - `calls` [EXTRACTED]
- [[_wrap_response()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/RateLimiter
