---
source_file: "gateway/tests/test_alert_telegram_relay.py"
type: "code"
community: "Gateway Test Suite"
location: "L12"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Gateway_Test_Suite
---

# _SendSpy

## Connections
- [[.__call__()_1]] - `method` [EXTRACTED]
- [[.__init__()_136]] - `method` [EXTRACTED]
- [[AlertTelegramRelay]] - `uses` [INFERRED]
- [[EventBus]] - `uses` [INFERRED]
- [[test_alert_telegram_relay.py]] - `contains` [EXTRACTED]
- [[test_async_sanitizer_supported()]] - `calls` [EXTRACTED]
- [[test_critical_alert_relayed_to_owner()]] - `calls` [EXTRACTED]
- [[test_dedup_key_includes_source()]] - `calls` [EXTRACTED]
- [[test_dedup_same_alert_sent_once()]] - `calls` [EXTRACTED]
- [[test_final_text_capped_below_telegram_limit()]] - `calls` [EXTRACTED]
- [[test_info_severity_not_relayed()]] - `calls` [EXTRACTED]
- [[test_non_alert_events_ignored()]] - `calls` [EXTRACTED]
- [[test_outgoing_text_passes_through_sanitizer()]] - `calls` [EXTRACTED]
- [[test_plain_dict_event_tolerated()]] - `calls` [EXTRACTED]
- [[test_rate_limit_caps_sends_per_hour()]] - `calls` [EXTRACTED]
- [[test_send_failure_rolls_back_dedup_for_retry()]] - `calls` [EXTRACTED]
- [[test_send_failure_swallowed()]] - `calls` [EXTRACTED]
- [[test_subscribed_relay_receives_bus_emissions()]] - `calls` [EXTRACTED]
- [[test_tool_field_control_chars_stripped_and_capped()]] - `calls` [EXTRACTED]
- [[test_warning_alert_relayed_with_orange_marker()]] - `calls` [EXTRACTED]
- [[test_warning_flood_cannot_starve_critical()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Gateway_Test_Suite