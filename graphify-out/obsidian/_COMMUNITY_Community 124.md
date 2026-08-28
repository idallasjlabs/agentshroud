---
type: community
cohesion: 0.09
members: 48
---

# Community 124

**Cohesion:** 0.09 - loosely connected
**Members:** 48 nodes

## Members
- [[.__call__()]] - code - gateway/ingest_api/alert_telegram_relay.py
- [[.__call__()_1]] - code - gateway/tests/test_alert_telegram_relay.py
- [[.__init__()_9]] - code - gateway/ingest_api/alert_telegram_relay.py
- [[.__init__()_140]] - code - gateway/tests/test_alert_telegram_relay.py
- [[._clean_tool()]] - code - gateway/ingest_api/alert_telegram_relay.py
- [[._coerce()]] - code - gateway/ingest_api/alert_telegram_relay.py
- [[._dedup_key()]] - code - gateway/ingest_api/alert_telegram_relay.py
- [[._handle()]] - code - gateway/ingest_api/alert_telegram_relay.py
- [[._spawn_send()]] - code - gateway/ingest_api/alert_telegram_relay.py
- [[.flush()]] - code - gateway/ingest_api/alert_telegram_relay.py
- [[Accept GatewayEvent objects or plain dicts from legacy emitters.]] - rationale - gateway/ingest_api/alert_telegram_relay.py
- [[AlertTelegramRelay]] - code - gateway/ingest_api/alert_telegram_relay.py
- [[Any_5]] - code - gateway/ingest_api/alert_telegram_relay.py
- [[Await in-flight sends (testshutdown helper).]] - rationale - gateway/ingest_api/alert_telegram_relay.py
- [[Config Keys Read_1]] - document - docs/vault/02 - Modules/Gateway Core/event_bus.py.md
- [[Environment Variables Used]] - document - docs/vault/02 - Modules/Gateway Core/event_bus.py.md
- [[Event Types Emitted by main.py]] - document - docs/vault/02 - Modules/Gateway Core/event_bus.py.md
- [[EventBus.emit(event)]] - document - docs/vault/02 - Modules/Gateway Core/event_bus.py.md
- [[Function Details_1]] - document - docs/vault/02 - Modules/Gateway Core/event_bus.py.md
- [[Imports From  Exports To_1]] - document - docs/vault/02 - Modules/Gateway Core/event_bus.py.md
- [[Key Classes  Functions_1]] - document - docs/vault/02 - Modules/Gateway Core/event_bus.py.md
- [[Known Issues  Notes_1]] - document - docs/vault/02 - Modules/Gateway Core/event_bus.py.md
- [[Purpose_112]] - document - docs/vault/02 - Modules/Gateway Core/event_bus.py.md
- [[Related_2]] - document - docs/vault/02 - Modules/Gateway Core/event_bus.py.md
- [[Responsibilities_1]] - document - docs/vault/02 - Modules/Gateway Core/event_bus.py.md
- [[Subscribe to the gateway EventBus; relay security alerts to Telegram.]] - rationale - gateway/ingest_api/alert_telegram_relay.py
- [[_SendSpy]] - code - gateway/tests/test_alert_telegram_relay.py
- [[_alert_event()]] - code - gateway/tests/test_alert_telegram_relay.py
- [[alert_telegram_relay.py]] - code - gateway/ingest_api/alert_telegram_relay.py
- [[event_bus.py_2]] - document - docs/vault/02 - Modules/Gateway Core/event_bus.py.md
- [[make_event(event_type, summary, details, severity)]] - document - docs/vault/02 - Modules/Gateway Core/event_bus.py.md
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
TABLE source_file, type FROM #community/Community_124
SORT file.name ASC
```

## Connections to other communities
- 8 edges to [[_COMMUNITY_Community 21]]
- 4 edges to [[_COMMUNITY_Memory Lifecycle & Egress Filtering]]
- 1 edge to [[_COMMUNITY_Middleware & Lifespan]]
- 1 edge to [[_COMMUNITY_Ingest API & Approval Routes]]

## Top bridge nodes
- [[AlertTelegramRelay]] - degree 33, connects to 2 communities
- [[test_alert_telegram_relay.py]] - degree 23, connects to 2 communities
- [[_SendSpy]] - degree 21, connects to 1 community
- [[_alert_event()]] - degree 16, connects to 1 community
- [[event_bus.py_2]] - degree 11, connects to 1 community