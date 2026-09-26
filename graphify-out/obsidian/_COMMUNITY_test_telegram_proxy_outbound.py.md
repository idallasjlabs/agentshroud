---
type: community
cohesion: 0.07
members: 59
---

# test_telegram_proxy_outbound.py

**Cohesion:** 0.07 - loosely connected
**Members:** 59 nodes

## Members
- [[.__call__()]] - code - gateway/ingest_api/alert_telegram_relay.py
- [[.__call__()_1]] - code - gateway/tests/test_alert_telegram_relay.py
- [[.__init__()_9]] - code - gateway/ingest_api/alert_telegram_relay.py
- [[.__init__()_12]] - code - gateway/ingest_api/event_bus.py
- [[.__init__()_140]] - code - gateway/tests/test_alert_telegram_relay.py
- [[._clean_tool()]] - code - gateway/ingest_api/alert_telegram_relay.py
- [[._coerce()]] - code - gateway/ingest_api/alert_telegram_relay.py
- [[._dedup_key()]] - code - gateway/ingest_api/alert_telegram_relay.py
- [[._handle()]] - code - gateway/ingest_api/alert_telegram_relay.py
- [[._spawn_send()]] - code - gateway/ingest_api/alert_telegram_relay.py
- [[.emit()]] - code - gateway/ingest_api/event_bus.py
- [[.filter()]] - code - gateway/ingest_api/lifespan.py
- [[.flush()]] - code - gateway/ingest_api/alert_telegram_relay.py
- [[.get_recent()]] - code - gateway/ingest_api/event_bus.py
- [[.get_stats()]] - code - gateway/ingest_api/event_bus.py
- [[.subscribe()]] - code - gateway/ingest_api/event_bus.py
- [[.to_dict()]] - code - gateway/ingest_api/event_bus.py
- [[.unsubscribe()]] - code - gateway/ingest_api/event_bus.py
- [[3+ auth failures within 5 minutes escalates event severity to critical]] - concept - gateway/tests/test_event_bus.py
- [[A single gateway event]] - rationale - gateway/ingest_api/event_bus.py
- [[Accept GatewayEvent objects or plain dicts from legacy emitters.]] - rationale - gateway/ingest_api/alert_telegram_relay.py
- [[AlertTelegramRelay]] - code - gateway/ingest_api/alert_telegram_relay.py
- [[Any_5]] - code - gateway/ingest_api/alert_telegram_relay.py
- [[Any_6]] - code - gateway/ingest_api/event_bus.py
- [[Await in-flight sends (testshutdown helper).]] - rationale - gateway/ingest_api/alert_telegram_relay.py
- [[Emit an event to all subscribers]] - rationale - gateway/ingest_api/event_bus.py
- [[EventBus]] - code - gateway/ingest_api/event_bus.py
- [[GatewayEvent]] - code - gateway/ingest_api/event_bus.py
- [[LogRecord]] - code - gateway/ingest_api/lifespan.py
- [[Regression (SCRUM-61) apialerts used to call event_bus.publish(),     a metho]] - rationale - gateway/tests/test_alert_telegram_relay.py
- [[Simple in-process event bus with async support]] - rationale - gateway/ingest_api/event_bus.py
- [[Subscribe to all events]] - rationale - gateway/ingest_api/event_bus.py
- [[Subscribe to the gateway EventBus; relay security alerts to Telegram.]] - rationale - gateway/ingest_api/alert_telegram_relay.py
- [[Suppress noisy uvicorn warning spam for malformed probe traffic.]] - rationale - gateway/ingest_api/lifespan.py
- [[Unsubscribe from events]] - rationale - gateway/ingest_api/event_bus.py
- [[_DropInvalidHTTPRequestFilter]] - code - gateway/ingest_api/lifespan.py
- [[_SendSpy]] - code - gateway/tests/test_alert_telegram_relay.py
- [[_alert_event()]] - code - gateway/tests/test_alert_telegram_relay.py
- [[alert_telegram_relay.py]] - code - gateway/ingest_api/alert_telegram_relay.py
- [[event_bus.py]] - code - gateway/ingest_api/event_bus.py
- [[event_bus.py_1]] - document - docs/vault/02 - Modules/Gateway Core/event_bus.py.md
- [[test_alert_telegram_relay.py]] - code - gateway/tests/test_alert_telegram_relay.py
- [[test_api_alerts_endpoint_emits_bus_event()]] - code - gateway/tests/test_alert_telegram_relay.py
- [[test_async_sanitizer_supported()]] - code - gateway/tests/test_alert_telegram_relay.py
- [[test_critical_alert_relayed_to_owner()]] - code - gateway/tests/test_alert_telegram_relay.py
- [[test_dedup_key_includes_source()]] - code - gateway/tests/test_alert_telegram_relay.py
- [[test_dedup_same_alert_sent_once()]] - code - gateway/tests/test_alert_telegram_relay.py
- [[test_final_text_capped_below_telegram_limit()]] - code - gateway/tests/test_alert_telegram_relay.py
- [[test_info_severity_not_relayed()]] - code - gateway/tests/test_alert_telegram_relay.py
- [[test_non_alert_events_ignored()]] - code - gateway/tests/test_alert_telegram_relay.py
- [[test_outgoing_text_passes_through_sanitizer()]] - code - gateway/tests/test_alert_telegram_relay.py
- [[test_plain_dict_event_tolerated()]] - code - gateway/tests/test_alert_telegram_relay.py
- [[test_rate_limit_caps_sends_per_hour()]] - code - gateway/tests/test_alert_telegram_relay.py
- [[test_send_failure_rolls_back_dedup_for_retry()]] - code - gateway/tests/test_alert_telegram_relay.py
- [[test_send_failure_swallowed()]] - code - gateway/tests/test_alert_telegram_relay.py
- [[test_subscribed_relay_receives_bus_emissions()]] - code - gateway/tests/test_alert_telegram_relay.py
- [[test_tool_field_control_chars_stripped_and_capped()]] - code - gateway/tests/test_alert_telegram_relay.py
- [[test_warning_alert_relayed_with_orange_marker()]] - code - gateway/tests/test_alert_telegram_relay.py
- [[test_warning_flood_cannot_starve_critical()]] - code - gateway/tests/test_alert_telegram_relay.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_telegram_proxy_outboundpy
SORT file.name ASC
```

## Connections to other communities
- 10 edges to [[_COMMUNITY_TestCollaboratorPromptClassifiers]]
- 9 edges to [[_COMMUNITY__wrap_response()]]
- 5 edges to [[_COMMUNITY_EgressPolicy]]
- 4 edges to [[_COMMUNITY_MiddlewareManager]]
- 3 edges to [[_COMMUNITY_ApprovalRequest]]
- 2 edges to [[_COMMUNITY_SSHProxy]]
- 2 edges to [[_COMMUNITY_TrustManager]]
- 2 edges to [[_COMMUNITY_ResourceGuard]]
- 2 edges to [[_COMMUNITY_KeyVaultConfig]]
- 1 edge to [[_COMMUNITY_A2APolicyEngine]]
- 1 edge to [[_COMMUNITY_RateLimiter]]
- 1 edge to [[_COMMUNITY_Socrates — Dialogue Architect]]
- 1 edge to [[_COMMUNITY_MCPToolCall]]
- 1 edge to [[_COMMUNITY_CredentialValidator]]
- 1 edge to [[_COMMUNITY_OpenClaw Host Hardening]]
- 1 edge to [[_COMMUNITY_PipelineAction]]

## Top bridge nodes
- [[_DropInvalidHTTPRequestFilter]] - degree 15, connects to 8 communities
- [[LogRecord]] - degree 10, connects to 6 communities
- [[event_bus.py]] - degree 9, connects to 6 communities
- [[EventBus]] - degree 25, connects to 4 communities
- [[event_bus.py_1]] - degree 5, connects to 3 communities