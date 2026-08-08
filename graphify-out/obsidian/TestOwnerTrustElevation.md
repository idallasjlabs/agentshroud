---
source_file: "gateway/tests/test_forward_routing.py"
type: "code"
community: "Gateway Test Suite"
location: "L470"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Gateway_Test_Suite
---

# TestOwnerTrustElevation

## Connections
- [[._post_forward()]] - `method` [EXTRACTED]
- [[.test_empty_user_id_does_not_elevate_trust()]] - `method` [EXTRACTED]
- [[.test_no_user_id_does_not_elevate_trust()]] - `method` [EXTRACTED]
- [[.test_non_owner_user_id_does_not_elevate_trust()]] - `method` [EXTRACTED]
- [[.test_owner_id_without_trusted_header_does_not_elevate_trust()]] - `method` [EXTRACTED]
- [[.test_owner_user_id_elevates_trust_to_full()]] - `method` [EXTRACTED]
- [[AgentTarget]] - `uses` [INFERRED]
- [[ForwardRequest]] - `uses` [INFERRED]
- [[SCRUM-46 verify forward.py elevates trust to FULL for the owner's user_id.]] - `rationale_for` [EXTRACTED]
- [[test_forward_routing.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Gateway_Test_Suite