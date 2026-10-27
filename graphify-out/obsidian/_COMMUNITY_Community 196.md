---
type: community
members: 32
---

# Community 196

**Members:** 32 nodes

## Members
- [[.test_absolute_path_to_sensitive_blocked()]] - code - gateway/tests/test_security_audit.py
- [[.test_app_read_allowed()]] - code - gateway/tests/test_security_audit.py
- [[.test_basic_traversal_blocked()]] - code - gateway/tests/test_security_audit.py
- [[.test_double_encoded_traversal_blocked()]] - code - gateway/tests/test_security_audit.py
- [[.test_enforce_vs_monitor_contrast()]] - code - gateway/tests/test_security_audit.py
- [[.test_monitor_mode_allows_everything()_1]] - code - gateway/tests/test_security_audit.py
- [[.test_null_byte_injection_blocked()]] - code - gateway/tests/test_security_audit.py
- [[.test_proc_meminfo_allowed()]] - code - gateway/tests/test_security_audit.py
- [[.test_proc_self_environ_blocked()]] - code - gateway/tests/test_security_audit.py
- [[.test_staging_detection()]] - code - gateway/tests/test_security_audit.py
- [[.test_symlink_traversal_blocked()]] - code - gateway/tests/test_security_audit.py
- [[.test_tmp_read_allowed()_1]] - code - gateway/tests/test_security_audit.py
- [[.test_windows_traversal_blocked()]] - code - gateway/tests/test_security_audit.py
- [[.test_write_outside_allowed_blocked()]] - code - gateway/tests/test_security_audit.py
- [[.test_write_pii_detection()]] - code - gateway/tests/test_security_audit.py
- [[.test_write_to_app_data_allowed()]] - code - gateway/tests/test_security_audit.py
- [[.test_write_to_system_dir_blocked()]] - code - gateway/tests/test_security_audit.py
- [[.test_write_to_tmp_allowed()]] - code - gateway/tests/test_security_audit.py
- [[Access to procselfenviron exposes env vars — must be blocked.]] - rationale - gateway/tests/test_security_audit.py
- [[Allowed read path should pass.]] - rationale - gateway/tests/test_security_audit.py
- [[Detect data staging patterns.]] - rationale - gateway/tests/test_security_audit.py
- [[Monitor mode flags but allows — verify difference from enforce.]] - rationale - gateway/tests/test_security_audit.py
- [[Reading from app should be allowed.]] - rationale - gateway/tests/test_security_audit.py
- [[Reading from tmp should be allowed.]] - rationale - gateway/tests/test_security_audit.py
- [[Same path, different modes — enforce blocks, monitor allows.]] - rationale - gateway/tests/test_security_audit.py
- [[Symlink-based escape attempt blocked.]] - rationale - gateway/tests/test_security_audit.py
- [[Test file system sandboxing in enforce mode — blocks unauthorized access.]] - rationale - gateway/tests/test_security_audit.py
- [[TestFileSandbox]] - code - gateway/tests/test_security_audit.py
- [[Writing PII should be flagged even to allowed paths.]] - rationale - gateway/tests/test_security_audit.py
- [[Writing outside allowed paths must be blocked.]] - rationale - gateway/tests/test_security_audit.py
- [[Writing to appdata should be allowed.]] - rationale - gateway/tests/test_security_audit.py
- [[Writing to tmp should be allowed.]] - rationale - gateway/tests/test_security_audit.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_196
SORT file.name ASC
```

## Connections to other communities
- 15 edges to [[_COMMUNITY_Community 0]]
- 3 edges to [[_COMMUNITY_Community 41]]
- 2 edges to [[_COMMUNITY_Community 72]]
- 2 edges to [[_COMMUNITY_Community 431]]
- 2 edges to [[_COMMUNITY_Community 24]]
- 1 edge to [[_COMMUNITY_Community 7]]
- 1 edge to [[_COMMUNITY_Community 52]]
- 1 edge to [[_COMMUNITY_Community 108]]
- 1 edge to [[_COMMUNITY_Community 146]]
- 1 edge to [[_COMMUNITY_Community 93]]
- 1 edge to [[_COMMUNITY_Community 477]]
- 1 edge to [[_COMMUNITY_Community 121]]
- 1 edge to [[_COMMUNITY_Community 71]]
- 1 edge to [[_COMMUNITY_Community 22]]
- 1 edge to [[_COMMUNITY_Community 434]]
- 1 edge to [[_COMMUNITY_Community 5]]
- 1 edge to [[_COMMUNITY_Community 11]]

## Top bridge nodes
- [[TestFileSandbox]] - degree 55, connects to 17 communities