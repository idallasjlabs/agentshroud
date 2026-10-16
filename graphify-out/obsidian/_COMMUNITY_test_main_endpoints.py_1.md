---
type: community
cohesion: 0.09
members: 36
---

# test_main_endpoints.py

**Cohesion:** 0.09 - loosely connected
**Members:** 36 nodes

## Members
- [[dot-_mock_websocket()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_backslash_encoded_rejected()]] - code - gateway/tests/test_main_endpoints.py
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
- [[HERMES_DASHBOARD_UPSTREAM  _HOST_UPSTREAM dev hostnames]] - rationale - docker/docker-compose.agentshroud-bot.marvin.yml
- [[Relay the Hermes dashboard's WebSocket channels (apiws, apipub) through the…]] - rationale - gateway/ingest_api/main.py
- [[Reverse-proxy the Hermes Agent dashboard through the gateway.]] - rationale - gateway/ingest_api/main.py
- [[TestHermesDashboardPathTraversal]] - code - gateway/tests/test_main_endpoints.py
- [[TestHermesDashboardWsProxy]] - code - gateway/tests/test_main_endpoints.py
- [[Upstream URL must be ws (not http) at the bridge port, with the client's…]] - rationale - gateway/tests/test_main_endpoints.py
- [[WebSocket relay for Slack Socket Mode inbound traffic. Bot connects here…]] - rationale - gateway/ingest_api/main.py
- [[_bot_to_upstream()]] - code - gateway/ingest_api/main.py
- [[_client_to_upstream()]] - code - gateway/ingest_api/main.py
- [[_empty_aiter()]] - code - gateway/tests/test_main_endpoints.py
- [[_one_frame_aiter()]] - code - gateway/tests/test_main_endpoints.py
- [[_upstream_to_bot()]] - code - gateway/ingest_api/main.py
- [[_upstream_to_client()]] - code - gateway/ingest_api/main.py
- [[asyncio_1]] - code
- [[hermes-dashboard-relay bypass of the gateway proxy]] - rationale - INCIDENT_2026-10-16_conduit-outage.md
- [[hermes_dashboard_proxy (hermes-dashboard{path} HTTP reverse proxy)]] - code - gateway/ingest_api/main.py
- [[hermes_dashboard_proxy must reject traversal sequences before forwarding.]] - rationale - gateway/tests/test_main_endpoints.py
- [[hermes_dashboard_proxy raises HTTPException(400) for traversal in path.]] - rationale - gateway/tests/test_main_endpoints.py
- [[hermes_dashboard_ws_proxy (WebSocket relay)]] - code - gateway/ingest_api/main.py
- [[hermes_dashboard_ws_proxy WebSocket counterpart of hermes_dashboard_proxy.…]] - rationale - gateway/tests/test_main_endpoints.py
- [[slack_ws_relay()]] - code - gateway/ingest_api/main.py
- [[websocket_2]] - code

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_main_endpointspy
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_test_main_endpoints.py]]
- 3 edges to [[_COMMUNITY_gatewayingest_apimain.py (hermes-dashboard HTTP + WebSocket reverse proxy)]]
- 3 edges to [[_COMMUNITY_agentshroud-blueteamSKILL_4]]
- 1 edge to [[_COMMUNITY_dot-_run_proxy()]]
- 1 edge to [[_COMMUNITY_SecureBrowser Skill_1]]
- 1 edge to [[_COMMUNITY_AgentTarget_3]]
- 1 edge to [[_COMMUNITY_run-standalone.sh (Hermes docker run launcher)_1]]

## Top bridge nodes
- [[hermes_dashboard_proxy (hermes-dashboard{path} HTTP reverse proxy)]] - degree 14, connects to 5 communities
- [[hermes_dashboard_ws_proxy (WebSocket relay)]] - degree 13, connects to 2 communities
- [[TestHermesDashboardPathTraversal]] - degree 10, connects to 1 community
- [[asyncio_1]] - degree 9, connects to 1 community
- [[TestHermesDashboardWsProxy]] - degree 9, connects to 1 community
