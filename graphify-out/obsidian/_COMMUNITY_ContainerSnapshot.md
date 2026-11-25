---
type: community
members: 22
---

# ContainerSnapshot

**Members:** 22 nodes

## Members
- [[dot-config_hash()]] - code - gateway/security/drift_detector.py
- [[dot-setup_method()_11]] - code - gateway/tests/test_security_hardening.py
- [[dot-teardown_method()_2]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_acknowledge_alert()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_alerts_persisted()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_config_hash_changes()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_config_hash_consistency()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_image_change()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_new_capability()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_new_env_var()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_new_mount()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_no_baseline_no_alerts()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_no_drift()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_privileged_escalation()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_read_only_disabled()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_removed_capability()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_seccomp_drift()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_set_and_get_baseline()]] - code - gateway/tests/test_security_hardening.py
- [[dot-to_dict()_4]] - code - gateway/security/drift_detector.py
- [[ContainerSnapshot]] - code - gateway/security/drift_detector.py
- [[SHA-256 hash of the config for quick comparison.]] - rationale - gateway/security/drift_detector.py
- [[TestDriftDetector]] - code - gateway/tests/test_security_hardening.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/ContainerSnapshot
SORT file.name ASC
```

## Connections to other communities
- 9 edges to [[_COMMUNITY_DriftDetector]]
- 4 edges to [[_COMMUNITY_drift_detector.py]]
- 2 edges to [[_COMMUNITY_deep_security_test]]
- 2 edges to [[_COMMUNITY_AgentRegistry]]
- 2 edges to [[_COMMUNITY_TestConcurrency]]
- 1 edge to [[_COMMUNITY_ingest_apimain.py]]
- 1 edge to [[_COMMUNITY_middleware.py]]
- 1 edge to [[_COMMUNITY_ingest_apiconfig.py]]
- 1 edge to [[_COMMUNITY_AlertDispatcher]]

## Top bridge nodes
- [[ContainerSnapshot]] - degree 37, connects to 9 communities
- [[TestDriftDetector]] - degree 20, connects to 2 communities
- [[dot-setup_method()_11]] - degree 3, connects to 1 community
