---
type: community
cohesion: 0.33
members: 7
---

# Key Rotation

**Cohesion:** 0.33 - loosely connected
**Members:** 7 nodes

## Members
- [[Test Gmail Credential Retrieval]] - code - gateway/tests/test_gmail_credential_retrieval.py
- [[Test the managecredentialsstatus endpoint.]] - rationale - gateway/tests/test_key_rotation.py
- [[Test the POST managecredentialsrotate{credential_id} endpoint.]] - rationale - gateway/tests/test_key_rotation.py
- [[test_credentials_health_endpoint()]] - code - gateway/tests/test_key_rotation.py
- [[test_credentials_status_endpoint()]] - code - gateway/tests/test_key_rotation.py
- [[test_key_rotation.py]] - code - gateway/tests/test_key_rotation.py
- [[test_rotate_credential_endpoint()]] - code - gateway/tests/test_key_rotation.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Key_Rotation
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_Key Rotation]]
- 3 edges to [[_COMMUNITY_Key Rotation]]
- 2 edges to [[_COMMUNITY_Key Rotation Internals]]
- 2 edges to [[_COMMUNITY_Key Rotation]]
- 1 edge to [[_COMMUNITY_Key Rotation (security)]]
- 1 edge to [[_COMMUNITY_Dashboard Endpoints (web)]]

## Top bridge nodes
- [[test_key_rotation.py]] - degree 18, connects to 6 communities