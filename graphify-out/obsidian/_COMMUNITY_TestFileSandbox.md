---
type: community
cohesion: 0.07
members: 31
---

# TestFileSandbox

**Cohesion:** 0.07 - loosely connected
**Members:** 31 nodes

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
TABLE source_file, type FROM #community/TestFileSandbox
SORT file.name ASC
```

## Connections to other communities
- 11 edges to [[_COMMUNITY_lifespan.py]]
- 4 edges to [[_COMMUNITY_test_security_audit.py]]
- 4 edges to [[_COMMUNITY_FileSandbox]]
- 3 edges to [[_COMMUNITY_TrustManager]]
- 3 edges to [[_COMMUNITY_EncryptedStore]]
- 2 edges to [[_COMMUNITY_DNSFilterConfig]]
- 2 edges to [[_COMMUNITY_TestAuth]]
- 2 edges to [[_COMMUNITY_ResourceGuard]]
- 1 edge to [[_COMMUNITY_KeyVaultConfig]]
- 1 edge to [[_COMMUNITY_EgressPolicy]]
- 1 edge to [[_COMMUNITY_ConsentFramework]]
- 1 edge to [[_COMMUNITY_GitGuard]]
- 1 edge to [[_COMMUNITY_KeyVault]]

## Top bridge nodes
- [[TestFileSandbox]] - degree 55, connects to 13 communities