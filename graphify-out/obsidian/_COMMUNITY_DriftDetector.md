---
type: community
members: 20
---

# DriftDetector

**Members:** 20 nodes

## Members
- [[dot-__init__()_183]] - code - gateway/security/drift_detector.py
- [[dot-_init_db()_2]] - code - gateway/security/drift_detector.py
- [[dot-acknowledge_alert()]] - code - gateway/security/drift_detector.py
- [[dot-close()_15]] - code - gateway/security/drift_detector.py
- [[dot-get_alerts()]] - code - gateway/security/drift_detector.py
- [[dot-set_baseline()]] - code - gateway/security/drift_detector.py
- [[dot-test_drift_detector_baseline()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_drift_detector_detects_change()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_drift_no_false_positive()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_simultaneous_baseline_and_config_change()]] - code - gateway/tests/test_security_hardening.py
- [[Detect configuration drift from known-good baselines.]] - rationale - gateway/security/drift_detector.py
- [[Drift detector catches container config changes during operation.]] - rationale - gateway/tests/test_security_integration.py
- [[DriftDetector]] - code - gateway/security/drift_detector.py
- [[Mark an alert as acknowledged.]] - rationale - gateway/security/drift_detector.py
- [[Retrieve stored drift alerts.]] - rationale - gateway/security/drift_detector.py
- [[Store a known-good baseline configuration. Returns config hash.]] - rationale - gateway/security/drift_detector.py
- [[TestDriftDetectorHardened]] - code - gateway/tests/test_security_hardening.py
- [[Tests for drift detector hardening.]] - rationale - gateway/tests/test_security_hardening.py
- [[Verify drift is detected even with rapid changes.]] - rationale - gateway/tests/test_security_hardening.py
- [[test_drift_detection_in_pipeline()]] - code - gateway/tests/test_security_integration.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/DriftDetector
SORT file.name ASC
```

## Connections to other communities
- 9 edges to [[_COMMUNITY_ContainerSnapshot]]
- 4 edges to [[_COMMUNITY_AlertDispatcher]]
- 3 edges to [[_COMMUNITY_drift_detector.py]]
- 2 edges to [[_COMMUNITY_middleware.py]]
- 2 edges to [[_COMMUNITY_AgentRegistry]]
- 2 edges to [[_COMMUNITY_ingest_apiconfig.py]]
- 2 edges to [[_COMMUNITY_TestConcurrency]]
- 1 edge to [[_COMMUNITY_MiddlewareManager]]
- 1 edge to [[_COMMUNITY_ContextGuard]]
- 1 edge to [[_COMMUNITY_lifespan.py]]
- 1 edge to [[_COMMUNITY_lifespan]]

## Top bridge nodes
- [[DriftDetector]] - degree 29, connects to 11 communities
- [[TestDriftDetectorHardened]] - degree 5, connects to 2 communities
- [[test_drift_detection_in_pipeline()]] - degree 4, connects to 2 communities
- [[dot-test_drift_detector_baseline()]] - degree 3, connects to 2 communities
- [[dot-test_drift_detector_detects_change()]] - degree 3, connects to 2 communities
