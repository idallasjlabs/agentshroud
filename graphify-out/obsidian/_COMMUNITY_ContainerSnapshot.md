---
type: community
members: 56
---

# ContainerSnapshot

**Members:** 56 nodes

## Members
- [[dot-__init__()_46]] - code - gateway/security/drift_detector.py
- [[dot-_init_db()]] - code - gateway/security/drift_detector.py
- [[dot-acknowledge_alert()]] - code - gateway/security/drift_detector.py
- [[dot-check_drift()]] - code - gateway/security/drift_detector.py
- [[dot-close()_1]] - code - gateway/security/drift_detector.py
- [[dot-config_hash()]] - code - gateway/security/drift_detector.py
- [[dot-from_dict()_3]] - code - gateway/security/drift_detector.py
- [[dot-get_alerts()]] - code - gateway/security/drift_detector.py
- [[dot-get_baseline()]] - code - gateway/security/drift_detector.py
- [[dot-set_baseline()]] - code - gateway/security/drift_detector.py
- [[dot-setup_method()_12]] - code - gateway/tests/test_security_hardening.py
- [[dot-teardown_method()_3]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_acknowledge_alert()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_alerts_persisted()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_canary_system_importable()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_config_hash_changes()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_config_hash_consistency()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_drift_detector_baseline()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_drift_detector_concurrent_writes()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_drift_detector_detects_change()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_drift_no_false_positive()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_health_report_importable()]] - code - gateway/tests/test_security_audit.py
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
- [[dot-test_simultaneous_baseline_and_config_change()]] - code - gateway/tests/test_security_hardening.py
- [[dot-to_dict()_2]] - code - gateway/security/drift_detector.py
- [[Compare current config against baseline, return any drift alerts.]] - rationale - gateway/security/drift_detector.py
- [[Concurrent baseline updates — SQLite is single-threaded by default. This…]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[ContainerSnapshot]] - code - gateway/security/drift_detector.py
- [[Detect configuration drift from known-good baselines.]] - rationale - gateway/security/drift_detector.py
- [[Drift Detection — detect unauthorized container config changes. Snapshots…]] - rationale - gateway/security/drift_detector.py
- [[Drift detector catches container config changes during operation.]] - rationale - gateway/tests/test_security_integration.py
- [[DriftAlert]] - code - gateway/security/drift_detector.py
- [[DriftDetector]] - code - gateway/security/drift_detector.py
- [[Mark an alert as acknowledged.]] - rationale - gateway/security/drift_detector.py
- [[Retrieve baseline snapshot for a container.]] - rationale - gateway/security/drift_detector.py
- [[Retrieve stored drift alerts.]] - rationale - gateway/security/drift_detector.py
- [[SHA-256 hash of the config for quick comparison.]] - rationale - gateway/security/drift_detector.py
- [[Store a known-good baseline configuration. Returns config hash.]] - rationale - gateway/security/drift_detector.py
- [[Test audit chain integrity and tamper detection.]] - rationale - gateway/tests/test_security_audit.py
- [[TestAuditTrail]] - code - gateway/tests/test_security_audit.py
- [[TestDriftDetector]] - code - gateway/tests/test_security_hardening.py
- [[TestDriftDetectorHardened]] - code - gateway/tests/test_security_hardening.py
- [[Tests for drift detector hardening.]] - rationale - gateway/tests/test_security_hardening.py
- [[Verify drift is detected even with rapid changes.]] - rationale - gateway/tests/test_security_hardening.py
- [[drift_detector.py]] - code - gateway/security/drift_detector.py
- [[test_drift_detection_in_pipeline()]] - code - gateway/tests/test_security_integration.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/ContainerSnapshot
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_AgentRegistry]]
- 4 edges to [[_COMMUNITY_test_security_integration.py]]
- 4 edges to [[_COMMUNITY_AlertDispatcher]]
- 3 edges to [[_COMMUNITY_test_security_audit.py]]
- 3 edges to [[_COMMUNITY_PromptGuard]]
- 3 edges to [[_COMMUNITY_middleware.py]]
- 2 edges to [[_COMMUNITY_deep_security_test]]
- 1 edge to [[_COMMUNITY_MiddlewareManager]]
- 1 edge to [[_COMMUNITY_ingest_apimain.py]]
- 1 edge to [[_COMMUNITY_lifespan.py]]
- 1 edge to [[_COMMUNITY_lifespan]]

## Top bridge nodes
- [[DriftDetector]] - degree 29, connects to 8 communities
- [[ContainerSnapshot]] - degree 37, connects to 6 communities
- [[drift_detector.py]] - degree 7, connects to 3 communities
- [[TestAuditTrail]] - degree 13, connects to 2 communities
- [[TestDriftDetector]] - degree 20, connects to 1 community
