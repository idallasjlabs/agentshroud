---
type: community
cohesion: 0.15
members: 16
---

# 3. Security Controls

**Cohesion:** 0.15 - loosely connected
**Members:** 16 nodes

## Members
- [[.__init__()_88]] - code - gateway/security/key_rotation.py
- [[.add_custom_policy()]] - code - gateway/security/key_rotation_config.py
- [[.get_policy()_1]] - code - gateway/security/key_rotation_config.py
- [[.test_default_policy_values()]] - code - gateway/tests/test_key_rotation.py
- [[Add or update a rotation policy for a specific credential type.]] - rationale - gateway/security/key_rotation_config.py
- [[CredentialRotationPolicy_1]] - code - gateway/security/key_rotation_config.py
- [[Get rotation policy for a credential type, falling back to api_key default.]] - rationale - gateway/security/key_rotation_config.py
- [[Initialize the key rotation manager.]] - rationale - gateway/security/key_rotation.py
- [[KeyRotationConfig]] - code - gateway/security/key_rotation.py
- [[Rotation policy for a specific credential type.]] - rationale - gateway/security/key_rotation_config.py
- [[Test credential rotation policy configuration.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test default policy has reasonable values.]] - rationale - gateway/tests/test_key_rotation.py
- [[TestCredentialRotationPolicy]] - code - gateway/tests/test_key_rotation.py
- [[datetime_4]] - code - gateway/security/key_rotation.py
- [[key_rotation.py]] - code - gateway/security/key_rotation.py
- [[key_rotation_config.py]] - code - gateway/security/key_rotation_config.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/3_Security_Controls
SORT file.name ASC
```

## Connections to other communities
- 9 edges to [[_COMMUNITY_OpenClaw Bot Container]]
- 7 edges to [[_COMMUNITY_TestNormalizeForSpeech]]
- 6 edges to [[_COMMUNITY_TestInspectorEdgeCases]]
- 6 edges to [[_COMMUNITY_Google Services Setup - Calendar, Contacts, Keep]]
- 2 edges to [[_COMMUNITY_TestOpProxyEndpoint]]
- 2 edges to [[_COMMUNITY_DOCKER-VPN-NETWORKING]]
- 1 edge to [[_COMMUNITY_EncryptedStore]]
- 1 edge to [[_COMMUNITY_TrustManager]]
- 1 edge to [[_COMMUNITY_DockerEngine]]
- 1 edge to [[_COMMUNITY_test_jira_weekly_review.py]]
- 1 edge to [[_COMMUNITY_chatbotmain.py]]
- 1 edge to [[_COMMUNITY_4. Environment Variables]]

## Top bridge nodes
- [[key_rotation.py]] - degree 13, connects to 9 communities
- [[CredentialRotationPolicy_1]] - degree 24, connects to 7 communities
- [[TestCredentialRotationPolicy]] - degree 9, connects to 5 communities
- [[datetime_4]] - degree 4, connects to 2 communities
- [[KeyRotationConfig]] - degree 3, connects to 1 community