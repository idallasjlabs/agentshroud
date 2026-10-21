---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "code"
community: ".test_collaborator_rate_limit_notice_is_sent_for_each_limited_message()"
location: "L3821"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/test_collaborator_rate_limit_notice_is_sent_for_each_limited_message
---

# .test_collaborator_rate_limit_notice_retries_next_message_when_send_fails()

## Connections
- [[FakeRBAC]] - `calls` [EXTRACTED]
- [[If notice send fails, cooldown should not suppress the next retry attempt.]] - `rationale_for` [EXTRACTED]
- [[PassthroughPipeline]] - `calls` [EXTRACTED]
- [[TestInboundPipelineOnGetUpdates]] - `method` [EXTRACTED]
- [[_make_update()]] - `calls` [EXTRACTED]
- [[_wrap_response()]] - `calls` [EXTRACTED]
- [[asyncio_3]] - `references` [EXTRACTED]
- [[fake_rate_notice()_1]] - `contains` [EXTRACTED]
- [[fake_rate_notice()_2]] - `indirect_call` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/test_collaborator_rate_limit_notice_is_sent_for_each_limited_message
