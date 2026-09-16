---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "code"
community: "Community 119"
location: "L3757"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Community_119
---

# .test_collaborator_rate_limit_notice_is_sent_for_each_limited_message()

## Connections
- [[FakeRBAC]] - `calls` [EXTRACTED]
- [[PassthroughPipeline]] - `calls` [EXTRACTED]
- [[RateLimiter]] - `calls` [EXTRACTED]
- [[Repeated rate-limited messages should each receive a deterministic notice.]] - `rationale_for` [EXTRACTED]
- [[TelegramAPIProxy]] - `calls` [EXTRACTED]
- [[TestInboundPipelineOnGetUpdates]] - `method` [EXTRACTED]
- [[_make_update()_1]] - `calls` [EXTRACTED]
- [[_wrap_response()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Community_119