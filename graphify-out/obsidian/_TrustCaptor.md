---
source_file: "gateway/tests/test_forward_routing.py"
type: "code"
community: "AgentTarget (3)"
location: "L394"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/AgentTarget_3
---

# _TrustCaptor

## Connections
- [[dot-__init__()_54]] - `method` [EXTRACTED]
- [[dot-process_inbound()_5]] - `method` [EXTRACTED]
- [[dot-process_outbound()_3]] - `method` [EXTRACTED]
- [[dot-test_empty_user_id_does_not_elevate_trust()]] - `calls` [EXTRACTED]
- [[dot-test_no_user_id_does_not_elevate_trust()]] - `calls` [EXTRACTED]
- [[dot-test_non_owner_user_id_does_not_elevate_trust()]] - `calls` [EXTRACTED]
- [[dot-test_owner_id_without_trusted_header_does_not_elevate_trust()]] - `calls` [EXTRACTED]
- [[dot-test_owner_user_id_elevates_trust_to_full()]] - `calls` [EXTRACTED]
- [[AgentTarget_2]] - `uses` [INFERRED]
- [[ForwardRequest]] - `uses` [INFERRED]
- [[Pipeline mock that records the user_trust_level passed to process_outbound.]] - `rationale_for` [EXTRACTED]
- [[_make_trust_app_state()]] - `references` [EXTRACTED]
- [[test_forward_routing.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/AgentTarget_3
