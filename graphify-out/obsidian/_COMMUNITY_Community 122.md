---
type: community
members: 143
---

# Community 122

**Members:** 143 nodes

## Members
- [[.__init__()_103]] - code - gateway/security/key_rotation.py
- [[.__init__()_190]] - code - gateway/tests/test_key_rotation.py
- [[._read_credential_from_1password()]] - code - gateway/security/key_rotation.py
- [[.add_custom_policy()]] - code - gateway/security/key_rotation_config.py
- [[.age_days()]] - code - gateway/security/key_rotation.py
- [[.get_op_reference()]] - code - gateway/security/key_rotation_config.py
- [[.get_policy()_1]] - code - gateway/security/key_rotation_config.py
- [[.is_emergency_trigger_enabled()]] - code - gateway/security/key_rotation_config.py
- [[.is_in_grace_period()]] - code - gateway/security/key_rotation.py
- [[.manager()]] - code - gateway/tests/test_key_rotation.py
- [[.register_credential()]] - code - gateway/security/key_rotation.py
- [[.register_validator()]] - code - gateway/security/key_rotation.py
- [[.sample_credential()]] - code - gateway/tests/test_key_rotation.py
- [[.setup_manager_with_credential()]] - code - gateway/tests/test_key_rotation.py
- [[.should_warn()]] - code - gateway/security/key_rotation.py
- [[.test_add_custom_policy()]] - code - gateway/tests/test_key_rotation.py
- [[.test_age_calculation()]] - code - gateway/tests/test_key_rotation.py
- [[.test_check_and_rotate_due_credentials()]] - code - gateway/tests/test_key_rotation.py
- [[.test_default_config_has_common_policies()]] - code - gateway/tests/test_key_rotation.py
- [[.test_default_policy_values()]] - code - gateway/tests/test_key_rotation.py
- [[.test_emergency_disabled_trigger_rejected()]] - code - gateway/tests/test_key_rotation_internals.py
- [[.test_emergency_rotation()]] - code - gateway/tests/test_key_rotation.py
- [[.test_generate_returns_typed_token()]] - code - gateway/tests/test_key_rotation_internals.py
- [[.test_get_all_credentials_status_lists_registered()]] - code - gateway/tests/test_key_rotation_internals.py
- [[.test_get_credential_status()]] - code - gateway/tests/test_key_rotation.py
- [[.test_get_credential_status_none_for_unknown()]] - code - gateway/tests/test_key_rotation_internals.py
- [[.test_get_health_score_all_healthy()]] - code - gateway/tests/test_key_rotation.py
- [[.test_get_health_score_mixed_states()]] - code - gateway/tests/test_key_rotation.py
- [[.test_get_op_reference_builds_correctly()]] - code - gateway/tests/test_key_rotation.py
- [[.test_get_policy_returns_default_for_unknown_type()]] - code - gateway/tests/test_key_rotation.py
- [[.test_grace_period_cleanup()]] - code - gateway/tests/test_key_rotation.py
- [[.test_grace_period_tracking()]] - code - gateway/tests/test_key_rotation.py
- [[.test_health_score_empty_is_perfect()]] - code - gateway/tests/test_key_rotation_internals.py
- [[.test_in_progress_is_rejected()]] - code - gateway/tests/test_key_rotation_internals.py
- [[.test_max_attempts_exceeded_is_rejected()]] - code - gateway/tests/test_key_rotation_internals.py
- [[.test_not_due_without_force_is_rejected()]] - code - gateway/tests/test_key_rotation_internals.py
- [[.test_read_generic_exception_yields_none()]] - code - gateway/tests/test_key_rotation_internals.py
- [[.test_read_nonzero_returncode_yields_none()]] - code - gateway/tests/test_key_rotation_internals.py
- [[.test_read_success_strips_whitespace()]] - code - gateway/tests/test_key_rotation_internals.py
- [[.test_read_timeout_yields_none()]] - code - gateway/tests/test_key_rotation_internals.py
- [[.test_register_credential()]] - code - gateway/tests/test_key_rotation.py
- [[.test_register_validator()]] - code - gateway/tests/test_key_rotation.py
- [[.test_retire_clears_old_reference_when_grace_expired()]] - code - gateway/tests/test_key_rotation_internals.py
- [[.test_retire_noop_when_no_grace_period()]] - code - gateway/tests/test_key_rotation_internals.py
- [[.test_rotation_with_validation_failure()]] - code - gateway/tests/test_key_rotation.py
- [[.test_scheduled_rotation_disabled_short_circuits()]] - code - gateway/tests/test_key_rotation_internals.py
- [[.test_should_rotate()]] - code - gateway/tests/test_key_rotation.py
- [[.test_should_warn()]] - code - gateway/tests/test_key_rotation.py
- [[.test_store_failure_marks_failed()]] - code - gateway/tests/test_key_rotation_internals.py
- [[.test_store_nonzero_returncode_is_false()]] - code - gateway/tests/test_key_rotation_internals.py
- [[.test_store_rejects_malformed_reference()]] - code - gateway/tests/test_key_rotation_internals.py
- [[.test_store_success()]] - code - gateway/tests/test_key_rotation_internals.py
- [[.test_store_timeout_is_false()]] - code - gateway/tests/test_key_rotation_internals.py
- [[.test_successful_rotation_workflow()]] - code - gateway/tests/test_key_rotation.py
- [[.test_unknown_credential_returns_error()]] - code - gateway/tests/test_key_rotation_internals.py
- [[.test_validate_with_validator_that_raises_fails_closed()]] - code - gateway/tests/test_key_rotation_internals.py
- [[.test_validate_without_registered_validator_passes()]] - code - gateway/tests/test_key_rotation_internals.py
- [[.validate()_2]] - code - gateway/tests/test_key_rotation.py
- [[Add or update a rotation policy for a specific credential type.]] - rationale - gateway/security/key_rotation_config.py
- [[Age of credential in days.]] - rationale - gateway/security/key_rotation.py
- [[Base class for credential validators.]] - rationale - gateway/security/key_rotation.py
- [[Build a complete op reference for a credential.]] - rationale - gateway/security/key_rotation_config.py
- [[Check if a specific emergency trigger is enabled.]] - rationale - gateway/security/key_rotation_config.py
- [[Configuration for key rotation policies and schedules.]] - rationale - gateway/security/key_rotation_config.py
- [[Create a manager with test configuration.]] - rationale - gateway/tests/test_key_rotation.py
- [[Create a sample credential for testing.]] - rationale - gateway/tests/test_key_rotation.py
- [[CredentialInfo]] - code - gateway/security/key_rotation.py
- [[CredentialRotationPolicy]] - code - gateway/security/key_rotation.py
- [[CredentialRotationPolicy_1]] - code - gateway/security/key_rotation_config.py
- [[CredentialValidator]] - code - gateway/security/key_rotation.py
- [[Get overall credential health score and status summary.]] - rationale - gateway/web/management.py
- [[Get rotation policy for a credential type, falling back to api_key default.]] - rationale - gateway/security/key_rotation_config.py
- [[Get status of all managed credentials including age and rotation schedule.]] - rationale - gateway/web/management.py
- [[Information about a managed credential.]] - rationale - gateway/security/key_rotation.py
- [[Initialize the key rotation manager.]] - rationale - gateway/security/key_rotation.py
- [[KeyRotationConfig]] - code - gateway/security/key_rotation.py
- [[KeyRotationConfig_1]] - code - gateway/security/key_rotation_config.py
- [[KeyRotationManager]] - code - gateway/security/key_rotation.py
- [[Manages automated rotation of credentials with zero downtime.]] - rationale - gateway/security/key_rotation.py
- [[Mock validation that can be controlled.]] - rationale - gateway/tests/test_key_rotation.py
- [[Mock validator for testing.]] - rationale - gateway/tests/test_key_rotation.py
- [[MockValidator]] - code - gateway/tests/test_key_rotation.py
- [[Register a credential for rotation management.]] - rationale - gateway/security/key_rotation.py
- [[Register a validator for a credential type.]] - rationale - gateway/security/key_rotation.py
- [[Rotation policy for a specific credential type.]] - rationale - gateway/security/key_rotation_config.py
- [[RotationStatus]] - code - gateway/security/key_rotation.py
- [[Safely read a credential from 1Password using op CLI.]] - rationale - gateway/security/key_rotation.py
- [[Set up manager with a credential that needs rotation.]] - rationale - gateway/tests/test_key_rotation.py
- [[Status of a credential rotation.]] - rationale - gateway/security/key_rotation.py
- [[Test Gmail Credential Retrieval]] - code - gateway/tests/test_gmail_credential_retrieval.py
- [[Test adding custom policy for new credential type.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test bulk rotation check and execution.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test complete successful rotation workflow.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test credential age calculation.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test credential information tracking.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test credential registration.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test credential rotation policy configuration.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test credential status reporting.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test default config includes policies for common credential types.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test default policy has reasonable values.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test emergency rotation workflow.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test get_policy falls back to api_key for unknown types.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test grace period and old credential cleanup.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test grace period status tracking.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test health score calculation with all healthy credentials.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test health score with mixed credential states.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test key rotation configuration.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test key rotation manager functionality.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test op reference building.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test rotation requirement calculation.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test rotation workflow with validation failure and rollback.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test the POST managecredentialsrotate{credential_id} endpoint.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test the complete rotation workflow.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test validator registration.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test warning threshold calculation.]] - rationale - gateway/tests/test_key_rotation.py
- [[TestCheckAndRotateDisabled]] - code - gateway/tests/test_key_rotation_internals.py
- [[TestCredentialInfo]] - code - gateway/tests/test_key_rotation.py
- [[TestCredentialRotationPolicy]] - code - gateway/tests/test_key_rotation.py
- [[TestEmergencyAndRetire]] - code - gateway/tests/test_key_rotation_internals.py
- [[TestGenerateAndValidate]] - code - gateway/tests/test_key_rotation_internals.py
- [[TestKeyRotationConfig]] - code - gateway/tests/test_key_rotation.py
- [[TestKeyRotationManager]] - code - gateway/tests/test_key_rotation.py
- [[TestKeyRotationWorkflow]] - code - gateway/tests/test_key_rotation.py
- [[TestReadFrom1Password]] - code - gateway/tests/test_key_rotation_internals.py
- [[TestRotateGuardBranches]] - code - gateway/tests/test_key_rotation_internals.py
- [[TestStatusHelpers]] - code - gateway/tests/test_key_rotation_internals.py
- [[TestStoreIn1Password]] - code - gateway/tests/test_key_rotation_internals.py
- [[Trigger manual rotation for a specific credential (owner only).]] - rationale - gateway/web/management.py
- [[Whether credential age warrants a warning.]] - rationale - gateway/security/key_rotation.py
- [[Whether credential is currently in grace period.]] - rationale - gateway/security/key_rotation.py
- [[_old_cred()]] - code - gateway/tests/test_key_rotation_internals.py
- [[credentials_health()]] - code - gateway/web/management.py
- [[credentials_status()]] - code - gateway/web/management.py
- [[datetime_5]] - code - gateway/security/key_rotation.py
- [[key_rotation.py]] - code - gateway/security/key_rotation.py
- [[key_rotation.py (KeyRotationManager)]] - code - gateway/security/key_rotation.py
- [[key_rotation_config.py]] - code - gateway/security/key_rotation_config.py
- [[key_rotation_config.py (KeyRotationConfig)]] - code - gateway/security/key_rotation_config.py
- [[manager()_2]] - code - gateway/tests/test_key_rotation_internals.py
- [[rotate_credential()]] - code - gateway/web/management.py
- [[test_key_rotation.py]] - code - gateway/tests/test_key_rotation.py
- [[test_key_rotation_internals.py]] - code - gateway/tests/test_key_rotation_internals.py
- [[test_rotate_credential_endpoint()]] - code - gateway/tests/test_key_rotation.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_122
SORT file.name ASC
```

## Connections to other communities
- 20 edges to [[_COMMUNITY_Community 198]]
- 10 edges to [[_COMMUNITY_Community 72]]
- 9 edges to [[_COMMUNITY_Community 166]]
- 2 edges to [[_COMMUNITY_Community 8]]
- 2 edges to [[_COMMUNITY_Community 1991]]
- 1 edge to [[_COMMUNITY_Community 84]]
- 1 edge to [[_COMMUNITY_Community 1]]
- 1 edge to [[_COMMUNITY_Community 1214]]
- 1 edge to [[_COMMUNITY_Community 73]]
- 1 edge to [[_COMMUNITY_Community 10]]
- 1 edge to [[_COMMUNITY_Community 40]]

## Top bridge nodes
- [[KeyRotationManager]] - degree 55, connects to 4 communities
- [[key_rotation.py]] - degree 12, connects to 4 communities
- [[KeyRotationConfig_1]] - degree 44, connects to 2 communities
- [[test_key_rotation.py]] - degree 18, connects to 2 communities
- [[rotate_credential()]] - degree 5, connects to 2 communities