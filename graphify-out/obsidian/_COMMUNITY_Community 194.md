---
type: community
cohesion: 0.14
members: 37
---

# Community 194

**Cohesion:** 0.14 - loosely connected
**Members:** 37 nodes

## Members
- [[dot-__call__()_3]] - code - gateway/ingest_api/alert_telegram_relay.py
- [[dot-__call__()_4]] - code - gateway/tests/test_alert_telegram_relay.py
- [[dot-__init__()_85]] - code - gateway/ingest_api/alert_telegram_relay.py
- [[dot-__init__()_86]] - code - gateway/tests/test_alert_telegram_relay.py
- [[dot-_clean_tool()]] - code - gateway/ingest_api/alert_telegram_relay.py
- [[dot-_coerce()]] - code - gateway/ingest_api/alert_telegram_relay.py
- [[dot-_dedup_key()]] - code - gateway/ingest_api/alert_telegram_relay.py
- [[dot-_handle()_1]] - code - gateway/ingest_api/alert_telegram_relay.py
- [[dot-_spawn_send()]] - code - gateway/ingest_api/alert_telegram_relay.py
- [[dot-flush()]] - code - gateway/ingest_api/alert_telegram_relay.py
- [[Accept GatewayEvent objects or plain dicts from legacy emitters.]] - rationale - gateway/ingest_api/alert_telegram_relay.py
- [[AlertTelegramRelay]] - code - gateway/ingest_api/alert_telegram_relay.py
- [[Any_30]] - code - gateway/ingest_api/alert_telegram_relay.py
- [[Await in-flight sends (testshutdown helper).]] - rationale - gateway/ingest_api/alert_telegram_relay.py
- [[Regression (SCRUM-61) apialerts used to call event_bus.publish(),     a metho]] - rationale - gateway/tests/test_alert_telegram_relay.py
- [[Subscribe to the gateway EventBus; relay security alerts to Telegram.]] - rationale - gateway/ingest_api/alert_telegram_relay.py
- [[_SendSpy]] - code - gateway/tests/test_alert_telegram_relay.py
- [[_alert_event()]] - code - gateway/tests/test_alert_telegram_relay.py
- [[alert_telegram_relay.py]] - code - gateway/ingest_api/alert_telegram_relay.py
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
TABLE source_file, type FROM #community/Community_194
SORT file.name ASC
```

## Connections to other communities
- 9 edges to [[_COMMUNITY_Approval Routing & Event Bus]]
- 3 edges to [[_COMMUNITY_Community 116]]
- 1 edge to [[_COMMUNITY_Ingest API & RBAC Core]]
- 1 edge to [[_COMMUNITY_Ingest Middleware & File Sandbox]]

## Top bridge nodes
- [[test_alert_telegram_relay.py]] - degree 23, connects to 3 communities
- [[test_api_alerts_endpoint_emits_bus_event()]] - degree 4, connects to 2 communities
- [[AlertTelegramRelay]] - degree 33, connects to 1 community
- [[_SendSpy]] - degree 21, connects to 1 community
- [[_alert_event()]] - degree 16, connects to 1 community