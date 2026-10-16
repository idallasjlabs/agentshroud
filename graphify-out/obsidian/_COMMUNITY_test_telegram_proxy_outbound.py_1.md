---
type: community
cohesion: 0.09
members: 35
---

# test_telegram_proxy_outbound.py

**Cohesion:** 0.09 - loosely connected
**Members:** 35 nodes

## Members
- [[dot-check_drift()]] - code - gateway/security/drift_detector.py
- [[dot-config_hash()]] - code - gateway/security/drift_detector.py
- [[dot-from_dict()_4]] - code - gateway/security/drift_detector.py
- [[dot-get_baseline()]] - code - gateway/security/drift_detector.py
- [[dot-set_baseline()]] - code - gateway/security/drift_detector.py
- [[dot-setup_method()_32]] - code - gateway/tests/test_security_hardening.py
- [[dot-teardown_method()_6]] - code - gateway/tests/test_security_hardening.py
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
- [[dot-test_simultaneous_baseline_and_config_change()]] - code - gateway/tests/test_security_hardening.py
- [[dot-to_dict()_8]] - code - gateway/security/drift_detector.py
- [[Compare current config against baseline, return any drift alerts.]] - rationale - gateway/security/drift_detector.py
- [[ContainerSnapshot]] - code - gateway/security/drift_detector.py
- [[Drift detector catches container config changes during operation.]] - rationale - gateway/tests/test_security_integration.py
- [[DriftAlert]] - code - gateway/security/drift_detector.py
- [[Retrieve baseline snapshot for a container.]] - rationale - gateway/security/drift_detector.py
- [[SHA-256 hash of the config for quick comparison.]] - rationale - gateway/security/drift_detector.py
- [[Store a known-good baseline configuration. Returns config hash.]] - rationale - gateway/security/drift_detector.py
- [[TestDriftDetector]] - code - gateway/tests/test_security_hardening.py
- [[Verify drift is detected even with rapid changes.]] - rationale - gateway/tests/test_security_hardening.py
- [[drift_detector.py]] - code - gateway/security/drift_detector.py
- [[test_drift_detection_in_pipeline()]] - code - gateway/tests/test_security_integration.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_telegram_proxy_outboundpy
SORT file.name ASC
```

## Connections to other communities
- 32 edges to [[_COMMUNITY_AlertDispatcher]]
- 12 edges to [[_COMMUNITY_EgressFilterConfig]]
- 5 edges to [[_COMMUNITY_AgentRegistry]]
- 4 edges to [[_COMMUNITY_KillSwitchMonitor_1]]
- 3 edges to [[_COMMUNITY_TrustConfig]]
- 2 edges to [[_COMMUNITY_PIIConfig]]
- 1 edge to [[_COMMUNITY_ResourceGuard]]
- 1 edge to [[_COMMUNITY_ContextSegment]]
- 1 edge to [[_COMMUNITY_parse_clamscan_output]]
- 1 edge to [[_COMMUNITY_EgressFilterConfig_1]]
- 1 edge to [[_COMMUNITY_egress_filter.py]]
- 1 edge to [[_COMMUNITY_ApprovalQueueConfig_6]]
- 1 edge to [[_COMMUNITY_AlertDispatcher_1]]
- 1 edge to [[_COMMUNITY_TestPathIsolationManager]]
- 1 edge to [[_COMMUNITY_Audit Ledger (SHA-256 hash only)_1]]
- 1 edge to [[_COMMUNITY_CrossBotTrustLedger_1]]
- 1 edge to [[_COMMUNITY_Path_3]]
- 1 edge to [[_COMMUNITY_AuditChain]]

## Top bridge nodes
- [[ContainerSnapshot]] - degree 63, connects to 11 communities
- [[TestDriftDetector]] - degree 35, connects to 8 communities
- [[drift_detector.py]] - degree 7, connects to 5 communities
- [[dot-test_simultaneous_baseline_and_config_change()]] - degree 4, connects to 2 communities
- [[test_drift_detection_in_pipeline()]] - degree 4, connects to 2 communities
