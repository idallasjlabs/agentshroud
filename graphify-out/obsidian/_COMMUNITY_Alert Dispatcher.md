---
type: community
cohesion: 0.03
members: 103
---

# Alert Dispatcher

**Cohesion:** 0.03 - loosely connected
**Members:** 103 nodes

## Members
- [[.__init__()_57]] - code - gateway/security/drift_detector.py
- [[._format_alert_message()]] - code - gateway/security/alert_dispatcher.py
- [[._init_db()_1]] - code - gateway/security/drift_detector.py
- [[._is_duplicate()]] - code - gateway/security/alert_dispatcher.py
- [[._is_rate_limited()]] - code - gateway/security/alert_dispatcher.py
- [[._log_alert()]] - code - gateway/security/alert_dispatcher.py
- [[._send_notification()]] - code - gateway/security/alert_dispatcher.py
- [[.acknowledge_alert()]] - code - gateway/security/drift_detector.py
- [[.check_drift()]] - code - gateway/security/drift_detector.py
- [[.cleanup_seen()]] - code - gateway/security/alert_dispatcher.py
- [[.close()_6]] - code - gateway/security/drift_detector.py
- [[.config_hash()]] - code - gateway/security/drift_detector.py
- [[.dispatch()]] - code - gateway/security/alert_dispatcher.py
- [[.from_dict()_4]] - code - gateway/security/drift_detector.py
- [[.get_alerts()]] - code - gateway/security/drift_detector.py
- [[.get_baseline()]] - code - gateway/security/drift_detector.py
- [[.get_digest()]] - code - gateway/security/alert_dispatcher.py
- [[.get_stats()_12]] - code - gateway/security/alert_dispatcher.py
- [[.set_baseline()]] - code - gateway/security/drift_detector.py
- [[.setup_method()_27]] - code - gateway/tests/test_security_hardening.py
- [[.teardown_method()_6]] - code - gateway/tests/test_security_hardening.py
- [[.test_acknowledge_alert()]] - code - gateway/tests/test_security_hardening.py
- [[.test_alert_dedup()]] - code - gateway/tests/test_security_audit.py
- [[.test_alert_dispatcher_concurrent_dispatch()]] - code - gateway/tests/test_security_audit_advanced.py
- [[.test_alert_dispatcher_init()]] - code - gateway/tests/test_security_audit.py
- [[.test_alert_dispatcher_write()]] - code - gateway/tests/test_security_audit.py
- [[.test_alerts_persisted()]] - code - gateway/tests/test_security_hardening.py
- [[.test_canary_system_importable()]] - code - gateway/tests/test_security_audit.py
- [[.test_config_hash_changes()]] - code - gateway/tests/test_security_hardening.py
- [[.test_config_hash_consistency()]] - code - gateway/tests/test_security_hardening.py
- [[.test_context_guard_session_isolation_under_load()]] - code - gateway/tests/test_security_audit_advanced.py
- [[.test_dashboard_has_csp_meta()]] - code - gateway/tests/test_security_audit_advanced.py
- [[.test_dashboard_html_exists()]] - code - gateway/tests/test_security_audit_advanced.py
- [[.test_dashboard_no_inline_secrets()]] - code - gateway/tests/test_security_audit_advanced.py
- [[.test_drift_detector_baseline()]] - code - gateway/tests/test_security_audit.py
- [[.test_drift_detector_concurrent_writes()]] - code - gateway/tests/test_security_audit_advanced.py
- [[.test_drift_detector_detects_change()]] - code - gateway/tests/test_security_audit.py
- [[.test_drift_no_false_positive()]] - code - gateway/tests/test_security_audit.py
- [[.test_health_report_importable()]] - code - gateway/tests/test_security_audit.py
- [[.test_image_change()]] - code - gateway/tests/test_security_hardening.py
- [[.test_new_capability()]] - code - gateway/tests/test_security_hardening.py
- [[.test_new_env_var()]] - code - gateway/tests/test_security_hardening.py
- [[.test_new_mount()]] - code - gateway/tests/test_security_hardening.py
- [[.test_no_baseline_no_alerts()]] - code - gateway/tests/test_security_hardening.py
- [[.test_no_drift()]] - code - gateway/tests/test_security_hardening.py
- [[.test_no_mixed_content()]] - code - gateway/tests/test_security_audit_advanced.py
- [[.test_privileged_escalation()]] - code - gateway/tests/test_security_hardening.py
- [[.test_prompt_guard_concurrent_scans()]] - code - gateway/tests/test_security_audit_advanced.py
- [[.test_read_only_disabled()]] - code - gateway/tests/test_security_hardening.py
- [[.test_removed_capability()]] - code - gateway/tests/test_security_hardening.py
- [[.test_seccomp_drift()]] - code - gateway/tests/test_security_hardening.py
- [[.test_set_and_get_baseline()]] - code - gateway/tests/test_security_hardening.py
- [[.test_simultaneous_baseline_and_config_change()]] - code - gateway/tests/test_security_hardening.py
- [[.test_trust_manager_rapid_updates()]] - code - gateway/tests/test_security_audit_advanced.py
- [[.test_xss_in_dashboard_inputs()]] - code - gateway/tests/test_security_audit_advanced.py
- [[.to_dict()_7]] - code - gateway/security/drift_detector.py
- [[AlertDispatcher]] - code - gateway/security/alert_dispatcher.py
- [[Any_27]] - code - gateway/security/alert_dispatcher.py
- [[Append alert to JSONL log file.]] - rationale - gateway/security/alert_dispatcher.py
- [[Check if alert was already seen within dedup window.]] - rationale - gateway/security/alert_dispatcher.py
- [[Check if we've exceeded the rate limit.]] - rationale - gateway/security/alert_dispatcher.py
- [[Compare current config against baseline, return any drift alerts.]] - rationale - gateway/security/drift_detector.py
- [[Concurrent alert dispatch shouldn't lose or corrupt alerts.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Concurrent baseline updates — SQLite is single-threaded by default.         This]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Concurrent prompt scans shouldn't interfere with each other.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[ContainerSnapshot]] - code - gateway/security/drift_detector.py
- [[Dashboard should escape user inputs (no raw innerHTML from API).]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Dashboard should have Content-Security-Policy or mention it.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Dashboard should have an HTML file.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Dashboard should not contain hardcoded secrets.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Dashboard should not load HTTP resources.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Detect configuration drift from known-good baselines.]] - rationale - gateway/security/drift_detector.py
- [[Dispatch an alert based on severity.          Args             alert Alert dic]] - rationale - gateway/security/alert_dispatcher.py
- [[Dispatches security alerts with dedup and rate limiting.]] - rationale - gateway/security/alert_dispatcher.py
- [[Drift detector catches container config changes during operation.]] - rationale - gateway/tests/test_security_integration.py
- [[DriftAlert]] - code - gateway/security/drift_detector.py
- [[DriftDetector]] - code - gateway/security/drift_detector.py
- [[Duplicate alerts should be deduplicated.]] - rationale - gateway/tests/test_security_audit.py
- [[Format alert as human-readable message.]] - rationale - gateway/security/alert_dispatcher.py
- [[Get buffered alerts for daily digest.          Args             clear Clear bu]] - rationale - gateway/security/alert_dispatcher.py
- [[Get dispatcher statistics.]] - rationale - gateway/security/alert_dispatcher.py
- [[Mark an alert as acknowledged.]] - rationale - gateway/security/drift_detector.py
- [[POST alert to apialerts with bounded retry + backoff.          Returns True on]] - rationale - gateway/security/alert_dispatcher.py
- [[Path_19]] - code - gateway/tests/test_alert_dispatcher_retry.py
- [[Rapid trust score updates shouldn't corrupt state.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Remove expired entries from seen IDs cache.          Returns             Number]] - rationale - gateway/security/alert_dispatcher.py
- [[Retrieve baseline snapshot for a container.]] - rationale - gateway/security/drift_detector.py
- [[Retrieve stored drift alerts.]] - rationale - gateway/security/drift_detector.py
- [[SHA-256 hash of the config for quick comparison.]] - rationale - gateway/security/drift_detector.py
- [[Sessions shouldn't leak data under concurrent access.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Store a known-good baseline configuration. Returns config hash.]] - rationale - gateway/security/drift_detector.py
- [[Test audit chain integrity and tamper detection.]] - rationale - gateway/tests/test_security_audit.py
- [[Test thread safety and race conditions in security modules.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Test web dashboard and API security headers.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[TestAuditTrail_1]] - code - gateway/tests/test_security_audit.py
- [[TestConcurrency]] - code - gateway/tests/test_security_audit_advanced.py
- [[TestDriftDetector]] - code - gateway/tests/test_security_hardening.py
- [[TestWebSecurity]] - code - gateway/tests/test_security_audit_advanced.py
- [[Verify drift is detected even with rapid changes.]] - rationale - gateway/tests/test_security_hardening.py
- [[alert_dispatcher.py]] - code - gateway/security/alert_dispatcher.py
- [[dispatcher()]] - code - gateway/tests/test_alert_dispatcher_retry.py
- [[drift_detector.py]] - code - gateway/security/drift_detector.py
- [[test_drift_detection_in_pipeline()]] - code - gateway/tests/test_security_integration.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Alert_Dispatcher
SORT file.name ASC
```

## Connections to other communities
- 40 edges to [[_COMMUNITY_PII Sanitizer & Resource Guard]]
- 34 edges to [[_COMMUNITY_RBAC Middleware & Ingest API]]
- 23 edges to [[_COMMUNITY_Environment Guard & Leak Detection]]
- 17 edges to [[_COMMUNITY_Module Group 79]]
- 9 edges to [[_COMMUNITY_Module Group 110]]
- 9 edges to [[_COMMUNITY_Subagent Monitor]]
- 9 edges to [[_COMMUNITY_Module Group 66]]
- 6 edges to [[_COMMUNITY_Module Group 88]]
- 6 edges to [[_COMMUNITY_Progressive Trust Levels]]
- 5 edges to [[_COMMUNITY_Agent Isolation & Container Config]]
- 5 edges to [[_COMMUNITY_Module Group 141]]
- 4 edges to [[_COMMUNITY_Gateway Config & Lifespan]]
- 4 edges to [[_COMMUNITY_Context Guard & Integrity]]
- 3 edges to [[_COMMUNITY_Tool Result Sanitizer]]
- 3 edges to [[_COMMUNITY_Module Group 258]]
- 3 edges to [[_COMMUNITY_Module Group 257]]
- 3 edges to [[_COMMUNITY_Module Group 137]]
- 3 edges to [[_COMMUNITY_Module Group 155]]
- 3 edges to [[_COMMUNITY_Module Group 114]]
- 3 edges to [[_COMMUNITY_Module Group 153]]
- 3 edges to [[_COMMUNITY_Module Group 102]]
- 3 edges to [[_COMMUNITY_DNS Filter & Tunneling Detection]]
- 3 edges to [[_COMMUNITY_Module Group 216]]
- 3 edges to [[_COMMUNITY_Module Group 80]]
- 2 edges to [[_COMMUNITY_Module Group 439]]
- 2 edges to [[_COMMUNITY_Module Group 324]]
- 2 edges to [[_COMMUNITY_Module Group 323]]
- 2 edges to [[_COMMUNITY_Module Group 285]]
- 2 edges to [[_COMMUNITY_Module Group 63]]
- 2 edges to [[_COMMUNITY_Module Group 103]]
- 1 edge to [[_COMMUNITY_CLI & Core Gateway Routes]]
- 1 edge to [[_COMMUNITY_Module Group 505]]
- 1 edge to [[_COMMUNITY_Module Group 286]]
- 1 edge to [[_COMMUNITY_Module Group 176]]
- 1 edge to [[_COMMUNITY_Module Group 163]]
- 1 edge to [[_COMMUNITY_Module Group 113]]
- 1 edge to [[_COMMUNITY_Egress Filter & Approval]]
- 1 edge to [[_COMMUNITY_Module Group 71]]

## Top bridge nodes
- [[AlertDispatcher]] - degree 73, connects to 20 communities
- [[DriftDetector]] - degree 65, connects to 16 communities
- [[TestAuditTrail_1]] - degree 44, connects to 16 communities
- [[ContainerSnapshot]] - degree 64, connects to 15 communities
- [[TestConcurrency]] - degree 30, connects to 13 communities
