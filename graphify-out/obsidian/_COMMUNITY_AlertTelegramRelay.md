---
type: community
cohesion: 0.15
members: 35
---

# AlertTelegramRelay

**Cohesion:** 0.15 - loosely connected
**Members:** 35 nodes

## Members
- [[dot-__call__()_5]] - code - gateway/ingest_api/alert_telegram_relay.py
- [[dot-__call__()_6]] - code - gateway/tests/test_alert_telegram_relay.py
- [[dot-__init__()_81]] - code - gateway/ingest_api/alert_telegram_relay.py
- [[dot-__init__()_82]] - code - gateway/tests/test_alert_telegram_relay.py
- [[dot-_clean_tool()]] - code - gateway/ingest_api/alert_telegram_relay.py
- [[dot-_coerce()]] - code - gateway/ingest_api/alert_telegram_relay.py
- [[dot-_dedup_key()]] - code - gateway/ingest_api/alert_telegram_relay.py
- [[dot-_handle()]] - code - gateway/ingest_api/alert_telegram_relay.py
- [[dot-_spawn_send()]] - code - gateway/ingest_api/alert_telegram_relay.py
- [[dot-flush()]] - code - gateway/ingest_api/alert_telegram_relay.py
- [[Accept GatewayEvent objects or plain dicts from legacy emitters.]] - rationale - gateway/ingest_api/alert_telegram_relay.py
- [[AlertTelegramRelay]] - code - gateway/ingest_api/alert_telegram_relay.py
- [[Any_31]] - code - gateway/ingest_api/alert_telegram_relay.py
- [[Await in-flight sends (testshutdown helper).]] - rationale - gateway/ingest_api/alert_telegram_relay.py
- [[Subscribe to the gateway EventBus; relay security alerts to Telegram.]] - rationale - gateway/ingest_api/alert_telegram_relay.py
- [[_SendSpy]] - code - gateway/tests/test_alert_telegram_relay.py
- [[_alert_event()]] - code - gateway/tests/test_alert_telegram_relay.py
- [[alert_telegram_relay.py]] - code - gateway/ingest_api/alert_telegram_relay.py
- [[test_alert_telegram_relay.py]] - code - gateway/tests/test_alert_telegram_relay.py
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
- 7 edges to [[_COMMUNITY_make_event]]
- 2 edges to [[_COMMUNITY_AgentRegistry]]
- 2 edges to [[_COMMUNITY_AgentTarget]]
- 1 edge to [[_COMMUNITY_UserSessionManager]]
- 1 edge to [[_COMMUNITY_gatewayingest_apimain.py (hermes-dashboard HTTP + WebSocket reverse proxy)]]

## Top bridge nodes
- [[AlertTelegramRelay]] - degree 33, connects to 3 communities
- [[test_alert_telegram_relay.py]] - degree 23, connects to 2 communities
- [[_SendSpy]] - degree 21, connects to 1 community
- [[_alert_event()]] - degree 16, connects to 1 community
- [[test_subscribed_relay_receives_bus_emissions()]] - degree 5, connects to 1 community
