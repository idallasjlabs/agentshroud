---
source_file: "gateway/ingest_api/event_bus.py"
type: "code"
community: "Community 116"
location: "L110"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Community_116
---

# make_event()

## Connections
- [[dot-_emit_privacy_event()]] - `calls` [EXTRACTED]
- [[dot-_emit_quarantine_event()]] - `calls` [EXTRACTED]
- [[dot-_record()]] - `calls` [EXTRACTED]
- [[dot-approve()]] - `calls` [EXTRACTED]
- [[dot-check_async()]] - `calls` [EXTRACTED]
- [[dot-deny()]] - `calls` [EXTRACTED]
- [[dot-request_approval()]] - `calls` [EXTRACTED]
- [[Any_22]] - `references` [EXTRACTED]
- [[GatewayEvent]] - `references` [EXTRACTED]
- [[Helper to create a GatewayEvent with current timestamp]] - `rationale_for` [EXTRACTED]
- [[_alert_event()]] - `calls` [EXTRACTED]
- [[_record_scanner_result()]] - `calls` [EXTRACTED]
- [[activity_websocket()]] - `calls` [EXTRACTED]
- [[approval.py]] - `imports` [EXTRACTED]
- [[approval_websocket()]] - `calls` [EXTRACTED]
- [[dashboard.py]] - `imports` [EXTRACTED]
- [[decide_approval()]] - `calls` [EXTRACTED]
- [[discard_blocked_message()]] - `calls` [EXTRACTED]
- [[discard_blocked_outbound()]] - `calls` [EXTRACTED]
- [[egress_add_rule()]] - `calls` [EXTRACTED]
- [[egress_approval.py]] - `imports` [EXTRACTED]
- [[egress_filter.py_1]] - `imports` [EXTRACTED]
- [[egress_remove_rule()]] - `calls` [EXTRACTED]
- [[egress_websocket()]] - `calls` [EXTRACTED]
- [[event_bus.py]] - `contains` [EXTRACTED]
- [[event_bus.py_1]] - `references` [EXTRACTED]
- [[forward.py]] - `imports` [EXTRACTED]
- [[forward_content()]] - `calls` [EXTRACTED]
- [[ingest_apimain.py]] - `imports` [EXTRACTED]
- [[mcp_proxy.py]] - `imports` [EXTRACTED]
- [[receive_security_alert()]] - `calls` [EXTRACTED]
- [[release_blocked_message()]] - `calls` [EXTRACTED]
- [[release_blocked_outbound()]] - `calls` [EXTRACTED]
- [[submit_approval_request()]] - `calls` [EXTRACTED]
- [[telegram_proxy.py]] - `imports` [EXTRACTED]
- [[test_alert_telegram_relay.py]] - `imports` [EXTRACTED]
- [[test_async_subscriber()]] - `calls` [EXTRACTED]
- [[test_auth_failure_escalation()]] - `calls` [EXTRACTED]
- [[test_dashboard.py]] - `imports` [EXTRACTED]
- [[test_emit_no_subscribers_no_error()]] - `calls` [EXTRACTED]
- [[test_emit_to_multiple_subscribers()]] - `calls` [EXTRACTED]
- [[test_event_bus.py]] - `imports` [EXTRACTED]
- [[test_event_has_required_fields()]] - `calls` [EXTRACTED]
- [[test_get_recent()]] - `calls` [EXTRACTED]
- [[test_get_stats()]] - `calls` [EXTRACTED]
- [[test_manage_soc_events_endpoint()]] - `calls` [EXTRACTED]
- [[test_manage_soc_report_endpoint()]] - `calls` [EXTRACTED]
- [[test_non_alert_events_ignored()]] - `calls` [EXTRACTED]
- [[test_soc_egress_endpoints.py]] - `imports` [EXTRACTED]
- [[test_subscribe_receive_events()]] - `calls` [EXTRACTED]
- [[test_unsubscribe_stops_events()]] - `calls` [EXTRACTED]
- [[test_ws_activity_receives_events()]] - `calls` [EXTRACTED]
- [[test_ws_egress_receives_auth_event()]] - `calls` [EXTRACTED]
- [[test_ws_egress_receives_privacy_event()]] - `calls` [EXTRACTED]
- [[test_ws_egress_receives_scanner_event()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Community_116