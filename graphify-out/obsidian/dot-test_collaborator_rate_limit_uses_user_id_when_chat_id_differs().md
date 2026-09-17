---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "code"
community: "Community 119"
location: "L3720"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Community_119
---

# .test_collaborator_rate_limit_uses_user_id_when_chat_id_differs()

## Connections
- [[FakeRBAC]] - `calls` [EXTRACTED]
- [[PassthroughPipeline]] - `calls` [EXTRACTED]
- [[Rate-limit notice path should key retry window by user_id, not chat_id.]] - `rationale_for` [EXTRACTED]
- [[RateLimiter]] - `calls` [EXTRACTED]
- [[TelegramAPIProxy]] - `calls` [EXTRACTED]
- [[TestInboundPipelineOnGetUpdates]] - `method` [EXTRACTED]
- [[_make_update()_1]] - `calls` [EXTRACTED]
- [[_wrap_response()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Community_119