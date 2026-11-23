---
type: community
members: 8
---

# TestWorkspaceAccessPreserved

**Members:** 8 nodes

## Members
- [[dot-test_tmp_write_allowed()]] - code - gateway/tests/test_privilege_separation.py
- [[dot-test_workspace_subdirectory_write_allowed()]] - code - gateway/tests/test_privilege_separation.py
- [[dot-test_workspace_write_allowed()]] - code - gateway/tests/test_privilege_separation.py
- [[Agent can still write to its own workspace.]] - rationale - gateway/tests/test_privilege_separation.py
- [[Agent can write to tmp for temporary files.]] - rationale - gateway/tests/test_privilege_separation.py
- [[Agent can write to its own workspace directory.]] - rationale - gateway/tests/test_privilege_separation.py
- [[Agent can write to subdirectories in workspace.]] - rationale - gateway/tests/test_privilege_separation.py
- [[TestWorkspaceAccessPreserved]] - code - gateway/tests/test_privilege_separation.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestWorkspaceAccessPreserved
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_middleware.py]]

## Top bridge nodes
- [[TestWorkspaceAccessPreserved]] - degree 5, connects to 1 community
