---
type: community
members: 17
---

# TestDomainValidationHelper

**Members:** 17 nodes

## Members
- [[dot-age_days()]] - code - gateway/security/key_rotation.py
- [[dot-is_in_grace_period()]] - code - gateway/security/key_rotation.py
- [[dot-test_age_calculation()]] - code - gateway/tests/test_key_rotation.py
- [[dot-test_grace_period_tracking()]] - code - gateway/tests/test_key_rotation.py
- [[dot-test_not_due_without_force_is_rejected()]] - code - gateway/tests/test_key_rotation_internals.py
- [[dot-test_should_rotate()]] - code - gateway/tests/test_key_rotation.py
- [[dot-test_should_warn()]] - code - gateway/tests/test_key_rotation.py
- [[Age of credential in days.]] - rationale - gateway/security/key_rotation.py
- [[CredentialInfo]] - code - gateway/security/key_rotation.py
- [[Information about a managed credential.]] - rationale - gateway/security/key_rotation.py
- [[Test credential age calculation.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test credential information tracking.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test grace period status tracking.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test rotation requirement calculation.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test warning threshold calculation.]] - rationale - gateway/tests/test_key_rotation.py
- [[TestCredentialInfo]] - code - gateway/tests/test_key_rotation.py
- [[Whether credential is currently in grace period.]] - rationale - gateway/security/key_rotation.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestDomainValidationHelper
SORT file.name ASC
```

## Connections to other communities
- 11 edges to [[_COMMUNITY_KeyRotationManager (2)]]
- 8 edges to [[_COMMUNITY_UserSessionManager (2)]]
- 4 edges to [[_COMMUNITY_KeyRotationManager]]
- 4 edges to [[_COMMUNITY_gatewayteststest_llm_proxy_thinking_suppression.py (8 cases)]]
- 4 edges to [[_COMMUNITY_TestDomainValidationHelper (2)]]
- 3 edges to [[_COMMUNITY_Restart Procedure]]
- 1 edge to [[_COMMUNITY_KeyRotationManager (3)]]

## Top bridge nodes
- [[CredentialInfo]] - degree 35, connects to 7 communities
- [[TestCredentialInfo]] - degree 12, connects to 4 communities
- [[dot-test_should_rotate()]] - degree 4, connects to 1 community
- [[dot-test_should_warn()]] - degree 4, connects to 1 community
- [[dot-test_not_due_without_force_is_rejected()]] - degree 2, connects to 1 community
