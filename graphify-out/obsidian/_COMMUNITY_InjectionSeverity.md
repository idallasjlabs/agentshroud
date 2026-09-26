---
type: community
cohesion: 0.05
members: 45
---

# InjectionSeverity

**Cohesion:** 0.05 - loosely connected
**Members:** 45 nodes

## Members
- [[.setup_method()_8]] - code - gateway/tests/test_main_endpoints.py
- [[.teardown_method()]] - code - gateway/tests/test_main_endpoints.py
- [[.test_404_error()]] - code - gateway/tests/test_main_endpoints.py
- [[.test_alerts_accepted_from_localhost()]] - code - gateway/tests/test_main_endpoints.py
- [[.test_alerts_rejected_from_non_localhost()]] - code - gateway/tests/test_main_endpoints.py
- [[.test_backslash_encoded_rejected()]] - code - gateway/tests/test_main_endpoints.py
- [[.test_clamav_default_target_passes_allowlist()]] - code - gateway/tests/test_main_endpoints.py
- [[.test_clamav_invalid_target_returns_400()]] - code - gateway/tests/test_main_endpoints.py
- [[.test_discard_blocked_message_not_found_returns_error()]] - code - gateway/tests/test_main_endpoints.py
- [[.test_dotdot_path_rejected()]] - code - gateway/tests/test_main_endpoints.py
- [[.test_encoded_traversal_rejected()]] - code - gateway/tests/test_main_endpoints.py
- [[.test_method_not_allowed()]] - code - gateway/tests/test_main_endpoints.py
- [[.test_mixed_case_encoded_rejected()]] - code - gateway/tests/test_main_endpoints.py
- [[.test_openscap_default_profile_passes_regex()]] - code - gateway/tests/test_main_endpoints.py
- [[.test_openscap_invalid_profile_returns_400()]] - code - gateway/tests/test_main_endpoints.py
- [[.test_openscap_semicolon_profile_returns_400()]] - code - gateway/tests/test_main_endpoints.py
- [[.test_proxy_returns_400_on_traversal()]] - code - gateway/tests/test_main_endpoints.py
- [[.test_proxy_returns_400_on_traversal_in_query()]] - code - gateway/tests/test_main_endpoints.py
- [[.test_quarantine_summary_counts_inbound_and_outbound()]] - code - gateway/tests/test_main_endpoints.py
- [[.test_release_blocked_outbound_marks_item_released()]] - code - gateway/tests/test_main_endpoints.py
- [[.test_safe_path_passes()]] - code - gateway/tests/test_main_endpoints.py
- [[.test_trivy_default_scan_type_passes_allowlist()]] - code - gateway/tests/test_main_endpoints.py
- [[.test_trivy_invalid_scan_type_returns_400()]] - code - gateway/tests/test_main_endpoints.py
- [[apialerts must reject non-localhost callers (S1 fix).]] - rationale - gateway/tests/test_main_endpoints.py
- [[Allowlist validation on ClamAV target, Trivy scan type, OpenSCAP profile.]] - rationale - gateway/tests/test_main_endpoints.py
- [[Authentication dependency for protected endpoints]] - rationale - gateway/ingest_api/main.py
- [[Handler returns ok=True when called from 127.0.0.1.]] - rationale - gateway/tests/test_main_endpoints.py
- [[Receive structured security alerts from gateway-internal scripts.      Called by]] - rationale - gateway/ingest_api/main.py
- [[Reverse-proxy the Hermes Agent dashboard through the gateway.]] - rationale - gateway/ingest_api/main.py
- [[Test 404 handling for non-existent endpoints.]] - rationale - gateway/tests/test_main_endpoints.py
- [[Test 405 handling for wrong HTTP methods.]] - rationale - gateway/tests/test_main_endpoints.py
- [[Test error handling across endpoints.]] - rationale - gateway/tests/test_main_endpoints.py
- [[Test quarantine management endpoints in main.py.]] - rationale - gateway/tests/test_main_endpoints.py
- [[TestAlertsLocalhostEnforcement]] - code - gateway/tests/test_main_endpoints.py
- [[TestErrorHandling]] - code - gateway/tests/test_main_endpoints.py
- [[TestHermesDashboardPathTraversal]] - code - gateway/tests/test_main_endpoints.py
- [[TestHermesDashboardPathTraversal (CWE-22 hardening)]] - code - gateway/tests/test_main_endpoints.py
- [[TestQuarantineEndpoints]] - code - gateway/tests/test_main_endpoints.py
- [[TestScanParameterAllowlists]] - code - gateway/tests/test_main_endpoints.py
- [[auth_dep()]] - code - gateway/ingest_api/main.py
- [[hermes_dashboard_proxy must reject traversal sequences before forwarding.]] - rationale - gateway/tests/test_main_endpoints.py
- [[hermes_dashboard_proxy raises HTTPException(400) for traversal in path.]] - rationale - gateway/tests/test_main_endpoints.py
- [[hermes_dashboard_proxy()]] - code - gateway/ingest_api/main.py
- [[receive_security_alert()]] - code - gateway/ingest_api/main.py
- [[test_main_endpoints.py]] - code - gateway/tests/test_main_endpoints.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/InjectionSeverity
SORT file.name ASC
```

## Connections to other communities
- 11 edges to [[_COMMUNITY_SSHProxy]]
- 7 edges to [[_COMMUNITY_TrustManager]]
- 3 edges to [[_COMMUNITY_RateLimiter]]
- 2 edges to [[_COMMUNITY_Mode A — Single task]]
- 2 edges to [[_COMMUNITY_OutboundInfoFilter]]
- 1 edge to [[_COMMUNITY_A2APolicyEngine]]
- 1 edge to [[_COMMUNITY_TestCollaboratorPromptClassifiers]]
- 1 edge to [[_COMMUNITY_TestMultiTurnTracker]]
- 1 edge to [[_COMMUNITY_AgentShroud™ — Project Knowledge Base]]
- 1 edge to [[_COMMUNITY_start-agentshroud.sh]]
- 1 edge to [[_COMMUNITY_TestCollaboratorAccess]]
- 1 edge to [[_COMMUNITY_Skill Technical Writer (TW)]]
- 1 edge to [[_COMMUNITY_DELIVERABLE 3 — v0.8.0 Implementation Items]]
- 1 edge to [[_COMMUNITY_macOS System Administrator (MAC)]]
- 1 edge to [[_COMMUNITY_Hermes — Podcast Production Orchestrator]]

## Top bridge nodes
- [[test_main_endpoints.py]] - degree 19, connects to 9 communities
- [[auth_dep()]] - degree 12, connects to 5 communities
- [[hermes_dashboard_proxy()]] - degree 8, connects to 2 communities
- [[receive_security_alert()]] - degree 7, connects to 2 communities
- [[TestScanParameterAllowlists]] - degree 12, connects to 1 community