---
type: community
members: 37
---

# CredentialInfo

**Members:** 37 nodes

## Members
- [[dot-age_days()]] - code - gateway/security/key_rotation.py
- [[dot-is_in_grace_period()]] - code - gateway/security/key_rotation.py
- [[dot-manager()_2]] - code - gateway/tests/test_key_rotation.py
- [[dot-sample_credential()]] - code - gateway/tests/test_key_rotation.py
- [[dot-setup_manager_with_credential()]] - code - gateway/tests/test_key_rotation.py
- [[dot-should_rotate()]] - code - gateway/security/key_rotation.py
- [[dot-should_warn()]] - code - gateway/security/key_rotation.py
- [[dot-test_age_calculation()]] - code - gateway/tests/test_key_rotation.py
- [[dot-test_get_credential_status()]] - code - gateway/tests/test_key_rotation.py
- [[dot-test_get_health_score_all_healthy()]] - code - gateway/tests/test_key_rotation.py
- [[dot-test_get_health_score_mixed_states()]] - code - gateway/tests/test_key_rotation.py
- [[dot-test_grace_period_tracking()]] - code - gateway/tests/test_key_rotation.py
- [[dot-test_register_credential()]] - code - gateway/tests/test_key_rotation.py
- [[dot-test_should_rotate()]] - code - gateway/tests/test_key_rotation.py
- [[dot-test_should_warn()]] - code - gateway/tests/test_key_rotation.py
- [[Age of credential in days.]] - rationale - gateway/security/key_rotation.py
- [[Create a manager with test configuration.]] - rationale - gateway/tests/test_key_rotation.py
- [[Create a sample credential for testing.]] - rationale - gateway/tests/test_key_rotation.py
- [[CredentialInfo]] - code - gateway/security/key_rotation.py
- [[Information about a managed credential.]] - rationale - gateway/security/key_rotation.py
- [[Set up manager with a credential that needs rotation.]] - rationale - gateway/tests/test_key_rotation.py
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
- [[Whether credential age warrants a warning.]] - rationale - gateway/security/key_rotation.py
- [[Whether credential is currently in grace period.]] - rationale - gateway/security/key_rotation.py
- [[Whether credential needs rotation based on age.]] - rationale - gateway/security/key_rotation.py
- [[fixture_143]] - code

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/CredentialInfo
SORT file.name ASC
```

## Connections to other communities
- 12 edges to [[_COMMUNITY_KeyRotationConfig]]
- 8 edges to [[_COMMUNITY_test_key_rotation.py]]
- 4 edges to [[_COMMUNITY_KeyRotationManager]]
- 3 edges to [[_COMMUNITY_asyncio_4]]

## Top bridge nodes
- [[CredentialInfo]] - degree 25, connects to 4 communities
- [[TestKeyRotationManager]] - degree 13, connects to 3 communities
- [[dot-setup_manager_with_credential()]] - degree 7, connects to 3 communities
- [[TestCredentialInfo]] - degree 8, connects to 2 communities
- [[dot-manager()_2]] - degree 5, connects to 2 communities
