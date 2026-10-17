---
type: community
members: 3
---

# Restart Procedure (3)

**Members:** 3 nodes

## Members
- [[Test the managecredentialsstatus endpoint.]] - rationale - gateway/tests/test_key_rotation.py
- [[test_credentials_health_endpoint()]] - code - gateway/tests/test_key_rotation.py
- [[test_credentials_status_endpoint()]] - code - gateway/tests/test_key_rotation.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Restart_Procedure_3
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_UserSessionManager]]

## Top bridge nodes
- [[test_credentials_health_endpoint()]] - degree 2, connects to 1 community
- [[test_credentials_status_endpoint()]] - degree 2, connects to 1 community
