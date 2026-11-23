---
source_file: "gateway/security/egress_monitor.py"
type: "code"
community: "EgressEvent"
location: "L40"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/EgressEvent
---

# EgressEvent

## Connections
- [[dot-get_events()_1]] - `references` [EXTRACTED]
- [[dot-record()]] - `references` [EXTRACTED]
- [[dot-scan_response()]] - `calls` [EXTRACTED]
- [[dot-test_alert_has_description()]] - `calls` [EXTRACTED]
- [[dot-test_alert_has_severity()]] - `calls` [EXTRACTED]
- [[dot-test_alert_monitor_mode_no_block()]] - `calls` [EXTRACTED]
- [[dot-test_high_volume_triggers_alert()]] - `calls` [EXTRACTED]
- [[dot-test_normal_multi_channel_not_flagged()]] - `calls` [EXTRACTED]
- [[dot-test_normal_volume_no_alert()]] - `calls` [EXTRACTED]
- [[dot-test_record_dns_event()]] - `calls` [EXTRACTED]
- [[dot-test_record_file_event()]] - `calls` [EXTRACTED]
- [[dot-test_record_http_event()]] - `calls` [EXTRACTED]
- [[dot-test_record_mcp_event()]] - `calls` [EXTRACTED]
- [[dot-test_slow_drip_across_channels()]] - `calls` [EXTRACTED]
- [[dot-test_summary_report()]] - `calls` [EXTRACTED]
- [[dot-test_unusual_destination_flagged()]] - `calls` [EXTRACTED]
- [[TestAlertGeneration]] - `uses` [INFERRED]
- [[TestAnomalyDetection_1]] - `uses` [INFERRED]
- [[TestDailySummary]] - `uses` [INFERRED]
- [[TestEventRecording]] - `uses` [INFERRED]
- [[TestExfiltrationDetection]] - `uses` [INFERRED]
- [[TestNetworkSecurity]] - `uses` [INFERRED]
- [[TestSlowDripDetection]] - `uses` [INFERRED]
- [[WebProxy]] - `uses` [INFERRED]
- [[egress_monitor.py_2]] - `contains` [EXTRACTED]
- [[test_egress_monitor.py]] - `imports` [EXTRACTED]
- [[test_security_audit.py]] - `imports` [EXTRACTED]
- [[web_proxy.py_2]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/EgressEvent
