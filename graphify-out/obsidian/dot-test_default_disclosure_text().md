---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "code"
community: "full_access collaborators must pass through middleware and secondary pipeline…"
location: "L9618"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/full_access_collaborators_must_pass_through_middleware_and_secondary_pipeline
---

# .test_default_disclosure_text()

## Connections
- [[FakeRBAC]] - `calls` [EXTRACTED]
- [[TestFullAccessMiddlewareBypass]] - `method` [EXTRACTED]
- [[asyncio]] - `references` [EXTRACTED]
- [[fake_send_text()]] - `contains` [EXTRACTED]
- [[fake_send_text()_1]] - `indirect_call` [INFERRED]
- [[local_only collaborator must receive the restricted-scope disclosure message.]] - `rationale_for` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/full_access_collaborators_must_pass_through_middleware_and_secondary_pipeline
