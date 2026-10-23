---
type: community
cohesion: 0.33
members: 4
---

# .get_op_reference()

**Cohesion:** 0.33 - loosely connected
**Members:** 4 nodes

## Members
- [[dot-get_op_reference()]] - code - gateway/security/key_rotation_config.py
- [[dot-test_get_credential_status()]] - code - gateway/tests/test_key_rotation.py
- [[Build a complete op reference for a credential.]] - rationale - gateway/security/key_rotation_config.py
- [[Test credential status reporting.]] - rationale - gateway/tests/test_key_rotation.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/get_op_reference
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_A2AMethod]]

## Top bridge nodes
- [[dot-get_op_reference()]] - degree 2, connects to 1 community
- [[dot-test_get_credential_status()]] - degree 2, connects to 1 community
