---
source_file: "gateway/ingest_api/alert_telegram_relay.py"
type: "code"
community: "AlertTelegramRelay"
location: "L52"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/AlertTelegramRelay
---

# AlertTelegramRelay

## Connections
- [[dot-__call__()_3]] - `method` [EXTRACTED]
- [[dot-__init__()_37]] - `method` [EXTRACTED]
- [[dot-_clean_tool()]] - `method` [EXTRACTED]
- [[dot-_coerce()]] - `method` [EXTRACTED]
- [[dot-_dedup_key()]] - `method` [EXTRACTED]
- [[dot-_handle()]] - `method` [EXTRACTED]
- [[dot-_spawn_send()]] - `method` [EXTRACTED]
- [[dot-flush()]] - `method` [EXTRACTED]
- [[Subscribe to the gateway EventBus; relay security alerts to Telegram.]] - `rationale_for` [EXTRACTED]
- [[alert_telegram_relay.py]] - `contains` [EXTRACTED]
- [[lifespan()]] - `uses` [INFERRED]
- [[lifespan.py]] - `imports` [EXTRACTED]
- [[test_alert_telegram_relay.py]] - `imports` [EXTRACTED]
- [[test_async_sanitizer_supported()]] - `uses` [INFERRED]
- [[test_critical_alert_relayed_to_owner()]] - `uses` [INFERRED]
- [[test_dedup_key_includes_source()]] - `uses` [INFERRED]
- [[test_dedup_same_alert_sent_once()]] - `uses` [INFERRED]
- [[test_final_text_capped_below_telegram_limit()]] - `uses` [INFERRED]
- [[test_info_severity_not_relayed()]] - `uses` [INFERRED]
- [[test_non_alert_events_ignored()]] - `uses` [INFERRED]
- [[test_outgoing_text_passes_through_sanitizer()]] - `uses` [INFERRED]
- [[test_plain_dict_event_tolerated()]] - `uses` [INFERRED]
- [[test_rate_limit_caps_sends_per_hour()]] - `uses` [INFERRED]
- [[test_send_failure_rolls_back_dedup_for_retry()]] - `uses` [INFERRED]
- [[test_send_failure_swallowed()]] - `uses` [INFERRED]
- [[test_subscribed_relay_receives_bus_emissions()]] - `uses` [INFERRED]
- [[test_tool_field_control_chars_stripped_and_capped()]] - `uses` [INFERRED]
- [[test_warning_alert_relayed_with_orange_marker()]] - `uses` [INFERRED]
- [[test_warning_flood_cannot_starve_critical()]] - `uses` [INFERRED]

#graphify/code #graphify/INFERRED #community/AlertTelegramRelay
