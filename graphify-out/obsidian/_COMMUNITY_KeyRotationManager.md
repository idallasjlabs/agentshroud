---
type: community
members: 120
---

# KeyRotationManager

**Members:** 120 nodes

## Members
- [[dot-__init__()_18]] - code - gateway/security/key_rotation.py
- [[dot-__init__()_19]] - code - gateway/tests/test_key_rotation.py
- [[dot-_read_credential_from_1password()]] - code - gateway/security/key_rotation.py
- [[dot-add_custom_policy()]] - code - gateway/security/key_rotation_config.py
- [[dot-age_days()]] - code - gateway/security/key_rotation.py
- [[dot-get_op_reference()]] - code - gateway/security/key_rotation_config.py
- [[dot-get_policy()]] - code - gateway/security/key_rotation_config.py
- [[dot-is_emergency_trigger_enabled()]] - code - gateway/security/key_rotation_config.py
- [[dot-is_in_grace_period()]] - code - gateway/security/key_rotation.py
- [[dot-manager()]] - code - gateway/tests/test_key_rotation.py
- [[dot-register_credential()]] - code - gateway/security/key_rotation.py
- [[dot-register_validator()]] - code - gateway/security/key_rotation.py
- [[dot-sample_credential()]] - code - gateway/tests/test_key_rotation.py
- [[dot-setup_manager_with_credential()]] - code - gateway/tests/test_key_rotation.py
- [[dot-should_rotate()]] - code - gateway/security/key_rotation.py
- [[dot-should_warn()]] - code - gateway/security/key_rotation.py
- [[dot-test_add_custom_policy()]] - code - gateway/tests/test_key_rotation.py
- [[dot-test_age_calculation()]] - code - gateway/tests/test_key_rotation.py
- [[dot-test_check_and_rotate_due_credentials()]] - code - gateway/tests/test_key_rotation.py
- [[dot-test_default_config_has_common_policies()]] - code - gateway/tests/test_key_rotation.py
- [[dot-test_default_policy_values()]] - code - gateway/tests/test_key_rotation.py
- [[dot-test_emergency_rotation()]] - code - gateway/tests/test_key_rotation.py
- [[dot-test_get_credential_status()]] - code - gateway/tests/test_key_rotation.py
- [[dot-test_get_health_score_all_healthy()]] - code - gateway/tests/test_key_rotation.py
- [[dot-test_get_health_score_mixed_states()]] - code - gateway/tests/test_key_rotation.py
- [[dot-test_get_op_reference_builds_correctly()]] - code - gateway/tests/test_key_rotation.py
- [[dot-test_get_policy_returns_default_for_unknown_type()]] - code - gateway/tests/test_key_rotation.py
- [[dot-test_grace_period_cleanup()]] - code - gateway/tests/test_key_rotation.py
- [[dot-test_grace_period_tracking()]] - code - gateway/tests/test_key_rotation.py
- [[dot-test_register_credential()]] - code - gateway/tests/test_key_rotation.py
- [[dot-test_register_validator()]] - code - gateway/tests/test_key_rotation.py
- [[dot-test_rotation_with_validation_failure()]] - code - gateway/tests/test_key_rotation.py
- [[dot-test_should_rotate()]] - code - gateway/tests/test_key_rotation.py
- [[dot-test_should_warn()]] - code - gateway/tests/test_key_rotation.py
- [[dot-test_successful_rotation_workflow()]] - code - gateway/tests/test_key_rotation.py
- [[dot-validate()]] - code - gateway/tests/test_key_rotation.py
- [[Add or update a rotation policy for a specific credential type.]] - rationale - gateway/security/key_rotation_config.py
- [[Age of credential in days.]] - rationale - gateway/security/key_rotation.py
- [[Base class for credential validators.]] - rationale - gateway/security/key_rotation.py
- [[Behavior tests for KeyRotationManager internals and guard branches. The…]] - rationale - gateway/tests/test_key_rotation_internals.py
- [[Build a complete op reference for a credential.]] - rationale - gateway/security/key_rotation_config.py
- [[Check if a specific emergency trigger is enabled.]] - rationale - gateway/security/key_rotation_config.py
- [[Configuration for key rotation policies and schedules.]] - rationale - gateway/security/key_rotation_config.py
- [[Create a manager with test configuration.]] - rationale - gateway/tests/test_key_rotation.py
- [[Create a sample credential for testing.]] - rationale - gateway/tests/test_key_rotation.py
- [[CredentialInfo]] - code - gateway/security/key_rotation.py
- [[CredentialRotationPolicy]] - code - gateway/security/key_rotation_config.py
- [[CredentialValidator]] - code - gateway/security/key_rotation.py
- [[Enum_11]] - code
- [[Get overall credential health score and status summary.]] - rationale - gateway/web/management.py
- [[Get rotation policy for a credential type, falling back to api_key default.]] - rationale - gateway/security/key_rotation_config.py
- [[Get status of all managed credentials including age and rotation schedule.]] - rationale - gateway/web/management.py
- [[Information about a managed credential.]] - rationale - gateway/security/key_rotation.py
- [[Initialize the key rotation manager.]] - rationale - gateway/security/key_rotation.py
- [[KeyRotationConfig]] - code - gateway/security/key_rotation_config.py
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
- [[Test the managecredentialshealth endpoint.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test the managecredentialsstatus endpoint.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test the POST managecredentialsrotate{credential_id} endpoint.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test the complete rotation workflow.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test validator registration.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test warning threshold calculation.]] - rationale - gateway/tests/test_key_rotation.py
- [[TestCredentialInfo]] - code - gateway/tests/test_key_rotation.py
- [[TestCredentialRotationPolicy]] - code - gateway/tests/test_key_rotation.py
- [[TestKeyRotationConfig]] - code - gateway/tests/test_key_rotation.py
- [[TestKeyRotationManager]] - code - gateway/tests/test_key_rotation.py
- [[TestKeyRotationWorkflow]] - code - gateway/tests/test_key_rotation.py
- [[Tests for automated key rotation (R-22)]] - rationale - gateway/tests/test_key_rotation.py
- [[Trigger manual rotation for a specific credential (owner only).]] - rationale - gateway/web/management.py
- [[Whether credential age warrants a warning.]] - rationale - gateway/security/key_rotation.py
- [[Whether credential is currently in grace period.]] - rationale - gateway/security/key_rotation.py
- [[Whether credential needs rotation based on age.]] - rationale - gateway/security/key_rotation.py
- [[asyncio_8]] - code
- [[credentials_health()]] - code - gateway/web/management.py
- [[credentials_status()]] - code - gateway/web/management.py
- [[datetime_1]] - code
- [[fixture_13]] - code
- [[fixture_14]] - code
- [[key_rotation.py]] - code - gateway/security/key_rotation.py
- [[key_rotation_config.py]] - code - gateway/security/key_rotation_config.py
- [[manager()]] - code - gateway/tests/test_key_rotation_internals.py
- [[post_1]] - code
- [[rotate_credential()]] - code - gateway/web/management.py
- [[test_credentials_health_endpoint()]] - code - gateway/tests/test_key_rotation.py
- [[test_credentials_status_endpoint()]] - code - gateway/tests/test_key_rotation.py
- [[test_key_rotation.py]] - code - gateway/tests/test_key_rotation.py
- [[test_key_rotation_internals.py]] - code - gateway/tests/test_key_rotation_internals.py
- [[test_rotate_credential_endpoint()]] - code - gateway/tests/test_key_rotation.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/KeyRotationManager
SORT file.name ASC
```

## Connections to other communities
- 13 edges to [[_COMMUNITY_asyncio_4]]
- 13 edges to [[_COMMUNITY_Any_1]]
- 7 edges to [[_COMMUNITY_EgressFilter]]
- 4 edges to [[_COMMUNITY_middleware.py]]
- 1 edge to [[_COMMUNITY_MiddlewareManager]]
- 1 edge to [[_COMMUNITY_test_web_api_coverage.py]]

## Top bridge nodes
- [[KeyRotationManager]] - degree 33, connects to 4 communities
- [[CredentialValidator]] - degree 8, connects to 2 communities
- [[KeyRotationConfig]] - degree 26, connects to 1 community
- [[CredentialInfo]] - degree 25, connects to 1 community
- [[test_key_rotation.py]] - degree 20, connects to 1 community
