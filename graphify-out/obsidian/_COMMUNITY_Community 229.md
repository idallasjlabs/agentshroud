---
type: community
members: 56
---

# Community 229

**Members:** 56 nodes

## Members
- [[.__call__()_1]] - code - gateway/ingest_api/alert_telegram_relay.py
- [[.__init__()_24]] - code - gateway/ingest_api/alert_telegram_relay.py
- [[.__init__()_27]] - code - gateway/ingest_api/event_bus.py
- [[.__init__()_152]] - code - gateway/tests/test_alert_telegram_relay.py
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
- [[.test_fan_out_honours_edge_subscription()]] - code - gateway/tests/test_soc_edge.py
- [[.to_dict()]] - code - gateway/ingest_api/event_bus.py
- [[.unsubscribe()]] - code - gateway/ingest_api/event_bus.py
- [[3+ auth failures within 5 minutes escalates event severity to critical]] - concept - gateway/tests/test_event_bus.py
- [[A single gateway event]] - rationale - gateway/ingest_api/event_bus.py
- [[Accept GatewayEvent objects or plain dicts from legacy emitters.]] - rationale - gateway/ingest_api/alert_telegram_relay.py
- [[AlertTelegramRelay]] - code - gateway/ingest_api/alert_telegram_relay.py
- [[Any_15]] - code - gateway/ingest_api/alert_telegram_relay.py
- [[Any_16]] - code - gateway/ingest_api/event_bus.py
- [[Await in-flight sends (testshutdown helper).]] - rationale - gateway/ingest_api/alert_telegram_relay.py
- [[Emit an event to all subscribers]] - rationale - gateway/ingest_api/event_bus.py
- [[EventBus]] - code - gateway/ingest_api/event_bus.py
- [[GatewayEvent]] - code - gateway/ingest_api/event_bus.py
- [[LogRecord]] - code - gateway/ingest_api/lifespan.py
- [[Regression (SCRUM-61) apialerts used to call event_bus.publish(),     a metho]] - rationale - gateway/tests/test_alert_telegram_relay.py
- [[Simple in-process event bus with async support]] - rationale - gateway/ingest_api/event_bus.py
- [[Subscribe to all events]] - rationale - gateway/ingest_api/event_bus.py
- [[Subscribe to the gateway EventBus; relay security alerts to Telegram.]] - rationale - gateway/ingest_api/alert_telegram_relay.py
- [[Unsubscribe from events]] - rationale - gateway/ingest_api/event_bus.py
- [[_SendSpy]] - code - gateway/tests/test_alert_telegram_relay.py
- [[_alert_event()]] - code - gateway/tests/test_alert_telegram_relay.py
- [[alert_telegram_relay.py]] - code - gateway/ingest_api/alert_telegram_relay.py
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
TABLE source_file, type FROM #community/Community_229
SORT file.name ASC
```

## Connections to other communities
- 11 edges to [[_COMMUNITY_Community 62]]
- 10 edges to [[_COMMUNITY_Community 151]]
- 8 edges to [[_COMMUNITY_Community 80]]
- 4 edges to [[_COMMUNITY_Community 6]]
- 3 edges to [[_COMMUNITY_Community 7]]
- 2 edges to [[_COMMUNITY_Community 75]]
- 1 edge to [[_COMMUNITY_Community 309]]
- 1 edge to [[_COMMUNITY_Community 1]]
- 1 edge to [[_COMMUNITY_Community 84]]
- 1 edge to [[_COMMUNITY_Community 60]]
- 1 edge to [[_COMMUNITY_Community 978]]
- 1 edge to [[_COMMUNITY_Community 68]]
- 1 edge to [[_COMMUNITY_Community 34]]
- 1 edge to [[_COMMUNITY_Community 767]]
- 1 edge to [[_COMMUNITY_Community 94]]

## Top bridge nodes
- [[EventBus]] - degree 35, connects to 6 communities
- [[LogRecord]] - degree 10, connects to 5 communities
- [[event_bus.py_1]] - degree 5, connects to 3 communities
- [[.test_fan_out_honours_edge_subscription()]] - degree 4, connects to 3 communities
- [[test_alert_telegram_relay.py]] - degree 23, connects to 2 communities