---
type: community
cohesion: 0.11
members: 24
---

# test_key_rotation_internals.py

**Cohesion:** 0.11 - loosely connected
**Members:** 24 nodes

## Members
- [[dot-test_emergency_disabled_trigger_rejected()]] - code - gateway/tests/test_key_rotation_internals.py
- [[dot-test_generate_returns_typed_token()]] - code - gateway/tests/test_key_rotation_internals.py
- [[dot-test_get_all_credentials_status_lists_registered()]] - code - gateway/tests/test_key_rotation_internals.py
- [[dot-test_get_credential_status_none_for_unknown()]] - code - gateway/tests/test_key_rotation_internals.py
- [[dot-test_health_score_empty_is_perfect()]] - code - gateway/tests/test_key_rotation_internals.py
- [[dot-test_in_progress_is_rejected()]] - code - gateway/tests/test_key_rotation_internals.py
- [[dot-test_max_attempts_exceeded_is_rejected()]] - code - gateway/tests/test_key_rotation_internals.py
- [[dot-test_retire_clears_old_reference_when_grace_expired()]] - code - gateway/tests/test_key_rotation_internals.py
- [[dot-test_retire_noop_when_no_grace_period()]] - code - gateway/tests/test_key_rotation_internals.py
- [[dot-test_scheduled_rotation_disabled_short_circuits()]] - code - gateway/tests/test_key_rotation_internals.py
- [[dot-test_store_failure_marks_failed()]] - code - gateway/tests/test_key_rotation_internals.py
- [[dot-test_unknown_credential_returns_error()]] - code - gateway/tests/test_key_rotation_internals.py
- [[dot-test_validate_with_validator_that_raises_fails_closed()]] - code - gateway/tests/test_key_rotation_internals.py
- [[dot-test_validate_without_registered_validator_passes()]] - code - gateway/tests/test_key_rotation_internals.py
- [[TestCheckAndRotateDisabled]] - code - gateway/tests/test_key_rotation_internals.py
- [[TestEmergencyAndRetire]] - code - gateway/tests/test_key_rotation_internals.py
- [[TestGenerateAndValidate]] - code - gateway/tests/test_key_rotation_internals.py
- [[TestRotateGuardBranches]] - code - gateway/tests/test_key_rotation_internals.py
- [[TestStatusHelpers]] - code - gateway/tests/test_key_rotation_internals.py
- [[_old_cred()]] - code - gateway/tests/test_key_rotation_internals.py
- [[key_rotation.py (KeyRotationManager)]] - code - gateway/security/key_rotation.py
- [[key_rotation_config.py (KeyRotationConfig)]] - code - gateway/security/key_rotation_config.py
- [[manager()_3]] - code - gateway/tests/test_key_rotation_internals.py
- [[test_key_rotation_internals.py]] - code - gateway/tests/test_key_rotation_internals.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_key_rotation_internalspy
SORT file.name ASC
```

## Connections to other communities
- 20 edges to [[_COMMUNITY_A2AMethod]]
- 8 edges to [[_COMMUNITY_CredentialInfo]]
- 7 edges to [[_COMMUNITY_TestNormalizeForSpeech]]
- 1 edge to [[_COMMUNITY_AgentShroud Documentation (2)]]
- 1 edge to [[_COMMUNITY_GSDL-715 (silent regression incident)]]

## Top bridge nodes
- [[test_key_rotation_internals.py]] - degree 17, connects to 5 communities
- [[TestRotateGuardBranches]] - degree 11, connects to 3 communities
- [[TestEmergencyAndRetire]] - degree 9, connects to 3 communities
- [[TestGenerateAndValidate]] - degree 9, connects to 3 communities
- [[TestStatusHelpers]] - degree 9, connects to 3 communities
