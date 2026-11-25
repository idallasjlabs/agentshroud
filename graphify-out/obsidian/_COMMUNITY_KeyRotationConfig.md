---
type: community
members: 37
---

# KeyRotationConfig

**Members:** 37 nodes

## Members
- [[dot-add_custom_policy()]] - code - gateway/security/key_rotation_config.py
- [[dot-get_op_reference()]] - code - gateway/security/key_rotation_config.py
- [[dot-get_policy()]] - code - gateway/security/key_rotation_config.py
- [[dot-is_emergency_trigger_enabled()]] - code - gateway/security/key_rotation_config.py
- [[dot-test_add_custom_policy()]] - code - gateway/tests/test_key_rotation.py
- [[dot-test_default_config_has_common_policies()]] - code - gateway/tests/test_key_rotation.py
- [[dot-test_default_policy_values()]] - code - gateway/tests/test_key_rotation.py
- [[dot-test_get_op_reference_builds_correctly()]] - code - gateway/tests/test_key_rotation.py
- [[dot-test_get_policy_returns_default_for_unknown_type()]] - code - gateway/tests/test_key_rotation.py
- [[Add or update a rotation policy for a specific credential type.]] - rationale - gateway/security/key_rotation_config.py
- [[Base class for credential validators.]] - rationale - gateway/security/key_rotation.py
- [[Behavior tests for KeyRotationManager internals and guard branches. The…]] - rationale - gateway/tests/test_key_rotation_internals.py
- [[Build a complete op reference for a credential.]] - rationale - gateway/security/key_rotation_config.py
- [[Check if a specific emergency trigger is enabled.]] - rationale - gateway/security/key_rotation_config.py
- [[Configuration for key rotation policies and schedules.]] - rationale - gateway/security/key_rotation_config.py
- [[CredentialRotationPolicy]] - code - gateway/security/key_rotation_config.py
- [[CredentialValidator]] - code - gateway/security/key_rotation.py
- [[Enum_9]] - code
- [[Get rotation policy for a credential type, falling back to api_key default.]] - rationale - gateway/security/key_rotation_config.py
- [[KeyRotationConfig]] - code - gateway/security/key_rotation_config.py
- [[Rotation policy for a specific credential type.]] - rationale - gateway/security/key_rotation_config.py
- [[RotationStatus]] - code - gateway/security/key_rotation.py
- [[Status of a credential rotation.]] - rationale - gateway/security/key_rotation.py
- [[Test adding custom policy for new credential type.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test credential rotation policy configuration.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test default config includes policies for common credential types.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test default policy has reasonable values.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test get_policy falls back to api_key for unknown types.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test key rotation configuration.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test op reference building.]] - rationale - gateway/tests/test_key_rotation.py
- [[TestCredentialRotationPolicy]] - code - gateway/tests/test_key_rotation.py
- [[TestKeyRotationConfig]] - code - gateway/tests/test_key_rotation.py
- [[fixture_20]] - code
- [[key_rotation.py]] - code - gateway/security/key_rotation.py
- [[key_rotation_config.py]] - code - gateway/security/key_rotation_config.py
- [[manager()]] - code - gateway/tests/test_key_rotation_internals.py
- [[test_key_rotation_internals.py]] - code - gateway/tests/test_key_rotation_internals.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/KeyRotationConfig
SORT file.name ASC
```

## Connections to other communities
- 12 edges to [[_COMMUNITY_CredentialInfo]]
- 12 edges to [[_COMMUNITY_test_key_rotation.py]]
- 9 edges to [[_COMMUNITY_asyncio_4]]
- 8 edges to [[_COMMUNITY_KeyRotationManager]]
- 4 edges to [[_COMMUNITY_management.py]]
- 1 edge to [[_COMMUNITY_TestStatusHelpers]]
- 1 edge to [[_COMMUNITY_ContextGuard]]
- 1 edge to [[_COMMUNITY_middleware.py]]

## Top bridge nodes
- [[key_rotation.py]] - degree 13, connects to 5 communities
- [[KeyRotationConfig]] - degree 26, connects to 4 communities
- [[test_key_rotation_internals.py]] - degree 17, connects to 4 communities
- [[CredentialValidator]] - degree 8, connects to 3 communities
- [[RotationStatus]] - degree 8, connects to 3 communities
