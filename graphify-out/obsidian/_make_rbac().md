---
source_file: "gateway/tests/test_privacy_policy.py"
type: "code"
community: "PrivacyPolicyEnforcer"
location: "L26"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/PrivacyPolicyEnforcer
---

# _make_rbac()

## Connections
- [[dot-test_collaborator_allowed_shared_service()]] - `calls` [EXTRACTED]
- [[dot-test_group_member_allowed_group_only_service()]] - `calls` [EXTRACTED]
- [[dot-test_non_group_member_blocked_from_group_only_service()]] - `calls` [EXTRACTED]
- [[RBACConfig]] - `calls` [EXTRACTED]
- [[Role]] - `uses` [INFERRED]
- [[TeamsConfig]] - `calls` [EXTRACTED]
- [[rbac()]] - `calls` [EXTRACTED]
- [[test_privacy_policy.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/PrivacyPolicyEnforcer
