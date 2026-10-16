---
type: community
cohesion: 0.06
members: 34
---

# ApprovalQueueConfig

**Cohesion:** 0.06 - loosely connected
**Members:** 34 nodes

## Members
- [[dot-monitor_sandbox()]] - code - gateway/tests/test_security_audit.py
- [[dot-sandbox()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_absolute_path_to_sensitive_blocked()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_app_read_allowed()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_basic_traversal_blocked()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_double_encoded_traversal_blocked()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_enforce_vs_monitor_contrast()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_monitor_mode_allows_everything()_1]] - code - gateway/tests/test_security_audit.py
- [[dot-test_null_byte_injection_blocked()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_proc_meminfo_allowed()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_proc_self_environ_blocked()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_staging_detection()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_symlink_traversal_blocked()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_tmp_read_allowed()_1]] - code - gateway/tests/test_security_audit.py
- [[dot-test_windows_traversal_blocked()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_write_outside_allowed_blocked()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_write_pii_detection()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_write_to_app_data_allowed()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_write_to_system_dir_blocked()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_write_to_tmp_allowed()]] - code - gateway/tests/test_security_audit.py
- [[Access to procselfenviron exposes env vars — must be blocked.]] - rationale - gateway/tests/test_security_audit.py
- [[Allowed read path should pass.]] - rationale - gateway/tests/test_security_audit.py
- [[Detect data staging patterns.]] - rationale - gateway/tests/test_security_audit.py
- [[Monitor mode flags but allows — verify difference from enforce.]] - rationale - gateway/tests/test_security_audit.py
- [[Monitor-mode sandbox for comparison testing.]] - rationale - gateway/tests/test_security_audit.py
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
TABLE source_file, type FROM #community/ApprovalQueueConfig
SORT file.name ASC
```

## Connections to other communities
- 15 edges to [[_COMMUNITY_AlertDispatcher]]
- 3 edges to [[_COMMUNITY_MiddlewareManager_1]]
- 3 edges to [[_COMMUNITY_AlertDispatcher_1]]
- 2 edges to [[_COMMUNITY_AgentTarget_2]]
- 2 edges to [[_COMMUNITY_TrustConfig_1]]
- 2 edges to [[_COMMUNITY_ResourceGuard]]
- 1 edge to [[_COMMUNITY_PIIConfig]]
- 1 edge to [[_COMMUNITY_ResourceGuard_1]]
- 1 edge to [[_COMMUNITY_KillSwitchMonitor_1]]
- 1 edge to [[_COMMUNITY_ConsentFramework_1]]
- 1 edge to [[_COMMUNITY_ContextSegment]]
- 1 edge to [[_COMMUNITY_agentshroud-blueteamSKILL_3]]
- 1 edge to [[_COMMUNITY_EgressFilterConfig_1]]
- 1 edge to [[_COMMUNITY_test_telegram_proxy_outbound.py_1]]
- 1 edge to [[_COMMUNITY_TrustConfig]]
- 1 edge to [[_COMMUNITY_DNSFilterConfig]]
- 1 edge to [[_COMMUNITY_validate_network_security]]

## Top bridge nodes
- [[TestFileSandbox]] - degree 55, connects to 17 communities
- [[dot-monitor_sandbox()]] - degree 4, connects to 2 communities
- [[dot-sandbox()]] - degree 3, connects to 2 communities
