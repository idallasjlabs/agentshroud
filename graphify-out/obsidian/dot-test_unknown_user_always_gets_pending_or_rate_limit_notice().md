---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "code"
community: ".test_unknown_user_always_gets_pending_or_rate_limit_notice()"
location: "L7992"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/test_unknown_user_always_gets_pending_or_rate_limit_notice
---

# .test_unknown_user_always_gets_pending_or_rate_limit_notice()

## Connections
- [[FakeRBAC]] - `calls` [EXTRACTED]
- [[PassthroughPipeline]] - `calls` [EXTRACTED]
- [[TestNoResponseGuarantee]] - `method` [EXTRACTED]
- [[Unknown users must always receive either a pending notice or a rate-limit…]] - `rationale_for` [EXTRACTED]
- [[_make_update()]] - `calls` [EXTRACTED]
- [[_wrap_response()]] - `calls` [EXTRACTED]
- [[asyncio_3]] - `references` [EXTRACTED]
- [[fake_owner_notice()_21]] - `contains` [EXTRACTED]
- [[fake_owner_notice()_4]] - `indirect_call` [INFERRED]
- [[fake_send()_24]] - `contains` [EXTRACTED]
- [[fake_send()_11]] - `indirect_call` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/test_unknown_user_always_gets_pending_or_rate_limit_notice
