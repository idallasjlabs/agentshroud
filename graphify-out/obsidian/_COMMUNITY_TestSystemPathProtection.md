---
type: community
members: 8
---

# TestSystemPathProtection

**Members:** 8 nodes

## Members
- [[dot-test_etc_write_blocked()]] - code - gateway/tests/test_privilege_separation.py
- [[dot-test_usr_bin_write_blocked()]] - code - gateway/tests/test_privilege_separation.py
- [[dot-test_var_log_write_blocked()]] - code - gateway/tests/test_privilege_separation.py
- [[Agent cannot modify system paths.]] - rationale - gateway/tests/test_privilege_separation.py
- [[Agent cannot write to etc system configuration.]] - rationale - gateway/tests/test_privilege_separation.py
- [[Agent cannot write to usrbin system binaries.]] - rationale - gateway/tests/test_privilege_separation.py
- [[Agent cannot write to varlog system logs.]] - rationale - gateway/tests/test_privilege_separation.py
- [[TestSystemPathProtection]] - code - gateway/tests/test_privilege_separation.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestSystemPathProtection
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_middleware.py]]

## Top bridge nodes
- [[TestSystemPathProtection]] - degree 5, connects to 1 community
