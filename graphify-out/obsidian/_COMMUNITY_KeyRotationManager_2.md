---
type: community
cohesion: 0.11
members: 28
---

# KeyRotationManager

**Cohesion:** 0.11 - loosely connected
**Members:** 28 nodes

## Members
- [[dot-__init__()_116]] - code - gateway/security/key_rotation.py
- [[dot-add_custom_policy()]] - code - gateway/security/key_rotation_config.py
- [[dot-get_op_reference()]] - code - gateway/security/key_rotation_config.py
- [[dot-get_policy()]] - code - gateway/security/key_rotation_config.py
- [[dot-is_emergency_trigger_enabled()]] - code - gateway/security/key_rotation_config.py
- [[dot-test_add_custom_policy()]] - code - gateway/tests/test_key_rotation.py
- [[dot-test_default_config_has_common_policies()]] - code - gateway/tests/test_key_rotation.py
- [[dot-test_get_op_reference_builds_correctly()]] - code - gateway/tests/test_key_rotation.py
- [[dot-test_get_policy_returns_default_for_unknown_type()]] - code - gateway/tests/test_key_rotation.py
- [[Add or update a rotation policy for a specific credential type.]] - rationale - gateway/security/key_rotation_config.py
- [[Build a complete op reference for a credential.]] - rationale - gateway/security/key_rotation_config.py
- [[Check if a specific emergency trigger is enabled.]] - rationale - gateway/security/key_rotation_config.py
- [[Configuration for key rotation policies and schedules.]] - rationale - gateway/security/key_rotation_config.py
- [[CredentialRotationPolicy_1]] - code - gateway/security/key_rotation_config.py
- [[Get rotation policy for a credential type, falling back to api_key default.]] - rationale - gateway/security/key_rotation_config.py
- [[Initialize the key rotation manager.]] - rationale - gateway/security/key_rotation.py
- [[KeyRotationConfig]] - code - gateway/security/key_rotation.py
- [[KeyRotationConfig_1]] - code - gateway/security/key_rotation_config.py
- [[Rotation policy for a specific credential type.]] - rationale - gateway/security/key_rotation_config.py
- [[Test adding custom policy for new credential type.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test default config includes policies for common credential types.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test get_policy falls back to api_key for unknown types.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test key rotation configuration.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test op reference building.]] - rationale - gateway/tests/test_key_rotation.py
- [[TestKeyRotationConfig]] - code - gateway/tests/test_key_rotation.py
- [[datetime_3]] - code - gateway/security/key_rotation.py
- [[key_rotation.py]] - code - gateway/security/key_rotation.py
- [[key_rotation_config.py]] - code - gateway/security/key_rotation_config.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/KeyRotationManager
SORT file.name ASC
```

## Connections to other communities
- 16 edges to [[_COMMUNITY_KeyRotationManager_1]]
- 13 edges to [[_COMMUNITY_KeyRotationManager]]
- 8 edges to [[_COMMUNITY_KeyRotationManager_4]]
- 6 edges to [[_COMMUNITY_KeyRotationManager_6]]
- 6 edges to [[_COMMUNITY_KeyRotationManager_3]]
- 3 edges to [[_COMMUNITY_KeyRotationManager_5]]
- 3 edges to [[_COMMUNITY_EgressFilterConfig]]
- 2 edges to [[_COMMUNITY_InjectionAction]]
- 1 edge to [[_COMMUNITY_KeyRotationManager_7]]
- 1 edge to [[_COMMUNITY_TestToolChainAnalyzer]]
- 1 edge to [[_COMMUNITY_MiddlewareManager]]
- 1 edge to [[_COMMUNITY_egress_filter.py]]

## Top bridge nodes
- [[KeyRotationConfig_1]] - degree 44, connects to 8 communities
- [[key_rotation.py]] - degree 13, connects to 7 communities
- [[CredentialRotationPolicy_1]] - degree 24, connects to 6 communities
- [[TestKeyRotationConfig]] - degree 12, connects to 4 communities
- [[datetime_3]] - degree 4, connects to 1 community
