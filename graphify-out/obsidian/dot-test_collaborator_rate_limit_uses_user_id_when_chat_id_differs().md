---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "code"
community: "Rate-limit notice path should key retry window by user_id, not chat_id."
location: "L3738"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Rate-limit_notice_path_should_key_retry_window_by_user_id_not_chat_id
---

# .test_collaborator_rate_limit_uses_user_id_when_chat_id_differs()

## Connections
- [[FakeRBAC]] - `calls` [EXTRACTED]
- [[PassthroughPipeline]] - `calls` [EXTRACTED]
- [[Rate-limit notice path should key retry window by user_id, not chat_id.]] - `rationale_for` [EXTRACTED]
- [[TestInboundPipelineOnGetUpdates]] - `method` [EXTRACTED]
- [[_make_update()]] - `calls` [EXTRACTED]
- [[_wrap_response()]] - `calls` [EXTRACTED]
- [[asyncio]] - `references` [EXTRACTED]
- [[fake_rate_notice()_2]] - `indirect_call` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/Rate-limit_notice_path_should_key_retry_window_by_user_id_not_chat_id
