---
source_file: "gateway/tests/test_privacy_policy.py"
type: "code"
community: "PrivacyPolicyEnforcer"
location: "L110"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/PrivacyPolicyEnforcer
---

# TestServiceAccessControl

## Connections
- [[dot-test_admin_blocked_from_private_service()]] - `method` [EXTRACTED]
- [[dot-test_collaborator_allowed_shared_service()]] - `method` [EXTRACTED]
- [[dot-test_collaborator_blocked_from_private_service()]] - `method` [EXTRACTED]
- [[dot-test_group_member_allowed_group_only_service()]] - `method` [EXTRACTED]
- [[dot-test_non_group_member_blocked_from_group_only_service()]] - `method` [EXTRACTED]
- [[dot-test_owner_can_access_private_service()]] - `method` [EXTRACTED]
- [[dot-test_unknown_service_allowed_by_default()]] - `method` [EXTRACTED]
- [[PrivacyPolicy]] - `uses` [INFERRED]
- [[PrivacyPolicyEnforcer]] - `uses` [INFERRED]
- [[RBACConfig_1]] - `uses` [INFERRED]
- [[Role_96]] - `uses` [INFERRED]
- [[ServicePrivacy]] - `uses` [INFERRED]
- [[TeamsConfig]] - `uses` [INFERRED]
- [[test_privacy_policy.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/PrivacyPolicyEnforcer
