---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "code"
community: "test_telegram_proxy_inbound.py"
location: "L9298"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/test_telegram_proxy_inboundpy
---

# .test_dm_hello_does_not_trigger_probe()

## Connections
- [[dot-_make_proxy()_1]] - `calls` [EXTRACTED]
- [[TestGroupPresenceProbe]] - `method` [EXTRACTED]
- [[The probe is group-only; 'hello' in a DM chat must not fire the ack.]] - `rationale_for` [EXTRACTED]
- [[_make_update()]] - `calls` [EXTRACTED]
- [[_wrap_response()]] - `calls` [EXTRACTED]
- [[asyncio]] - `references` [EXTRACTED]
- [[fake_send()_1]] - `contains` [EXTRACTED]
- [[fake_send()_7]] - `indirect_call` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/test_telegram_proxy_inboundpy
