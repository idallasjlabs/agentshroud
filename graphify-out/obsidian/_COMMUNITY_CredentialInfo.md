---
type: community
cohesion: 0.10
members: 21
---

# CredentialInfo

**Cohesion:** 0.10 - loosely connected
**Members:** 21 nodes

## Members
- [[dot-age_days()]] - code - gateway/security/key_rotation.py
- [[dot-is_in_grace_period()]] - code - gateway/security/key_rotation.py
- [[dot-sample_credential()]] - code - gateway/tests/test_key_rotation.py
- [[dot-test_age_calculation()]] - code - gateway/tests/test_key_rotation.py
- [[dot-test_get_health_score_all_healthy()]] - code - gateway/tests/test_key_rotation.py
- [[dot-test_get_health_score_mixed_states()]] - code - gateway/tests/test_key_rotation.py
- [[dot-test_grace_period_tracking()]] - code - gateway/tests/test_key_rotation.py
- [[dot-test_not_due_without_force_is_rejected()]] - code - gateway/tests/test_key_rotation_internals.py
- [[dot-test_should_rotate()]] - code - gateway/tests/test_key_rotation.py
- [[dot-test_should_warn()]] - code - gateway/tests/test_key_rotation.py
- [[Age of credential in days.]] - rationale - gateway/security/key_rotation.py
- [[Create a sample credential for testing.]] - rationale - gateway/tests/test_key_rotation.py
- [[CredentialInfo]] - code - gateway/security/key_rotation.py
- [[Information about a managed credential.]] - rationale - gateway/security/key_rotation.py
- [[Test credential age calculation.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test grace period status tracking.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test health score calculation with all healthy credentials.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test health score with mixed credential states.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test rotation requirement calculation.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test warning threshold calculation.]] - rationale - gateway/tests/test_key_rotation.py
- [[Whether credential is currently in grace period.]] - rationale - gateway/security/key_rotation.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/CredentialInfo
SORT file.name ASC
```

## Connections to other communities
- 18 edges to [[_COMMUNITY_A2AMethod]]
- 8 edges to [[_COMMUNITY_test_key_rotation_internals.py]]
- 3 edges to [[_COMMUNITY_TestNormalizeForSpeech]]
- 3 edges to [[_COMMUNITY_env_guard.py]]
- 1 edge to [[_COMMUNITY_AgentShroud Documentation (2)]]
- 1 edge to [[_COMMUNITY_GSDL-715 (silent regression incident)]]

## Top bridge nodes
- [[CredentialInfo]] - degree 35, connects to 6 communities
- [[dot-test_should_rotate()]] - degree 4, connects to 1 community
- [[dot-test_should_warn()]] - degree 4, connects to 1 community
- [[dot-test_age_calculation()]] - degree 3, connects to 1 community
- [[dot-test_grace_period_tracking()]] - degree 3, connects to 1 community
