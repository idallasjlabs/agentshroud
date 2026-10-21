---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "code"
community: "ApprovalQueueConfig (2)"
location: "L3914"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/ApprovalQueueConfig_2
---

# .test_send_telegram_text_honors_retry_after_on_http_429()

## Connections
- [[PassthroughPipeline]] - `calls` [EXTRACTED]
- [[TestInboundPipelineOnGetUpdates]] - `method` [EXTRACTED]
- [[_send_telegram_text should honor Telegram retry_after when rate limited.]] - `rationale_for` [EXTRACTED]
- [[asyncio_3]] - `references` [EXTRACTED]
- [[fake_sleep()]] - `indirect_call` [INFERRED]
- [[fake_urlopen()_67]] - `contains` [EXTRACTED]
- [[fake_urlopen()_25]] - `indirect_call` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/ApprovalQueueConfig_2
