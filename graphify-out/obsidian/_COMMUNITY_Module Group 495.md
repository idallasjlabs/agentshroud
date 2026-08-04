---
type: community
cohesion: 0.33
members: 6
---

# Module Group 495

**Cohesion:** 0.33 - loosely connected
**Members:** 6 nodes

## Members
- [[.test_ssh_command_uses_strict_checking()]] - code - gateway/tests/test_security_fixes.py
- [[.test_strict_host_key_checking_in_source()]] - code - gateway/tests/test_security_fixes.py
- [[SSH execute builds command with StrictHostKeyChecking=yes]] - rationale - gateway/tests/test_security_fixes.py
- [[Source code uses StrictHostKeyChecking=yes]] - rationale - gateway/tests/test_security_fixes.py
- [[TestSSHStrictHostKeyChecking]] - code - gateway/tests/test_security_fixes.py
- [[Verify SSH proxy uses StrictHostKeyChecking=yes, not accept-new]] - rationale - gateway/tests/test_security_fixes.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_495
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_SSH Proxy & Gateway Config]]
- 2 edges to [[_COMMUNITY_Module Group 94]]
- 1 edge to [[_COMMUNITY_Module Group 132]]

## Top bridge nodes
- [[TestSSHStrictHostKeyChecking]] - degree 7, connects to 3 communities
- [[.test_ssh_command_uses_strict_checking()]] - degree 5, connects to 2 communities
