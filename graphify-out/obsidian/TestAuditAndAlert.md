---
source_file: "gateway/tests/test_privacy_policy.py"
type: "code"
community: "Privacy Policy"
location: "L153"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Privacy_Policy
---

# TestAuditAndAlert

## Connections
- [[.test_audit_disabled_globally()]] - `method` [EXTRACTED]
- [[.test_should_alert_non_owner()]] - `method` [EXTRACTED]
- [[.test_should_audit_private_service()]] - `method` [EXTRACTED]
- [[.test_should_not_alert_owner()]] - `method` [EXTRACTED]
- [[.test_should_not_audit_unknown_service()]] - `method` [EXTRACTED]
- [[PrivacyPolicy]] - `uses` [INFERRED]
- [[PrivacyPolicyEnforcer]] - `uses` [INFERRED]
- [[RBACConfig_1]] - `uses` [INFERRED]
- [[Role_1]] - `uses` [INFERRED]
- [[ServicePolicy]] - `uses` [INFERRED]
- [[ServicePrivacy]] - `uses` [INFERRED]
- [[TeamsConfig]] - `uses` [INFERRED]
- [[test_privacy_policy.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Privacy_Policy
