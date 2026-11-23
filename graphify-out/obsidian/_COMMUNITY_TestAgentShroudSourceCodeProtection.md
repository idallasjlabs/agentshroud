---
type: community
members: 10
---

# TestAgentShroudSourceCodeProtection

**Members:** 10 nodes

## Members
- [[dot-test_any_python_file_in_gateway_blocked()]] - code - gateway/tests/test_privilege_separation.py
- [[dot-test_gateway_source_write_blocked()]] - code - gateway/tests/test_privilege_separation.py
- [[dot-test_modules_source_write_blocked()]] - code - gateway/tests/test_privilege_separation.py
- [[dot-test_security_module_write_blocked()]] - code - gateway/tests/test_privilege_separation.py
- [[Agent cannot modify AgentShroud's own source code.]] - rationale - gateway/tests/test_privilege_separation.py
- [[Agent cannot write to gateway Python source files.]] - rationale - gateway/tests/test_privilege_separation.py
- [[Agent cannot write to security framework files.]] - rationale - gateway/tests/test_privilege_separation.py
- [[Agent cannot write to security module source files.]] - rationale - gateway/tests/test_privilege_separation.py
- [[Any .py file in gateway directory should be blocked.]] - rationale - gateway/tests/test_privilege_separation.py
- [[TestAgentShroudSourceCodeProtection]] - code - gateway/tests/test_privilege_separation.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestAgentShroudSourceCodeProtection
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_middleware.py]]

## Top bridge nodes
- [[TestAgentShroudSourceCodeProtection]] - degree 6, connects to 1 community
