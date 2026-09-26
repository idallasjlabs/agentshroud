---
type: community
cohesion: 0.10
members: 24
---

# OpenClaw Bot Container

**Cohesion:** 0.10 - loosely connected
**Members:** 24 nodes

## Members
- [[.get_op_reference()]] - code - gateway/security/key_rotation_config.py
- [[.is_emergency_trigger_enabled()]] - code - gateway/security/key_rotation_config.py
- [[.test_add_custom_policy()]] - code - gateway/tests/test_key_rotation.py
- [[.test_default_config_has_common_policies()]] - code - gateway/tests/test_key_rotation.py
- [[.test_get_op_reference_builds_correctly()]] - code - gateway/tests/test_key_rotation.py
- [[.test_get_policy_returns_default_for_unknown_type()]] - code - gateway/tests/test_key_rotation.py
- [[Build a complete op reference for a credential.]] - rationale - gateway/security/key_rotation_config.py
- [[Check if a specific emergency trigger is enabled.]] - rationale - gateway/security/key_rotation_config.py
- [[Configuration for key rotation policies and schedules.]] - rationale - gateway/security/key_rotation_config.py
- [[EgressAllowlistResponse]] - code - gateway/web/management.py
- [[Get overall credential health score and status summary.]] - rationale - gateway/web/management.py
- [[Get status of all managed credentials including age and rotation schedule.]] - rationale - gateway/web/management.py
- [[KeyRotationConfig_1]] - code - gateway/security/key_rotation_config.py
- [[Response model for egress allowlist.]] - rationale - gateway/web/management.py
- [[Test adding custom policy for new credential type.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test default config includes policies for common credential types.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test get_policy falls back to api_key for unknown types.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test key rotation configuration.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test op reference building.]] - rationale - gateway/tests/test_key_rotation.py
- [[TestKeyRotationConfig]] - code - gateway/tests/test_key_rotation.py
- [[Trigger manual rotation for a specific credential (owner only).]] - rationale - gateway/web/management.py
- [[credentials_health()]] - code - gateway/web/management.py
- [[credentials_status()]] - code - gateway/web/management.py
- [[rotate_credential()]] - code - gateway/web/management.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/OpenClaw_Bot_Container
SORT file.name ASC
```

## Connections to other communities
- 11 edges to [[_COMMUNITY_Google Services Setup - Calendar, Contacts, Keep]]
- 9 edges to [[_COMMUNITY_3. Security Controls]]
- 8 edges to [[_COMMUNITY_TestNormalizeForSpeech]]
- 7 edges to [[_COMMUNITY_SkillGuard]]
- 4 edges to [[_COMMUNITY_DOCKER-VPN-NETWORKING]]
- 3 edges to [[_COMMUNITY_TestInspectorEdgeCases]]
- 2 edges to [[_COMMUNITY_TestOpProxyEndpoint]]
- 2 edges to [[_COMMUNITY_test_key_rotation.py]]
- 2 edges to [[_COMMUNITY_4. Environment Variables]]
- 1 edge to [[_COMMUNITY_main.rs]]

## Top bridge nodes
- [[KeyRotationConfig_1]] - degree 44, connects to 9 communities
- [[TestKeyRotationConfig]] - degree 12, connects to 5 communities
- [[EgressAllowlistResponse]] - degree 6, connects to 3 communities
- [[credentials_health()]] - degree 4, connects to 2 communities
- [[credentials_status()]] - degree 4, connects to 2 communities