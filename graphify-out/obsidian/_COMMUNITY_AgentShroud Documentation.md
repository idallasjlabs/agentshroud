---
type: community
members: 31
---

# AgentShroud Documentation

**Members:** 31 nodes

## Members
- [[dot-age_days()]] - code - gateway/security/key_rotation.py
- [[dot-is_in_grace_period()]] - code - gateway/security/key_rotation.py
- [[dot-test_age_calculation()]] - code - gateway/tests/test_key_rotation.py
- [[dot-test_emergency_disabled_trigger_rejected()]] - code - gateway/tests/test_key_rotation_internals.py
- [[dot-test_get_all_credentials_status_lists_registered()]] - code - gateway/tests/test_key_rotation_internals.py
- [[dot-test_get_credential_status_none_for_unknown()]] - code - gateway/tests/test_key_rotation_internals.py
- [[dot-test_grace_period_tracking()]] - code - gateway/tests/test_key_rotation.py
- [[dot-test_health_score_empty_is_perfect()]] - code - gateway/tests/test_key_rotation_internals.py
- [[dot-test_in_progress_is_rejected()]] - code - gateway/tests/test_key_rotation_internals.py
- [[dot-test_max_attempts_exceeded_is_rejected()]] - code - gateway/tests/test_key_rotation_internals.py
- [[dot-test_not_due_without_force_is_rejected()]] - code - gateway/tests/test_key_rotation_internals.py
- [[dot-test_retire_clears_old_reference_when_grace_expired()]] - code - gateway/tests/test_key_rotation_internals.py
- [[dot-test_retire_noop_when_no_grace_period()]] - code - gateway/tests/test_key_rotation_internals.py
- [[dot-test_scheduled_rotation_disabled_short_circuits()]] - code - gateway/tests/test_key_rotation_internals.py
- [[dot-test_store_failure_marks_failed()]] - code - gateway/tests/test_key_rotation_internals.py
- [[dot-test_unknown_credential_returns_error()]] - code - gateway/tests/test_key_rotation_internals.py
- [[Age of credential in days.]] - rationale - gateway/security/key_rotation.py
- [[CredentialInfo]] - code - gateway/security/key_rotation.py
- [[Information about a managed credential.]] - rationale - gateway/security/key_rotation.py
- [[Test credential age calculation.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test grace period status tracking.]] - rationale - gateway/tests/test_key_rotation.py
- [[TestCheckAndRotateDisabled]] - code - gateway/tests/test_key_rotation_internals.py
- [[TestEmergencyAndRetire]] - code - gateway/tests/test_key_rotation_internals.py
- [[TestRotateGuardBranches]] - code - gateway/tests/test_key_rotation_internals.py
- [[TestStatusHelpers]] - code - gateway/tests/test_key_rotation_internals.py
- [[Whether credential is currently in grace period.]] - rationale - gateway/security/key_rotation.py
- [[_old_cred()]] - code - gateway/tests/test_key_rotation_internals.py
- [[key_rotation.py (KeyRotationManager)]] - code - gateway/security/key_rotation.py
- [[key_rotation_config.py (KeyRotationConfig)]] - code - gateway/security/key_rotation_config.py
- [[manager()_1]] - code - gateway/tests/test_key_rotation_internals.py
- [[test_key_rotation_internals.py]] - code - gateway/tests/test_key_rotation_internals.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/AgentShroud_Documentation
SORT file.name ASC
```

## Connections to other communities
- 28 edges to [[_COMMUNITY_A2AMethod]]
- 9 edges to [[_COMMUNITY_TestNormalizeForSpeech]]
- 4 edges to [[_COMMUNITY_FODL — Fluence Operational Data Lakehouse]]
- 4 edges to [[_COMMUNITY_env_guard.py]]
- 2 edges to [[_COMMUNITY_AgentShroud Documentation (2)]]
- 2 edges to [[_COMMUNITY_GSDL-715 (silent regression incident)]]
- 2 edges to [[_COMMUNITY_AgentShroud Documentation (3)]]

## Top bridge nodes
- [[CredentialInfo]] - degree 35, connects to 7 communities
- [[test_key_rotation_internals.py]] - degree 17, connects to 5 communities
- [[TestRotateGuardBranches]] - degree 11, connects to 2 communities
- [[TestEmergencyAndRetire]] - degree 9, connects to 2 communities
- [[TestStatusHelpers]] - degree 9, connects to 2 communities
