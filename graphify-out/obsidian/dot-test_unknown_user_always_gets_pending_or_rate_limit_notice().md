---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "code"
community: "Every collaborator message must produce a response — never a silent drop."
location: "L7992"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Every_collaborator_message_must_produce_a_response__never_a_silent_drop
---

# .test_unknown_user_always_gets_pending_or_rate_limit_notice()

## Connections
- [[FakeRBAC]] - `calls` [EXTRACTED]
- [[PassthroughPipeline]] - `calls` [EXTRACTED]
- [[TestNoResponseGuarantee]] - `method` [EXTRACTED]
- [[Unknown users must always receive either a pending notice or a rate-limit…]] - `rationale_for` [EXTRACTED]
- [[_make_update()]] - `calls` [EXTRACTED]
- [[_wrap_response()]] - `calls` [EXTRACTED]
- [[asyncio]] - `references` [EXTRACTED]
- [[fake_owner_notice()_21]] - `contains` [EXTRACTED]
- [[fake_owner_notice()_4]] - `indirect_call` [INFERRED]
- [[fake_send()_24]] - `contains` [EXTRACTED]
- [[fake_send()_7]] - `indirect_call` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/Every_collaborator_message_must_produce_a_response__never_a_silent_drop
