---
type: community
members: 2
---

# Restart Procedure (4)

**Members:** 2 nodes

## Members
- [[Test the POST managecredentialsrotate{credential_id} endpoint.]] - rationale - gateway/tests/test_key_rotation.py
- [[test_rotate_credential_endpoint()]] - code - gateway/tests/test_key_rotation.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Restart_Procedure_4
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_UserSessionManager]]

## Top bridge nodes
- [[test_rotate_credential_endpoint()]] - degree 2, connects to 1 community
