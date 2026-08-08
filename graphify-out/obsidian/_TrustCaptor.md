---
source_file: "gateway/tests/test_forward_routing.py"
type: "code"
community: "Gateway Test Suite"
location: "L394"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Gateway_Test_Suite
---

# _TrustCaptor

## Connections
- [[.__init__()_146]] - `method` [EXTRACTED]
- [[.process_inbound()_5]] - `method` [EXTRACTED]
- [[.process_outbound()_6]] - `method` [EXTRACTED]
- [[.test_empty_user_id_does_not_elevate_trust()]] - `calls` [EXTRACTED]
- [[.test_no_user_id_does_not_elevate_trust()]] - `calls` [EXTRACTED]
- [[.test_non_owner_user_id_does_not_elevate_trust()]] - `calls` [EXTRACTED]
- [[.test_owner_id_without_trusted_header_does_not_elevate_trust()]] - `calls` [EXTRACTED]
- [[.test_owner_user_id_elevates_trust_to_full()]] - `calls` [EXTRACTED]
- [[AgentTarget]] - `uses` [INFERRED]
- [[ForwardRequest]] - `uses` [INFERRED]
- [[Pipeline mock that records the user_trust_level passed to process_outbound.]] - `rationale_for` [EXTRACTED]
- [[_make_trust_app_state()]] - `references` [EXTRACTED]
- [[test_forward_routing.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Gateway_Test_Suite