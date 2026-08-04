---
source_file: "gateway/security/privacy_policy.py"
type: "code"
community: "Privacy Policy"
location: "L178"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Privacy_Policy
---

# PrivacyPolicyEnforcer

## Connections
- [[.__init__()_85]] - `method` [EXTRACTED]
- [[._get_role_value()]] - `method` [EXTRACTED]
- [[._user_in_allowed_groups()]] - `method` [EXTRACTED]
- [[.contains_private_data()]] - `method` [EXTRACTED]
- [[.filter_response()_1]] - `method` [EXTRACTED]
- [[.is_service_allowed()]] - `method` [EXTRACTED]
- [[.should_alert()]] - `method` [EXTRACTED]
- [[.should_audit()]] - `method` [EXTRACTED]
- [[.test_audit_disabled_globally()]] - `calls` [EXTRACTED]
- [[.test_collaborator_allowed_shared_service()]] - `calls` [EXTRACTED]
- [[.test_extra_pattern_redacted()]] - `calls` [EXTRACTED]
- [[.test_group_member_allowed_group_only_service()]] - `calls` [EXTRACTED]
- [[.test_invalid_extra_pattern_does_not_crash()]] - `calls` [EXTRACTED]
- [[.test_non_group_member_blocked_from_group_only_service()]] - `calls` [EXTRACTED]
- [[Evaluates access control and filters responses per privacy policy.]] - `rationale_for` [EXTRACTED]
- [[RBACConfig_2]] - `uses` [INFERRED]
- [[RBACConfig_1]] - `uses` [INFERRED]
- [[TestAuditAndAlert]] - `uses` [INFERRED]
- [[TestPrivacyPolicyParsing]] - `uses` [INFERRED]
- [[TestResponseFiltering]] - `uses` [INFERRED]
- [[TestServiceAccessControl]] - `uses` [INFERRED]
- [[enforcer()_1]] - `calls` [EXTRACTED]
- [[lifespan()_1]] - `calls` [EXTRACTED]
- [[lifespan.py]] - `imports` [EXTRACTED]
- [[privacy_policy.py]] - `contains` [EXTRACTED]
- [[test_privacy_policy.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Privacy_Policy
