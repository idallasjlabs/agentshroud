---
type: community
members: 10
---

# TestSecurityPolicyProtection

**Members:** 10 nodes

## Members
- [[dot-test_config_yaml_write_blocked()]] - code - gateway/tests/test_privilege_separation.py
- [[dot-test_soul_md_in_workspace_blocked()]] - code - gateway/tests/test_privilege_separation.py
- [[dot-test_soul_md_write_blocked()]] - code - gateway/tests/test_privilege_separation.py
- [[dot-test_system_prompt_write_blocked()]] - code - gateway/tests/test_privilege_separation.py
- [[Agent cannot modify SOUL.md behavioral instructions.]] - rationale - gateway/tests/test_privilege_separation.py
- [[Agent cannot modify SOUL.md even in workspace path.]] - rationale - gateway/tests/test_privilege_separation.py
- [[Agent cannot modify gateway configuration.]] - rationale - gateway/tests/test_privilege_separation.py
- [[Agent cannot modify security policies and behavioral instructions.]] - rationale - gateway/tests/test_privilege_separation.py
- [[Agent cannot modify system prompt files.]] - rationale - gateway/tests/test_privilege_separation.py
- [[TestSecurityPolicyProtection]] - code - gateway/tests/test_privilege_separation.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestSecurityPolicyProtection
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_middleware.py]]

## Top bridge nodes
- [[TestSecurityPolicyProtection]] - degree 6, connects to 1 community
