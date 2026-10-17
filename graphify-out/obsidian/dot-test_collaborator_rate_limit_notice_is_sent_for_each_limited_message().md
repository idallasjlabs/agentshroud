---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "code"
community: "Rate-limit notice path should key retry window by user_id, not chat_id."
location: "L3775"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Rate-limit_notice_path_should_key_retry_window_by_user_id_not_chat_id
---

# .test_collaborator_rate_limit_notice_is_sent_for_each_limited_message()

## Connections
- [[FakeRBAC]] - `calls` [EXTRACTED]
- [[PassthroughPipeline]] - `calls` [EXTRACTED]
- [[Repeated rate-limited messages should each receive a deterministic notice.]] - `rationale_for` [EXTRACTED]
- [[TestInboundPipelineOnGetUpdates]] - `method` [EXTRACTED]
- [[_make_update()]] - `calls` [EXTRACTED]
- [[_wrap_response()]] - `calls` [EXTRACTED]
- [[asyncio]] - `references` [EXTRACTED]
- [[fake_rate_notice()]] - `contains` [EXTRACTED]
- [[fake_rate_notice()_2]] - `indirect_call` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/Rate-limit_notice_path_should_key_retry_window_by_user_id_not_chat_id
