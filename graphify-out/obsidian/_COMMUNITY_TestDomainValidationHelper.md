---
type: community
cohesion: 0.08
members: 31
---

# TestDomainValidationHelper

**Cohesion:** 0.08 - loosely connected
**Members:** 31 nodes

## Members
- [[dot-age_days()]] - code - gateway/security/key_rotation.py
- [[dot-is_in_grace_period()]] - code - gateway/security/key_rotation.py
- [[dot-manager()_1]] - code - gateway/tests/test_key_rotation.py
- [[dot-sample_credential()]] - code - gateway/tests/test_key_rotation.py
- [[dot-test_age_calculation()]] - code - gateway/tests/test_key_rotation.py
- [[dot-test_get_credential_status()]] - code - gateway/tests/test_key_rotation.py
- [[dot-test_get_health_score_all_healthy()]] - code - gateway/tests/test_key_rotation.py
- [[dot-test_get_health_score_mixed_states()]] - code - gateway/tests/test_key_rotation.py
- [[dot-test_grace_period_tracking()]] - code - gateway/tests/test_key_rotation.py
- [[dot-test_not_due_without_force_is_rejected()]] - code - gateway/tests/test_key_rotation_internals.py
- [[dot-test_register_credential()]] - code - gateway/tests/test_key_rotation.py
- [[dot-test_should_rotate()]] - code - gateway/tests/test_key_rotation.py
- [[dot-test_should_warn()]] - code - gateway/tests/test_key_rotation.py
- [[Age of credential in days.]] - rationale - gateway/security/key_rotation.py
- [[Create a manager with test configuration.]] - rationale - gateway/tests/test_key_rotation.py
- [[Create a sample credential for testing.]] - rationale - gateway/tests/test_key_rotation.py
- [[CredentialInfo]] - code - gateway/security/key_rotation.py
- [[Information about a managed credential.]] - rationale - gateway/security/key_rotation.py
- [[Test credential age calculation.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test credential information tracking.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test credential registration.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test credential status reporting.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test grace period status tracking.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test health score calculation with all healthy credentials.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test health score with mixed credential states.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test key rotation manager functionality.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test rotation requirement calculation.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test warning threshold calculation.]] - rationale - gateway/tests/test_key_rotation.py
- [[TestCredentialInfo]] - code - gateway/tests/test_key_rotation.py
- [[TestKeyRotationManager]] - code - gateway/tests/test_key_rotation.py
- [[Whether credential is currently in grace period.]] - rationale - gateway/security/key_rotation.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestDomainValidationHelper
SORT file.name ASC
```

## Connections to other communities
- 14 edges to [[_COMMUNITY_KeyRotationManager]]
- 11 edges to [[_COMMUNITY_UserSessionManager_4]]
- 6 edges to [[_COMMUNITY_KeyRotationManager_1]]
- 5 edges to [[_COMMUNITY_gatewayteststest_llm_proxy_thinking_suppression.py (8 cases)]]
- 4 edges to [[_COMMUNITY_Restart Procedure_1]]

## Top bridge nodes
- [[CredentialInfo]] - degree 35, connects to 5 communities
- [[TestKeyRotationManager]] - degree 15, connects to 5 communities
- [[TestCredentialInfo]] - degree 12, connects to 4 communities
- [[dot-manager()_1]] - degree 4, connects to 2 communities
- [[dot-test_should_rotate()]] - degree 4, connects to 1 community
