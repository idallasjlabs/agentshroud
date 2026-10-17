---
type: community
members: 44
---

# KeyRotationManager

**Members:** 44 nodes

## Members
- [[dot-__init__()_56]] - code - gateway/security/key_rotation.py
- [[dot-_read_credential_from_1password()]] - code - gateway/security/key_rotation.py
- [[dot-register_validator()]] - code - gateway/security/key_rotation.py
- [[dot-test_emergency_disabled_trigger_rejected()]] - code - gateway/tests/test_key_rotation_internals.py
- [[dot-test_generate_returns_typed_token()]] - code - gateway/tests/test_key_rotation_internals.py
- [[dot-test_get_all_credentials_status_lists_registered()]] - code - gateway/tests/test_key_rotation_internals.py
- [[dot-test_get_credential_status_none_for_unknown()]] - code - gateway/tests/test_key_rotation_internals.py
- [[dot-test_health_score_empty_is_perfect()]] - code - gateway/tests/test_key_rotation_internals.py
- [[dot-test_in_progress_is_rejected()]] - code - gateway/tests/test_key_rotation_internals.py
- [[dot-test_max_attempts_exceeded_is_rejected()]] - code - gateway/tests/test_key_rotation_internals.py
- [[dot-test_not_due_without_force_is_rejected()]] - code - gateway/tests/test_key_rotation_internals.py
- [[dot-test_read_generic_exception_yields_none()]] - code - gateway/tests/test_key_rotation_internals.py
- [[dot-test_read_nonzero_returncode_yields_none()]] - code - gateway/tests/test_key_rotation_internals.py
- [[dot-test_read_success_strips_whitespace()]] - code - gateway/tests/test_key_rotation_internals.py
- [[dot-test_read_timeout_yields_none()]] - code - gateway/tests/test_key_rotation_internals.py
- [[dot-test_retire_clears_old_reference_when_grace_expired()]] - code - gateway/tests/test_key_rotation_internals.py
- [[dot-test_retire_noop_when_no_grace_period()]] - code - gateway/tests/test_key_rotation_internals.py
- [[dot-test_scheduled_rotation_disabled_short_circuits()]] - code - gateway/tests/test_key_rotation_internals.py
- [[dot-test_store_failure_marks_failed()]] - code - gateway/tests/test_key_rotation_internals.py
- [[dot-test_store_nonzero_returncode_is_false()]] - code - gateway/tests/test_key_rotation_internals.py
- [[dot-test_store_rejects_malformed_reference()]] - code - gateway/tests/test_key_rotation_internals.py
- [[dot-test_store_success()]] - code - gateway/tests/test_key_rotation_internals.py
- [[dot-test_store_timeout_is_false()]] - code - gateway/tests/test_key_rotation_internals.py
- [[dot-test_unknown_credential_returns_error()]] - code - gateway/tests/test_key_rotation_internals.py
- [[dot-test_validate_with_validator_that_raises_fails_closed()]] - code - gateway/tests/test_key_rotation_internals.py
- [[dot-test_validate_without_registered_validator_passes()]] - code - gateway/tests/test_key_rotation_internals.py
- [[Initialize the key rotation manager.]] - rationale - gateway/security/key_rotation.py
- [[KeyRotationConfig]] - code - gateway/security/key_rotation.py
- [[KeyRotationManager]] - code - gateway/security/key_rotation.py
- [[Manages automated rotation of credentials with zero downtime.]] - rationale - gateway/security/key_rotation.py
- [[Register a validator for a credential type.]] - rationale - gateway/security/key_rotation.py
- [[Safely read a credential from 1Password using op CLI.]] - rationale - gateway/security/key_rotation.py
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
- [[manager()]] - code - gateway/tests/test_key_rotation_internals.py
- [[test_key_rotation_internals.py]] - code - gateway/tests/test_key_rotation_internals.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/KeyRotationManager
SORT file.name ASC
```

## Connections to other communities
- 52 edges to [[_COMMUNITY_UserSessionManager]]
- 12 edges to [[_COMMUNITY_KeyRotationManager (2)]]
- 11 edges to [[_COMMUNITY_AlertDispatcher]]
- 6 edges to [[_COMMUNITY_TestSSRFDetection (2)]]

## Top bridge nodes
- [[KeyRotationManager]] - degree 55, connects to 4 communities
- [[test_key_rotation_internals.py]] - degree 17, connects to 1 community
- [[TestRotateGuardBranches]] - degree 11, connects to 1 community
- [[TestReadFrom1Password]] - degree 10, connects to 1 community
- [[TestStoreIn1Password]] - degree 10, connects to 1 community
