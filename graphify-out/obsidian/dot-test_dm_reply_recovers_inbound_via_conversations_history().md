---
source_file: "gateway/tests/test_slack_proxy_coverage.py"
type: "code"
community: "AsyncMock"
location: "L188"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/AsyncMock
---

# .test_dm_reply_recovers_inbound_via_conversations_history()

## Connections
- [[AsyncMock]] - `calls` [INFERRED]
- [[Non-thread reply → conversations.history lookup; bot and subtype messages are…]] - `rationale_for` [EXTRACTED]
- [[TestOutboundTracking]] - `method` [EXTRACTED]
- [[_make_proxy()]] - `calls` [EXTRACTED]
- [[asyncio_5]] - `references` [EXTRACTED]
- [[fake_api()]] - `contains` [EXTRACTED]
- [[fake_api()_3]] - `indirect_call` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/AsyncMock
