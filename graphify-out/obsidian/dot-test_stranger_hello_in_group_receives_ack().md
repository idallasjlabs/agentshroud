---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "code"
community: "SecurityPipeline"
location: "L9362"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/SecurityPipeline
---

# .test_stranger_hello_in_group_receives_ack()

## Connections
- [[dot-_make_proxy()_1]] - `calls` [EXTRACTED]
- [[A stranger (not owner, not collaborator) typing 'hello' in a group still gets…]] - `rationale_for` [EXTRACTED]
- [[TestGroupPresenceProbe]] - `method` [EXTRACTED]
- [[_make_group_update()]] - `calls` [EXTRACTED]
- [[_wrap_response()]] - `calls` [EXTRACTED]
- [[asyncio_3]] - `references` [EXTRACTED]
- [[fake_send()_10]] - `contains` [EXTRACTED]
- [[fake_send()_11]] - `indirect_call` [INFERRED]
- [[noop_owner_notice()]] - `indirect_call` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/SecurityPipeline
