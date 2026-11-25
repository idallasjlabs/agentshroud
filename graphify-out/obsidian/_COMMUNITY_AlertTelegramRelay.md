---
type: community
members: 45
---

# AlertTelegramRelay

**Members:** 45 nodes

## Members
- [[dot-__call__()_10]] - code - gateway/ingest_api/alert_telegram_relay.py
- [[dot-__call__()_11]] - code - gateway/tests/test_alert_telegram_relay.py
- [[dot-__init__()_166]] - code - gateway/ingest_api/alert_telegram_relay.py
- [[dot-__init__()_167]] - code - gateway/tests/test_alert_telegram_relay.py
- [[dot-_clean_tool()]] - code - gateway/ingest_api/alert_telegram_relay.py
- [[dot-_coerce()]] - code - gateway/ingest_api/alert_telegram_relay.py
- [[dot-_dedup_key()]] - code - gateway/ingest_api/alert_telegram_relay.py
- [[dot-_handle()]] - code - gateway/ingest_api/alert_telegram_relay.py
- [[dot-_spawn_send()]] - code - gateway/ingest_api/alert_telegram_relay.py
- [[dot-flush()]] - code - gateway/ingest_api/alert_telegram_relay.py
- [[dot-summary()]] - code - gateway/web/dashboard_endpoints.py
- [[Accept GatewayEvent objects or plain dicts from legacy emitters.]] - rationale - gateway/ingest_api/alert_telegram_relay.py
- [[Alert → owner Telegram relay (SCRUM-61). Event-bus subscriber that forwards…]] - rationale - gateway/ingest_api/alert_telegram_relay.py
- [[AlertTelegramRelay]] - code - gateway/ingest_api/alert_telegram_relay.py
- [[Any_62]] - code
- [[Await in-flight sends (testshutdown helper).]] - rationale - gateway/ingest_api/alert_telegram_relay.py
- [[Regression (SCRUM-61) apialerts used to call event_bus.publish(), a method…]] - rationale - gateway/tests/test_alert_telegram_relay.py
- [[Subscribe to the gateway EventBus; relay security alerts to Telegram.]] - rationale - gateway/ingest_api/alert_telegram_relay.py
- [[Tests for AlertTelegramRelay (SCRUM-61) — security_alert events → owner…]] - rationale - gateway/tests/test_alert_telegram_relay.py
- [[_SendSpy]] - code - gateway/tests/test_alert_telegram_relay.py
- [[_alert_event()]] - code - gateway/tests/test_alert_telegram_relay.py
- [[_capture()_2]] - code - gateway/tests/test_alert_telegram_relay.py
- [[_do_send()]] - code - gateway/ingest_api/alert_telegram_relay.py
- [[_san()_3]] - code - gateway/tests/test_alert_telegram_relay.py
- [[alert_telegram_relay.py]] - code - gateway/ingest_api/alert_telegram_relay.py
- [[asyncio_64]] - code
- [[json()_2]] - code - gateway/tests/test_alert_telegram_relay.py
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
TABLE source_file, type FROM #community/AlertTelegramRelay
SORT file.name ASC
```

## Connections to other communities
- 7 edges to [[_COMMUNITY_ingest_apimain.py]]
- 3 edges to [[_COMMUNITY_EventBus]]
- 1 edge to [[_COMMUNITY_lifespan.py]]
- 1 edge to [[_COMMUNITY_lifespan]]
- 1 edge to [[_COMMUNITY_test_dashboard_endpoints.py]]
- 1 edge to [[_COMMUNITY_Severity]]

## Top bridge nodes
- [[AlertTelegramRelay]] - degree 29, connects to 2 communities
- [[test_alert_telegram_relay.py]] - degree 26, connects to 2 communities
- [[test_api_alerts_endpoint_emits_bus_event()]] - degree 7, connects to 2 communities
- [[dot-summary()]] - degree 3, connects to 2 communities
- [[_alert_event()]] - degree 16, connects to 1 community
