---
type: community
cohesion: 0.20
members: 11
---

# test_key_rotation.py

**Cohesion:** 0.20 - loosely connected
**Members:** 11 nodes

## Members
- [[dot-test_default_policy_values()]] - code - gateway/tests/test_key_rotation.py
- [[Test Gmail Credential Retrieval]] - code - gateway/tests/test_gmail_credential_retrieval.py
- [[Test credential rotation policy configuration.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test default policy has reasonable values.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test the managecredentialsstatus endpoint.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test the POST managecredentialsrotate{credential_id} endpoint.]] - rationale - gateway/tests/test_key_rotation.py
- [[TestCredentialRotationPolicy]] - code - gateway/tests/test_key_rotation.py
- [[test_credentials_health_endpoint()]] - code - gateway/tests/test_key_rotation.py
- [[test_credentials_status_endpoint()]] - code - gateway/tests/test_key_rotation.py
- [[test_key_rotation.py]] - code - gateway/tests/test_key_rotation.py
- [[test_rotate_credential_endpoint()]] - code - gateway/tests/test_key_rotation.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_key_rotationpy
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_KeyRotationConfig]]
- 5 edges to [[_COMMUNITY_CredentialValidator]]
- 4 edges to [[_COMMUNITY_CredentialInfo]]
- 2 edges to [[_COMMUNITY_KeyRotationManager]]
- 2 edges to [[_COMMUNITY_MockValidator]]
- 1 edge to [[_COMMUNITY_ModeRequest]]

## Top bridge nodes
- [[test_key_rotation.py]] - degree 18, connects to 6 communities
- [[TestCredentialRotationPolicy]] - degree 9, connects to 4 communities
- [[dot-test_default_policy_values()]] - degree 3, connects to 1 community
