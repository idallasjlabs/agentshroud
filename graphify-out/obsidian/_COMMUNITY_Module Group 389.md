---
type: community
cohesion: 0.20
members: 10
---

# Module Group 389

**Cohesion:** 0.20 - loosely connected
**Members:** 10 nodes

## Members
- [[.test_any_python_file_in_gateway_blocked()]] - code - gateway/tests/test_privilege_separation.py
- [[.test_gateway_source_write_blocked()]] - code - gateway/tests/test_privilege_separation.py
- [[.test_modules_source_write_blocked()]] - code - gateway/tests/test_privilege_separation.py
- [[.test_security_module_write_blocked()]] - code - gateway/tests/test_privilege_separation.py
- [[Agent cannot modify AgentShroud's own source code.]] - rationale - gateway/tests/test_privilege_separation.py
- [[Agent cannot write to gateway Python source files.]] - rationale - gateway/tests/test_privilege_separation.py
- [[Agent cannot write to security framework files.]] - rationale - gateway/tests/test_privilege_separation.py
- [[Agent cannot write to security module source files.]] - rationale - gateway/tests/test_privilege_separation.py
- [[Any .py file in gateway directory should be blocked.]] - rationale - gateway/tests/test_privilege_separation.py
- [[TestAgentShroudSourceCodeProtection]] - code - gateway/tests/test_privilege_separation.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_389
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_Environment Guard & Leak Detection]]
- 1 edge to [[_COMMUNITY_RBAC Middleware & Ingest API]]

## Top bridge nodes
- [[TestAgentShroudSourceCodeProtection]] - degree 9, connects to 2 communities