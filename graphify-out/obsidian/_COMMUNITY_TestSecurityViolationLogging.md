---
type: community
members: 8
---

# TestSecurityViolationLogging

**Members:** 8 nodes

## Members
- [[dot-test_multiple_violations_tracked()]] - code - gateway/tests/test_privilege_separation.py
- [[dot-test_normal_operations_not_violations()]] - code - gateway/tests/test_privilege_separation.py
- [[dot-test_violation_recorded_in_audit()]] - code - gateway/tests/test_privilege_separation.py
- [[Multiple violations should all be tracked.]] - rationale - gateway/tests/test_privilege_separation.py
- [[Normal workspace operations should not be flagged as violations.]] - rationale - gateway/tests/test_privilege_separation.py
- [[Security violations should be recorded in audit log.]] - rationale - gateway/tests/test_privilege_separation.py
- [[Test that security violations are properly logged and tracked.]] - rationale - gateway/tests/test_privilege_separation.py
- [[TestSecurityViolationLogging]] - code - gateway/tests/test_privilege_separation.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestSecurityViolationLogging
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_FileSandbox]]

## Top bridge nodes
- [[TestSecurityViolationLogging]] - degree 5, connects to 1 community
