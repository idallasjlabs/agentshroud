---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "code"
community: "Community 119"
location: "L3803"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Community_119
---

# .test_collaborator_rate_limit_notice_retries_next_message_when_send_fails()

## Connections
- [[FakeRBAC]] - `calls` [EXTRACTED]
- [[If notice send fails, cooldown should not suppress the next retry attempt.]] - `rationale_for` [EXTRACTED]
- [[PassthroughPipeline]] - `calls` [EXTRACTED]
- [[RateLimiter]] - `calls` [EXTRACTED]
- [[TelegramAPIProxy]] - `calls` [EXTRACTED]
- [[TestInboundPipelineOnGetUpdates]] - `method` [EXTRACTED]
- [[_make_update()_1]] - `calls` [EXTRACTED]
- [[_wrap_response()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Community_119