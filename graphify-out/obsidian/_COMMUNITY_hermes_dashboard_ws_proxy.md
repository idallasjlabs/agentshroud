---
type: community
members: 33
---

# hermes_dashboard_ws_proxy

**Members:** 33 nodes

## Members
- [[dot-_mock_websocket()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_alerts_accepted_from_localhost()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_backslash_encoded_rejected()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_bots_inventory_matches_the_real_container_name()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_connects_to_bridge_port_with_ws_scheme_and_query()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_dotdot_path_rejected()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_encoded_traversal_rejected()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_mixed_case_encoded_rejected()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_proxy_returns_400_on_traversal()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_proxy_returns_400_on_traversal_in_query()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_relays_text_and_bytes_both_directions()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_safe_path_passes()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_traversal_in_path_closes_without_connecting()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_traversal_in_query_closes_without_connecting()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_upstream_connect_failure_closes_gracefully()]] - code - gateway/tests/test_main_endpoints.py
- [[A deadunreachable bridge must not raise out of the route -- it closes the…]] - rationale - gateway/tests/test_main_endpoints.py
- [[Handler returns ok=True when called from 127.0.0.1.]] - rationale - gateway/tests/test_main_endpoints.py
- [[Relay the Hermes dashboard's WebSocket channels (apiws, apipub) through the…]] - rationale - gateway/ingest_api/main.py
- [[TestHealthCheckDetailBotsInventory]] - code - gateway/tests/test_main_endpoints.py
- [[TestHermesDashboardPathTraversal]] - code - gateway/tests/test_main_endpoints.py
- [[TestHermesDashboardWsProxy]] - code - gateway/tests/test_main_endpoints.py
- [[Upstream URL must be ws (not http) at the bridge port, with the client's…]] - rationale - gateway/tests/test_main_endpoints.py
- [[_client_to_upstream()]] - code - gateway/ingest_api/main.py
- [[_empty_aiter()]] - code - gateway/tests/test_main_endpoints.py
- [[_one_frame_aiter()]] - code - gateway/tests/test_main_endpoints.py
- [[_upstream_to_client()]] - code - gateway/ingest_api/main.py
- [[asyncio_52]] - code
- [[health_check_detail's per-bot inventory must key the Docker lookup by each…]] - rationale - gateway/tests/test_main_endpoints.py
- [[hermes_dashboard_proxy must reject traversal sequences before forwarding.]] - rationale - gateway/tests/test_main_endpoints.py
- [[hermes_dashboard_proxy raises HTTPException(400) for traversal in path.]] - rationale - gateway/tests/test_main_endpoints.py
- [[hermes_dashboard_proxy raises HTTPException(400) for traversal in query string.]] - rationale - gateway/tests/test_main_endpoints.py
- [[hermes_dashboard_ws_proxy()]] - code - gateway/ingest_api/main.py
- [[hermes_dashboard_ws_proxy WebSocket counterpart of hermes_dashboard_proxy.…]] - rationale - gateway/tests/test_main_endpoints.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/hermes_dashboard_ws_proxy
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_AsyncMock]]
- 4 edges to [[_COMMUNITY_fastapi]]
- 4 edges to [[_COMMUNITY_ingest_apimain.py]]
- 2 edges to [[_COMMUNITY__FakeWSConnect]]
- 1 edge to [[_COMMUNITY_app]]
- 1 edge to [[_COMMUNITY_server.py]]

## Top bridge nodes
- [[hermes_dashboard_ws_proxy()]] - degree 12, connects to 3 communities
- [[dot-test_alerts_accepted_from_localhost()]] - degree 5, connects to 3 communities
- [[dot-test_bots_inventory_matches_the_real_container_name()]] - degree 4, connects to 2 communities
- [[TestHermesDashboardPathTraversal]] - degree 9, connects to 1 community
- [[TestHermesDashboardWsProxy]] - degree 8, connects to 1 community
