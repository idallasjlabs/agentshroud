---
source_file: "gateway/tests/test_alert_telegram_relay.py"
type: "code"
community: "Gateway Test Suite"
location: "L1"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Gateway_Test_Suite
---

# test_alert_telegram_relay.py

## Connections
- [[AlertTelegramRelay]] - `imports` [EXTRACTED]
- [[EventBus]] - `imports` [EXTRACTED]
- [[_SendSpy]] - `contains` [EXTRACTED]
- [[_alert_event()]] - `contains` [EXTRACTED]
- [[main.py_2]] - `imports_from` [EXTRACTED]
- [[make_event()]] - `imports` [EXTRACTED]
- [[test_api_alerts_endpoint_emits_bus_event()]] - `contains` [EXTRACTED]
- [[test_async_sanitizer_supported()]] - `contains` [EXTRACTED]
- [[test_critical_alert_relayed_to_owner()]] - `contains` [EXTRACTED]
- [[test_dedup_key_includes_source()]] - `contains` [EXTRACTED]
- [[test_dedup_same_alert_sent_once()]] - `contains` [EXTRACTED]
- [[test_final_text_capped_below_telegram_limit()]] - `contains` [EXTRACTED]
- [[test_info_severity_not_relayed()]] - `contains` [EXTRACTED]
- [[test_non_alert_events_ignored()]] - `contains` [EXTRACTED]
- [[test_outgoing_text_passes_through_sanitizer()]] - `contains` [EXTRACTED]
- [[test_plain_dict_event_tolerated()]] - `contains` [EXTRACTED]
- [[test_rate_limit_caps_sends_per_hour()]] - `contains` [EXTRACTED]
- [[test_send_failure_rolls_back_dedup_for_retry()]] - `contains` [EXTRACTED]
- [[test_send_failure_swallowed()]] - `contains` [EXTRACTED]
- [[test_subscribed_relay_receives_bus_emissions()]] - `contains` [EXTRACTED]
- [[test_tool_field_control_chars_stripped_and_capped()]] - `contains` [EXTRACTED]
- [[test_warning_alert_relayed_with_orange_marker()]] - `contains` [EXTRACTED]
- [[test_warning_flood_cannot_starve_critical()]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Gateway_Test_Suite