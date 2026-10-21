---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "code"
community: "SecurityPipeline"
location: "L8371"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/SecurityPipeline
---

# .test_suspended_drop_notice_respects_cooldown()

## Connections
- [[dot-_make_proxy()_1]] - `calls` [EXTRACTED]
- [[AsyncMock]] - `calls` [EXTRACTED]
- [[Second dropped message within cooldown window must NOT produce another notice.]] - `rationale_for` [EXTRACTED]
- [[TestProgressiveLockdownUX]] - `method` [EXTRACTED]
- [[_make_update()]] - `calls` [EXTRACTED]
- [[_wrap_response()]] - `calls` [EXTRACTED]
- [[asyncio_3]] - `references` [EXTRACTED]
- [[fake_send()_19]] - `contains` [EXTRACTED]
- [[fake_send()_11]] - `indirect_call` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/SecurityPipeline
