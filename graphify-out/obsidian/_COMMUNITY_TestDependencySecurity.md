---
type: community
members: 10
---

# TestDependencySecurity

**Members:** 10 nodes

## Members
- [[dot-test_no_pickle_in_security_modules()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_no_shell_true_in_subprocess()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_no_yaml_unsafe_load()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_requirements_pinned()]] - code - gateway/tests/test_security_audit_advanced.py
- [[No yaml.load() without Loader (arbitrary code execution).]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Requirements should have pinned versions.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Security modules should not use pickle (deserialization attack).]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Subprocess calls should not pass shell=True. Uses AST analysis to flag only a…]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Test dependency and supply chain security.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[TestDependencySecurity]] - code - gateway/tests/test_security_audit_advanced.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestDependencySecurity
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_lifespan.py]]

## Top bridge nodes
- [[TestDependencySecurity]] - degree 6, connects to 1 community
