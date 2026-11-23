---
type: community
members: 10
---

# TestReadAccess

**Members:** 10 nodes

## Members
- [[dot-test_gateway_source_read_flagged()]] - code - gateway/tests/test_privilege_separation.py
- [[dot-test_sensitive_config_read_blocked()]] - code - gateway/tests/test_privilege_separation.py
- [[dot-test_system_info_read_allowed()]] - code - gateway/tests/test_privilege_separation.py
- [[dot-test_workspace_read_allowed()]] - code - gateway/tests/test_privilege_separation.py
- [[Agent can read basic system info.]] - rationale - gateway/tests/test_privilege_separation.py
- [[Agent can read its own workspace.]] - rationale - gateway/tests/test_privilege_separation.py
- [[Agent cannot read sensitive configuration.]] - rationale - gateway/tests/test_privilege_separation.py
- [[Reading gateway source should be flaggedblocked.]] - rationale - gateway/tests/test_privilege_separation.py
- [[Test read access controls.]] - rationale - gateway/tests/test_privilege_separation.py
- [[TestReadAccess]] - code - gateway/tests/test_privilege_separation.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestReadAccess
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_middleware.py]]

## Top bridge nodes
- [[TestReadAccess]] - degree 6, connects to 1 community
