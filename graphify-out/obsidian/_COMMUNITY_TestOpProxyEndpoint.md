---
type: community
cohesion: 0.33
members: 7
---

# TestOpProxyEndpoint

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
TABLE source_file, type FROM #community/TestOpProxyEndpoint
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_Google Services Setup - Calendar, Contacts, Keep]]
- 2 edges to [[_COMMUNITY_TestInspectorEdgeCases]]
- 2 edges to [[_COMMUNITY_3. Security Controls]]
- 2 edges to [[_COMMUNITY_OpenClaw Bot Container]]
- 2 edges to [[_COMMUNITY_DOCKER-VPN-NETWORKING]]
- 1 edge to [[_COMMUNITY_TestNormalizeForSpeech]]
- 1 edge to [[_COMMUNITY_4. Environment Variables]]
- 1 edge to [[_COMMUNITY_test_redteam_probes.py]]

## Top bridge nodes
- [[test_key_rotation.py]] - degree 18, connects to 8 communities