---
type: community
members: 38
---

# Community 1658

**Members:** 38 nodes

## Members
- [[._mock_websocket()]] - code - gateway/tests/test_main_endpoints.py
- [[.test_alerts_accepted_from_localhost()]] - code - gateway/tests/test_main_endpoints.py
- [[.test_alerts_rejected_from_non_localhost()]] - code - gateway/tests/test_main_endpoints.py
- [[.test_backslash_encoded_rejected()]] - code - gateway/tests/test_main_endpoints.py
- [[.test_connects_to_bridge_port_with_ws_scheme_and_query()]] - code - gateway/tests/test_main_endpoints.py
- [[.test_discard_blocked_message_not_found_returns_error()]] - code - gateway/tests/test_main_endpoints.py
- [[.test_dotdot_path_rejected()]] - code - gateway/tests/test_main_endpoints.py
- [[.test_encoded_traversal_rejected()]] - code - gateway/tests/test_main_endpoints.py
- [[.test_mixed_case_encoded_rejected()]] - code - gateway/tests/test_main_endpoints.py
- [[.test_proxy_returns_400_on_traversal()]] - code - gateway/tests/test_main_endpoints.py
- [[.test_proxy_returns_400_on_traversal_in_query()]] - code - gateway/tests/test_main_endpoints.py
- [[.test_quarantine_summary_counts_inbound_and_outbound()]] - code - gateway/tests/test_main_endpoints.py
- [[.test_relays_text_and_bytes_both_directions()]] - code - gateway/tests/test_main_endpoints.py
- [[.test_release_blocked_outbound_marks_item_released()]] - code - gateway/tests/test_main_endpoints.py
- [[.test_safe_path_passes()]] - code - gateway/tests/test_main_endpoints.py
- [[.test_traversal_in_path_closes_without_connecting()]] - code - gateway/tests/test_main_endpoints.py
- [[.test_traversal_in_query_closes_without_connecting()]] - code - gateway/tests/test_main_endpoints.py
- [[.test_upstream_connect_failure_closes_gracefully()]] - code - gateway/tests/test_main_endpoints.py
- [[apialerts must reject non-localhost callers (S1 fix).]] - rationale - gateway/tests/test_main_endpoints.py
- [[A deadunreachable bridge must not raise out of the route --         it closes t]] - rationale - gateway/tests/test_main_endpoints.py
- [[Handler returns ok=True when called from 127.0.0.1.]] - rationale - gateway/tests/test_main_endpoints.py
- [[Receive structured security alerts from gateway-internal scripts.      Called by]] - rationale - gateway/ingest_api/main.py
- [[Relay the Hermes dashboard's WebSocket channels (apiws, apipub)     through]] - rationale - gateway/ingest_api/main.py
- [[Reverse-proxy the Hermes Agent dashboard through the gateway.]] - rationale - gateway/ingest_api/main.py
- [[Test quarantine management endpoints in main.py.]] - rationale - gateway/tests/test_main_endpoints.py
- [[TestAlertsLocalhostEnforcement]] - code - gateway/tests/test_main_endpoints.py
- [[TestHermesDashboardPathTraversal]] - code - gateway/tests/test_main_endpoints.py
- [[TestHermesDashboardWsProxy]] - code - gateway/tests/test_main_endpoints.py
- [[TestQuarantineEndpoints]] - code - gateway/tests/test_main_endpoints.py
- [[Upstream URL must be ws (not http) at the bridge port, with         the cl]] - rationale - gateway/tests/test_main_endpoints.py
- [[hermes_dashboard_proxy must reject traversal sequences before forwarding.]] - rationale - gateway/tests/test_main_endpoints.py
- [[hermes_dashboard_proxy raises HTTPException(400) for traversal in path.]] - rationale - gateway/tests/test_main_endpoints.py
- [[hermes_dashboard_proxy raises HTTPException(400) for traversal in query string.]] - rationale - gateway/tests/test_main_endpoints.py
- [[hermes_dashboard_proxy()]] - code - gateway/ingest_api/main.py
- [[hermes_dashboard_ws_proxy()]] - code - gateway/ingest_api/main.py
- [[hermes_dashboard_ws_proxy WebSocket counterpart of hermes_dashboard_proxy.]] - rationale - gateway/tests/test_main_endpoints.py
- [[receive_security_alert()]] - code - gateway/ingest_api/main.py
- [[test_main_endpoints.py]] - code - gateway/tests/test_main_endpoints.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_1658
SORT file.name ASC
```

## Connections to other communities
- 10 edges to [[_COMMUNITY_Community 1127]]
- 9 edges to [[_COMMUNITY_Community 53]]
- 5 edges to [[_COMMUNITY_Community 72]]
- 4 edges to [[_COMMUNITY_Community 978]]
- 3 edges to [[_COMMUNITY_Community 254]]
- 1 edge to [[_COMMUNITY_Community 62]]
- 1 edge to [[_COMMUNITY_Community 2154]]
- 1 edge to [[_COMMUNITY_Community 480]]
- 1 edge to [[_COMMUNITY_Community 707]]

## Top bridge nodes
- [[test_main_endpoints.py]] - degree 22, connects to 6 communities
- [[hermes_dashboard_proxy()]] - degree 7, connects to 3 communities
- [[receive_security_alert()]] - degree 6, connects to 3 communities
- [[TestHermesDashboardPathTraversal]] - degree 11, connects to 2 communities
- [[TestHermesDashboardWsProxy]] - degree 10, connects to 2 communities