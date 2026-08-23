---
type: community
cohesion: 0.08
members: 36
---

# Key Rotation Internals

**Cohesion:** 0.08 - loosely connected
**Members:** 36 nodes

## Members
- [[.test_emergency_disabled_trigger_rejected()]] - code - gateway/tests/test_key_rotation_internals.py
- [[.test_generate_returns_typed_token()]] - code - gateway/tests/test_key_rotation_internals.py
- [[.test_get_all_credentials_status_lists_registered()]] - code - gateway/tests/test_key_rotation_internals.py
- [[.test_get_credential_status_none_for_unknown()]] - code - gateway/tests/test_key_rotation_internals.py
- [[.test_health_score_empty_is_perfect()]] - code - gateway/tests/test_key_rotation_internals.py
- [[.test_in_progress_is_rejected()]] - code - gateway/tests/test_key_rotation_internals.py
- [[.test_max_attempts_exceeded_is_rejected()]] - code - gateway/tests/test_key_rotation_internals.py
- [[.test_read_generic_exception_yields_none()]] - code - gateway/tests/test_key_rotation_internals.py
- [[.test_read_nonzero_returncode_yields_none()]] - code - gateway/tests/test_key_rotation_internals.py
- [[.test_read_success_strips_whitespace()]] - code - gateway/tests/test_key_rotation_internals.py
- [[.test_read_timeout_yields_none()]] - code - gateway/tests/test_key_rotation_internals.py
- [[.test_retire_clears_old_reference_when_grace_expired()]] - code - gateway/tests/test_key_rotation_internals.py
- [[.test_retire_noop_when_no_grace_period()]] - code - gateway/tests/test_key_rotation_internals.py
- [[.test_scheduled_rotation_disabled_short_circuits()]] - code - gateway/tests/test_key_rotation_internals.py
- [[.test_store_failure_marks_failed()]] - code - gateway/tests/test_key_rotation_internals.py
- [[.test_store_nonzero_returncode_is_false()]] - code - gateway/tests/test_key_rotation_internals.py
- [[.test_store_rejects_malformed_reference()]] - code - gateway/tests/test_key_rotation_internals.py
- [[.test_store_success()]] - code - gateway/tests/test_key_rotation_internals.py
- [[.test_store_timeout_is_false()]] - code - gateway/tests/test_key_rotation_internals.py
- [[.test_unknown_credential_returns_error()]] - code - gateway/tests/test_key_rotation_internals.py
- [[.test_validate_with_validator_that_raises_fails_closed()]] - code - gateway/tests/test_key_rotation_internals.py
- [[.test_validate_without_registered_validator_passes()]] - code - gateway/tests/test_key_rotation_internals.py
- [[Base class for credential validators.]] - rationale - gateway/security/key_rotation.py
- [[CredentialValidator]] - code - gateway/security/key_rotation.py
- [[TestCheckAndRotateDisabled]] - code - gateway/tests/test_key_rotation_internals.py
- [[TestEmergencyAndRetire]] - code - gateway/tests/test_key_rotation_internals.py
- [[TestGenerateAndValidate]] - code - gateway/tests/test_key_rotation_internals.py
- [[TestReadFrom1Password]] - code - gateway/tests/test_key_rotation_internals.py
- [[TestRotateGuardBranches]] - code - gateway/tests/test_key_rotation_internals.py
- [[TestStatusHelpers]] - code - gateway/tests/test_key_rotation_internals.py
- [[TestStoreIn1Password]] - code - gateway/tests/test_key_rotation_internals.py
- [[_old_cred()]] - code - gateway/tests/test_key_rotation_internals.py
- [[key_rotation.py (KeyRotationManager)]] - code - gateway/security/key_rotation.py
- [[key_rotation_config.py (KeyRotationConfig)]] - code - gateway/security/key_rotation_config.py
- [[manager()_2]] - code - gateway/tests/test_key_rotation_internals.py
- [[test_key_rotation_internals.py]] - code - gateway/tests/test_key_rotation_internals.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Key_Rotation_Internals
SORT file.name ASC
```

## Connections to other communities
- 22 edges to [[_COMMUNITY_Key Rotation]]
- 12 edges to [[_COMMUNITY_Key Rotation]]
- 11 edges to [[_COMMUNITY_Key Rotation (security)]]
- 2 edges to [[_COMMUNITY_Key Rotation]]
- 2 edges to [[_COMMUNITY_Key Rotation]]

## Top bridge nodes
- [[CredentialValidator]] - degree 21, connects to 5 communities
- [[test_key_rotation_internals.py]] - degree 17, connects to 4 communities
- [[TestRotateGuardBranches]] - degree 11, connects to 3 communities
- [[TestReadFrom1Password]] - degree 10, connects to 3 communities
- [[TestStoreIn1Password]] - degree 10, connects to 3 communities