---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "code"
community: "TestInboundPipelineOnGetUpdates"
location: "L3914"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/TestInboundPipelineOnGetUpdates
---

# .test_send_telegram_text_honors_retry_after_on_http_429()

## Connections
- [[PassthroughPipeline]] - `calls` [EXTRACTED]
- [[TestInboundPipelineOnGetUpdates]] - `method` [EXTRACTED]
- [[_send_telegram_text should honor Telegram retry_after when rate limited.]] - `rationale_for` [EXTRACTED]
- [[asyncio_3]] - `references` [EXTRACTED]
- [[fake_sleep()]] - `indirect_call` [INFERRED]
- [[fake_urlopen()_53]] - `contains` [EXTRACTED]
- [[fake_urlopen()_19]] - `indirect_call` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/TestInboundPipelineOnGetUpdates
