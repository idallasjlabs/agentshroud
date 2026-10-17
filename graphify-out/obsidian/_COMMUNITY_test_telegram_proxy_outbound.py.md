---
type: community
members: 40
---

# test_telegram_proxy_outbound.py

**Members:** 40 nodes

## Members
- [[dot-check_drift()]] - code - gateway/security/drift_detector.py
- [[dot-config_hash()]] - code - gateway/security/drift_detector.py
- [[dot-from_dict()]] - code - gateway/security/drift_detector.py
- [[dot-get_baseline()]] - code - gateway/security/drift_detector.py
- [[dot-set_baseline()]] - code - gateway/security/drift_detector.py
- [[dot-setup_method()_11]] - code - gateway/tests/test_security_hardening.py
- [[dot-teardown_method()_3]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_acknowledge_alert()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_alerts_persisted()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_config_hash_changes()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_config_hash_consistency()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_drift_detector_baseline()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_drift_detector_detects_change()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_drift_no_false_positive()]] - code - gateway/tests/test_security_audit.py
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
- [[ContainerSnapshot]] - code - gateway/security/drift_detector.py
- [[Drift detector catches container config changes during operation.]] - rationale - gateway/tests/test_security_integration.py
- [[DriftAlert]] - code - gateway/security/drift_detector.py
- [[Retrieve baseline snapshot for a container.]] - rationale - gateway/security/drift_detector.py
- [[SHA-256 hash of the config for quick comparison.]] - rationale - gateway/security/drift_detector.py
- [[Store a known-good baseline configuration. Returns config hash.]] - rationale - gateway/security/drift_detector.py
- [[TestDriftDetector]] - code - gateway/tests/test_security_hardening.py
- [[Verify drift is detected even with rapid changes.]] - rationale - gateway/tests/test_security_hardening.py
- [[alert_dispatcher.py]] - code - gateway/security/alert_dispatcher.py
- [[clamav_scanner.py]] - code - gateway/security/clamav_scanner.py
- [[drift_detector.py]] - code - gateway/security/drift_detector.py
- [[test_drift_detection_in_pipeline()]] - code - gateway/tests/test_security_integration.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_telegram_proxy_outboundpy
SORT file.name ASC
```

## Connections to other communities
- 23 edges to [[_COMMUNITY_AlertDispatcher]]
- 19 edges to [[_COMMUNITY_AlertDispatcher (2)]]
- 15 edges to [[_COMMUNITY_EgressFilterConfig]]
- 6 edges to [[_COMMUNITY_AgentRegistry]]
- 4 edges to [[_COMMUNITY_parse_clamscan_output]]
- 3 edges to [[_COMMUNITY_FalcoAlertWatcher]]
- 2 edges to [[_COMMUNITY_ContextSegment]]
- 2 edges to [[_COMMUNITY_TrustConfig]]
- 2 edges to [[_COMMUNITY_ClamAV]]
- 2 edges to [[_COMMUNITY_PIIConfig]]
- 1 edge to [[_COMMUNITY_WebContentScanner]]
- 1 edge to [[_COMMUNITY_AuditChain]]
- 1 edge to [[_COMMUNITY_test_security_toolchain.py]]
- 1 edge to [[_COMMUNITY_test_e2e_proxy.py]]
- 1 edge to [[_COMMUNITY_DNSFilterConfig]]
- 1 edge to [[_COMMUNITY_test_clamav_pipeline.py]]
- 1 edge to [[_COMMUNITY_FR3 System Integrity]]
- 1 edge to [[_COMMUNITY_egress_filter.py (3)]]
- 1 edge to [[_COMMUNITY_KillSwitchMonitor (4)]]
- 1 edge to [[_COMMUNITY_CrossBotTrustLedger (2)]]
- 1 edge to [[_COMMUNITY_Path (4)]]
- 1 edge to [[_COMMUNITY_CrossBotTrustLedger]]

## Top bridge nodes
- [[ContainerSnapshot]] - degree 63, connects to 8 communities
- [[TestDriftDetector]] - degree 35, connects to 8 communities
- [[clamav_scanner.py]] - degree 13, connects to 8 communities
- [[alert_dispatcher.py]] - degree 10, connects to 7 communities
- [[drift_detector.py]] - degree 7, connects to 3 communities
