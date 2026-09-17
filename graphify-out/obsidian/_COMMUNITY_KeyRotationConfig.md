---
type: community
cohesion: 0.11
members: 28
---

# KeyRotationConfig

**Cohesion:** 0.11 - loosely connected
**Members:** 28 nodes

## Members
- [[.__init__()_124]] - code - gateway/security/key_rotation.py
- [[.add_custom_policy()]] - code - gateway/security/key_rotation_config.py
- [[.get_op_reference()]] - code - gateway/security/key_rotation_config.py
- [[.get_policy()_1]] - code - gateway/security/key_rotation_config.py
- [[.is_emergency_trigger_enabled()]] - code - gateway/security/key_rotation_config.py
- [[.test_add_custom_policy()]] - code - gateway/tests/test_key_rotation.py
- [[.test_default_config_has_common_policies()]] - code - gateway/tests/test_key_rotation.py
- [[.test_get_op_reference_builds_correctly()]] - code - gateway/tests/test_key_rotation.py
- [[.test_get_policy_returns_default_for_unknown_type()]] - code - gateway/tests/test_key_rotation.py
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
- [[datetime_2]] - code - gateway/security/key_rotation.py
- [[key_rotation.py]] - code - gateway/security/key_rotation.py
- [[key_rotation_config.py]] - code - gateway/security/key_rotation_config.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/KeyRotationConfig
SORT file.name ASC
```

## Connections to other communities
- 16 edges to [[_COMMUNITY_CredentialValidator]]
- 13 edges to [[_COMMUNITY_KeyRotationManager]]
- 8 edges to [[_COMMUNITY_CredentialInfo]]
- 6 edges to [[_COMMUNITY_test_key_rotation.py]]
- 6 edges to [[_COMMUNITY_MockValidator]]
- 3 edges to [[_COMMUNITY_TestKeyRotationManager]]
- 3 edges to [[_COMMUNITY_EgressFilterConfig]]
- 1 edge to [[_COMMUNITY_TestStoreIn1Password]]
- 1 edge to [[_COMMUNITY_test_redteam_probes.py]]
- 1 edge to [[_COMMUNITY_agentshroud-blueteamSKILL]]
- 1 edge to [[_COMMUNITY_TrustManager]]
- 1 edge to [[_COMMUNITY_Enum]]
- 1 edge to [[_COMMUNITY_AgentShroud Semgrep SAST Configuration]]

## Top bridge nodes
- [[KeyRotationConfig_1]] - degree 44, connects to 8 communities
- [[key_rotation.py]] - degree 13, connects to 8 communities
- [[CredentialRotationPolicy_1]] - degree 24, connects to 6 communities
- [[TestKeyRotationConfig]] - degree 12, connects to 4 communities
- [[datetime_2]] - degree 4, connects to 1 community