---
type: community
members: 76
---

# UserSessionManager

**Members:** 76 nodes

## Members
- [[dot-__init__()_154]] - code - gateway/tests/test_key_rotation.py
- [[dot-add_custom_policy()]] - code - gateway/security/key_rotation_config.py
- [[dot-get_op_reference()]] - code - gateway/security/key_rotation_config.py
- [[dot-get_policy()]] - code - gateway/security/key_rotation_config.py
- [[dot-is_emergency_trigger_enabled()]] - code - gateway/security/key_rotation_config.py
- [[dot-manager()_2]] - code - gateway/tests/test_key_rotation.py
- [[dot-sample_credential()]] - code - gateway/tests/test_key_rotation.py
- [[dot-setup_manager_with_credential()]] - code - gateway/tests/test_key_rotation.py
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
- [[dot-test_grace_period_tracking()]] - code - gateway/tests/test_key_rotation.py
- [[dot-test_register_validator()]] - code - gateway/tests/test_key_rotation.py
- [[dot-test_rotation_with_validation_failure()]] - code - gateway/tests/test_key_rotation.py
- [[dot-test_should_rotate()]] - code - gateway/tests/test_key_rotation.py
- [[dot-test_should_warn()]] - code - gateway/tests/test_key_rotation.py
- [[dot-test_successful_rotation_workflow()]] - code - gateway/tests/test_key_rotation.py
- [[Add or update a rotation policy for a specific credential type.]] - rationale - gateway/security/key_rotation_config.py
- [[Base class for credential validators.]] - rationale - gateway/security/key_rotation.py
- [[Build a complete op reference for a credential.]] - rationale - gateway/security/key_rotation_config.py
- [[Check if a specific emergency trigger is enabled.]] - rationale - gateway/security/key_rotation_config.py
- [[Configuration for key rotation policies and schedules.]] - rationale - gateway/security/key_rotation_config.py
- [[Create a manager with test configuration.]] - rationale - gateway/tests/test_key_rotation.py
- [[Create a sample credential for testing.]] - rationale - gateway/tests/test_key_rotation.py
- [[CredentialInfo]] - code - gateway/security/key_rotation.py
- [[CredentialRotationPolicy_1]] - code - gateway/security/key_rotation_config.py
- [[CredentialValidator]] - code - gateway/security/key_rotation.py
- [[Get rotation policy for a credential type, falling back to api_key default.]] - rationale - gateway/security/key_rotation_config.py
- [[Information about a managed credential.]] - rationale - gateway/security/key_rotation.py
- [[KeyRotationConfig_1]] - code - gateway/security/key_rotation_config.py
- [[Mock validator for testing.]] - rationale - gateway/tests/test_key_rotation.py
- [[MockValidator]] - code - gateway/tests/test_key_rotation.py
- [[Rotation policy for a specific credential type.]] - rationale - gateway/security/key_rotation_config.py
- [[RotationStatus]] - code - gateway/security/key_rotation.py
- [[Set up manager with a credential that needs rotation.]] - rationale - gateway/tests/test_key_rotation.py
- [[Status of a credential rotation.]] - rationale - gateway/security/key_rotation.py
- [[Test Gmail Credential Retrieval]] - code - gateway/tests/test_gmail_credential_retrieval.py
- [[Test adding custom policy for new credential type.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test bulk rotation check and execution.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test complete successful rotation workflow.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test credential age calculation.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test credential information tracking.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test credential rotation policy configuration.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test credential status reporting.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test default config includes policies for common credential types.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test default policy has reasonable values.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test emergency rotation workflow.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test get_policy falls back to api_key for unknown types.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test grace period status tracking.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test health score calculation with all healthy credentials.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test health score with mixed credential states.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test key rotation configuration.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test key rotation manager functionality.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test op reference building.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test rotation requirement calculation.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test rotation workflow with validation failure and rollback.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test the complete rotation workflow.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test validator registration.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test warning threshold calculation.]] - rationale - gateway/tests/test_key_rotation.py
- [[TestCredentialInfo]] - code - gateway/tests/test_key_rotation.py
- [[TestCredentialRotationPolicy]] - code - gateway/tests/test_key_rotation.py
- [[TestKeyRotationConfig]] - code - gateway/tests/test_key_rotation.py
- [[TestKeyRotationManager]] - code - gateway/tests/test_key_rotation.py
- [[TestKeyRotationWorkflow]] - code - gateway/tests/test_key_rotation.py
- [[datetime_4]] - code - gateway/security/key_rotation.py
- [[key_rotation.py]] - code - gateway/security/key_rotation.py
- [[key_rotation_config.py]] - code - gateway/security/key_rotation_config.py
- [[test_key_rotation.py]] - code - gateway/tests/test_key_rotation.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/UserSessionManager
SORT file.name ASC
```

## Connections to other communities
- 52 edges to [[_COMMUNITY_KeyRotationManager]]
- 9 edges to [[_COMMUNITY_KeyRotationManager (2)]]
- 6 edges to [[_COMMUNITY_TestSSRFDetection (2)]]
- 2 edges to [[_COMMUNITY_Restart Procedure (3)]]
- 2 edges to [[_COMMUNITY_TestToolChainAnalyzer]]
- 2 edges to [[_COMMUNITY_MiddlewareManager (2)]]
- 1 edge to [[_COMMUNITY_AlertDispatcher]]
- 1 edge to [[_COMMUNITY_TestDomainValidationHelper]]
- 1 edge to [[_COMMUNITY_TestDomainValidationHelper (2)]]
- 1 edge to [[_COMMUNITY_gatewayteststest_llm_proxy_thinking_suppression.py (8 cases)]]
- 1 edge to [[_COMMUNITY_TestDomainValidationHelper (3)]]
- 1 edge to [[_COMMUNITY_gatewayteststest_llm_proxy_thinking_suppression.py (8 cases) (2)]]
- 1 edge to [[_COMMUNITY_Restart Procedure (4)]]
- 1 edge to [[_COMMUNITY_ModeRequest]]
- 1 edge to [[_COMMUNITY_egress_filter.py (2)]]

## Top bridge nodes
- [[key_rotation.py]] - degree 13, connects to 5 communities
- [[CredentialInfo]] - degree 35, connects to 4 communities
- [[test_key_rotation.py]] - degree 18, connects to 4 communities
- [[KeyRotationConfig_1]] - degree 44, connects to 3 communities
- [[CredentialRotationPolicy_1]] - degree 24, connects to 2 communities
