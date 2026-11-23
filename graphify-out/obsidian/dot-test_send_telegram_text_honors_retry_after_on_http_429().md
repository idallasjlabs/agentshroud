---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "code"
community: "fake_urlopen"
location: "L3914"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/fake_urlopen
---

# .test_send_telegram_text_honors_retry_after_on_http_429()

## Connections
- [[PassthroughPipeline]] - `calls` [EXTRACTED]
- [[TestInboundPipelineOnGetUpdates]] - `method` [EXTRACTED]
- [[_send_telegram_text should honor Telegram retry_after when rate limited.]] - `rationale_for` [EXTRACTED]
- [[asyncio_21]] - `references` [EXTRACTED]
- [[fake_sleep()_2]] - `indirect_call` [INFERRED]
- [[fake_urlopen()_79]] - `contains` [EXTRACTED]
- [[fake_urlopen()_62]] - `indirect_call` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/fake_urlopen
