---
type: community
cohesion: 0.07
members: 54
---

# A2AMethod

**Cohesion:** 0.07 - loosely connected
**Members:** 54 nodes

## Members
- [[dot-add_custom_policy()]] - code - gateway/security/key_rotation_config.py
- [[dot-get_policy()]] - code - gateway/security/key_rotation_config.py
- [[dot-is_emergency_trigger_enabled()]] - code - gateway/security/key_rotation_config.py
- [[dot-manager()_1]] - code - gateway/tests/test_key_rotation.py
- [[dot-test_add_custom_policy()]] - code - gateway/tests/test_key_rotation.py
- [[dot-test_default_config_has_common_policies()]] - code - gateway/tests/test_key_rotation.py
- [[dot-test_default_policy_values()]] - code - gateway/tests/test_key_rotation.py
- [[dot-test_emergency_rotation()]] - code - gateway/tests/test_key_rotation.py
- [[dot-test_get_op_reference_builds_correctly()]] - code - gateway/tests/test_key_rotation.py
- [[dot-test_get_policy_returns_default_for_unknown_type()]] - code - gateway/tests/test_key_rotation.py
- [[dot-test_grace_period_cleanup()]] - code - gateway/tests/test_key_rotation.py
- [[dot-test_register_credential()]] - code - gateway/tests/test_key_rotation.py
- [[dot-test_successful_rotation_workflow()]] - code - gateway/tests/test_key_rotation.py
- [[Add or update a rotation policy for a specific credential type.]] - rationale - gateway/security/key_rotation_config.py
- [[Base class for credential validators.]] - rationale - gateway/security/key_rotation.py
- [[Check if a specific emergency trigger is enabled.]] - rationale - gateway/security/key_rotation_config.py
- [[Configuration for key rotation policies and schedules.]] - rationale - gateway/security/key_rotation_config.py
- [[Create a manager with test configuration.]] - rationale - gateway/tests/test_key_rotation.py
- [[CredentialRotationPolicy]] - code - gateway/security/key_rotation_config.py
- [[CredentialValidator]] - code - gateway/security/key_rotation.py
- [[Get rotation policy for a credential type, falling back to api_key default.]] - rationale - gateway/security/key_rotation_config.py
- [[KeyRotationConfig]] - code - gateway/security/key_rotation_config.py
- [[Rotation policy for a specific credential type.]] - rationale - gateway/security/key_rotation_config.py
- [[RotationStatus]] - code - gateway/security/key_rotation.py
- [[Status of a credential rotation.]] - rationale - gateway/security/key_rotation.py
- [[Test Gmail Credential Retrieval]] - code - gateway/tests/test_gmail_credential_retrieval.py
- [[Test adding custom policy for new credential type.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test complete successful rotation workflow.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test credential information tracking.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test credential registration.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test credential rotation policy configuration.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test default config includes policies for common credential types.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test default policy has reasonable values.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test emergency rotation workflow.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test get_policy falls back to api_key for unknown types.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test grace period and old credential cleanup.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test key rotation configuration.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test key rotation manager functionality.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test op reference building.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test the managecredentialsstatus endpoint.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test the POST managecredentialsrotate{credential_id} endpoint.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test the complete rotation workflow.]] - rationale - gateway/tests/test_key_rotation.py
- [[TestCredentialInfo]] - code - gateway/tests/test_key_rotation.py
- [[TestCredentialRotationPolicy]] - code - gateway/tests/test_key_rotation.py
- [[TestKeyRotationConfig]] - code - gateway/tests/test_key_rotation.py
- [[TestKeyRotationManager]] - code - gateway/tests/test_key_rotation.py
- [[TestKeyRotationWorkflow]] - code - gateway/tests/test_key_rotation.py
- [[datetime_2]] - code - gateway/security/key_rotation.py
- [[key_rotation.py]] - code - gateway/security/key_rotation.py
- [[key_rotation_config.py]] - code - gateway/security/key_rotation_config.py
- [[test_credentials_health_endpoint()]] - code - gateway/tests/test_key_rotation.py
- [[test_credentials_status_endpoint()]] - code - gateway/tests/test_key_rotation.py
- [[test_key_rotation.py]] - code - gateway/tests/test_key_rotation.py
- [[test_rotate_credential_endpoint()]] - code - gateway/tests/test_key_rotation.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/A2AMethod
SORT file.name ASC
```

## Connections to other communities
- 20 edges to [[_COMMUNITY_test_key_rotation_internals.py]]
- 18 edges to [[_COMMUNITY_CredentialInfo]]
- 17 edges to [[_COMMUNITY_TestNormalizeForSpeech]]
- 11 edges to [[_COMMUNITY_env_guard.py]]
- 6 edges to [[_COMMUNITY_EgressFilterConfig (2) (2)]]
- 3 edges to [[_COMMUNITY_AgentShroud Documentation (2)]]
- 3 edges to [[_COMMUNITY_GSDL-715 (silent regression incident)]]
- 2 edges to [[_COMMUNITY_Enum]]
- 2 edges to [[_COMMUNITY_A2AMethod (2)]]
- 2 edges to [[_COMMUNITY_dot-get_op_reference()]]
- 1 edge to [[_COMMUNITY_Any]]
- 1 edge to [[_COMMUNITY_FileSandbox]]
- 1 edge to [[_COMMUNITY_DelegationManager]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy (3)]]

## Top bridge nodes
- [[KeyRotationConfig]] - degree 44, connects to 9 communities
- [[key_rotation.py]] - degree 12, connects to 6 communities
- [[CredentialValidator]] - degree 21, connects to 5 communities
- [[RotationStatus]] - degree 20, connects to 5 communities
- [[test_key_rotation.py]] - degree 18, connects to 5 communities
