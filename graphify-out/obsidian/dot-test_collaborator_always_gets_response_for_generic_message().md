---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "code"
community: "Every collaborator message must produce a response — never a silent drop."
location: "L7949"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Every_collaborator_message_must_produce_a_response__never_a_silent_drop
---

# .test_collaborator_always_gets_response_for_generic_message()

## Connections
- [[Even a generic message triggers _send_collaborator_safe_info_response…]] - `rationale_for` [EXTRACTED]
- [[FakeRBAC]] - `calls` [EXTRACTED]
- [[PassthroughPipeline]] - `calls` [EXTRACTED]
- [[TestNoResponseGuarantee]] - `method` [EXTRACTED]
- [[_make_update()]] - `calls` [EXTRACTED]
- [[_wrap_response()]] - `calls` [EXTRACTED]
- [[asyncio]] - `references` [EXTRACTED]
- [[fake_send()_22]] - `contains` [EXTRACTED]
- [[fake_send()_7]] - `indirect_call` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/Every_collaborator_message_must_produce_a_response__never_a_silent_drop
