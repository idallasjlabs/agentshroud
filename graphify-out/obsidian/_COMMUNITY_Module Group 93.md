---
type: community
cohesion: 0.08
members: 44
---

# Module Group 93

**Cohesion:** 0.08 - loosely connected
**Members:** 44 nodes

## Members
- [[.add_custom_policy()]] - code - gateway/security/key_rotation_config.py
- [[.get_op_reference()]] - code - gateway/security/key_rotation_config.py
- [[.get_policy()_1]] - code - gateway/security/key_rotation_config.py
- [[.is_emergency_trigger_enabled()]] - code - gateway/security/key_rotation_config.py
- [[.test_add_custom_policy()]] - code - gateway/tests/test_key_rotation.py
- [[.test_default_config_has_common_policies()]] - code - gateway/tests/test_key_rotation.py
- [[.test_default_policy_values()]] - code - gateway/tests/test_key_rotation.py
- [[.test_get_op_reference_builds_correctly()]] - code - gateway/tests/test_key_rotation.py
- [[.test_get_policy_returns_default_for_unknown_type()]] - code - gateway/tests/test_key_rotation.py
- [[.test_should_warn()]] - code - gateway/tests/test_key_rotation.py
- [[Add or update a rotation policy for a specific credential type.]] - rationale - gateway/security/key_rotation_config.py
- [[Base class for credential validators.]] - rationale - gateway/security/key_rotation.py
- [[Build a complete op reference for a credential.]] - rationale - gateway/security/key_rotation_config.py
- [[Check if a specific emergency trigger is enabled.]] - rationale - gateway/security/key_rotation_config.py
- [[Configuration for key rotation policies and schedules.]] - rationale - gateway/security/key_rotation_config.py
- [[CredentialRotationPolicy_1]] - code - gateway/security/key_rotation_config.py
- [[CredentialValidator]] - code - gateway/security/key_rotation.py
- [[Get rotation policy for a credential type, falling back to api_key default.]] - rationale - gateway/security/key_rotation_config.py
- [[KeyRotationConfig_1]] - code - gateway/security/key_rotation_config.py
- [[Rotation policy for a specific credential type.]] - rationale - gateway/security/key_rotation_config.py
- [[RotationStatus]] - code - gateway/security/key_rotation.py
- [[Status of a credential rotation.]] - rationale - gateway/security/key_rotation.py
- [[Test adding custom policy for new credential type.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test credential information tracking.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test credential rotation policy configuration.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test default config includes policies for common credential types.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test default policy has reasonable values.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test get_policy falls back to api_key for unknown types.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test key rotation configuration.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test op reference building.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test the managecredentialshealth endpoint.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test the managecredentialsstatus endpoint.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test the POST managecredentialsrotate{credential_id} endpoint.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test warning threshold calculation.]] - rationale - gateway/tests/test_key_rotation.py
- [[TestCredentialInfo]] - code - gateway/tests/test_key_rotation.py
- [[TestCredentialRotationPolicy]] - code - gateway/tests/test_key_rotation.py
- [[TestKeyRotationConfig]] - code - gateway/tests/test_key_rotation.py
- [[datetime_2]] - code - gateway/security/key_rotation.py
- [[key_rotation.py]] - code - gateway/security/key_rotation.py
- [[key_rotation_config.py]] - code - gateway/security/key_rotation_config.py
- [[test_credentials_health_endpoint()]] - code - gateway/tests/test_key_rotation.py
- [[test_credentials_status_endpoint()]] - code - gateway/tests/test_key_rotation.py
- [[test_key_rotation.py]] - code - gateway/tests/test_key_rotation.py
- [[test_rotate_credential_endpoint()]] - code - gateway/tests/test_key_rotation.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_93
SORT file.name ASC
```

## Connections to other communities
- 18 edges to [[_COMMUNITY_Module Group 185]]
- 16 edges to [[_COMMUNITY_Module Group 108]]
- 12 edges to [[_COMMUNITY_Module Group 223]]
- 6 edges to [[_COMMUNITY_Module Group 150]]
- 2 edges to [[_COMMUNITY_URL Analyzer & Content Scanner]]
- 1 edge to [[_COMMUNITY_RBAC Middleware & Ingest API]]
- 1 edge to [[_COMMUNITY_Module Group 70]]

## Top bridge nodes
- [[KeyRotationConfig_1]] - degree 35, connects to 4 communities
- [[test_key_rotation.py]] - degree 16, connects to 4 communities
- [[key_rotation.py]] - degree 10, connects to 4 communities
- [[CredentialRotationPolicy_1]] - degree 24, connects to 3 communities
- [[CredentialValidator]] - degree 13, connects to 3 communities