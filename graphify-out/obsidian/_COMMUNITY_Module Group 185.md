---
type: community
cohesion: 0.09
members: 26
---

# Module Group 185

**Cohesion:** 0.09 - loosely connected
**Members:** 26 nodes

## Members
- [[.age_days()]] - code - gateway/security/key_rotation.py
- [[.is_in_grace_period()]] - code - gateway/security/key_rotation.py
- [[.manager()]] - code - gateway/tests/test_key_rotation.py
- [[.sample_credential()]] - code - gateway/tests/test_key_rotation.py
- [[.test_age_calculation()]] - code - gateway/tests/test_key_rotation.py
- [[.test_get_credential_status()]] - code - gateway/tests/test_key_rotation.py
- [[.test_get_health_score_all_healthy()]] - code - gateway/tests/test_key_rotation.py
- [[.test_get_health_score_mixed_states()]] - code - gateway/tests/test_key_rotation.py
- [[.test_grace_period_tracking()]] - code - gateway/tests/test_key_rotation.py
- [[.test_register_credential()]] - code - gateway/tests/test_key_rotation.py
- [[.test_should_rotate()]] - code - gateway/tests/test_key_rotation.py
- [[Age of credential in days.]] - rationale - gateway/security/key_rotation.py
- [[Create a manager with test configuration.]] - rationale - gateway/tests/test_key_rotation.py
- [[Create a sample credential for testing.]] - rationale - gateway/tests/test_key_rotation.py
- [[CredentialInfo]] - code - gateway/security/key_rotation.py
- [[Information about a managed credential.]] - rationale - gateway/security/key_rotation.py
- [[Test credential age calculation.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test credential registration.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test credential status reporting.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test grace period status tracking.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test health score calculation with all healthy credentials.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test health score with mixed credential states.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test key rotation manager functionality.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test rotation requirement calculation.]] - rationale - gateway/tests/test_key_rotation.py
- [[TestKeyRotationManager]] - code - gateway/tests/test_key_rotation.py
- [[Whether credential is currently in grace period.]] - rationale - gateway/security/key_rotation.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_185
SORT file.name ASC
```

## Connections to other communities
- 18 edges to [[_COMMUNITY_Module Group 93]]
- 5 edges to [[_COMMUNITY_Module Group 108]]
- 5 edges to [[_COMMUNITY_Module Group 223]]

## Top bridge nodes
- [[CredentialInfo]] - degree 25, connects to 3 communities
- [[TestKeyRotationManager]] - degree 15, connects to 3 communities
- [[.manager()]] - degree 4, connects to 2 communities
- [[.test_should_rotate()]] - degree 4, connects to 1 community
- [[.test_age_calculation()]] - degree 3, connects to 1 community
