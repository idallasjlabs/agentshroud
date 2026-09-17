---
source_file: "gateway/security/egress_monitor.py"
type: "code"
community: "Community 155"
location: "L40"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Community_155
---

# EgressEvent

## Connections
- [[dot-get_events()_2]] - `references` [EXTRACTED]
- [[dot-record()_1]] - `references` [EXTRACTED]
- [[dot-scan_response()_2]] - `calls` [EXTRACTED]
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
- [[MockEgressEvent]] - `shares_data_with` [AMBIGUOUS]
- [[TestAlertGeneration]] - `uses` [INFERRED]
- [[TestAnomalyDetection]] - `uses` [INFERRED]
- [[TestAuditTrail]] - `uses` [INFERRED]
- [[TestAuth]] - `uses` [INFERRED]
- [[TestConcurrency]] - `uses` [INFERRED]
- [[TestContainerSecurity]] - `uses` [INFERRED]
- [[TestContextGuard]] - `uses` [INFERRED]
- [[TestCryptography]] - `uses` [INFERRED]
- [[TestDailySummary]] - `uses` [INFERRED]
- [[TestDependencySecurity]] - `uses` [INFERRED]
- [[TestDoSPrevention]] - `uses` [INFERRED]
- [[TestEgressMonitorConfig]] - `uses` [INFERRED]
- [[TestEventRecording]] - `uses` [INFERRED]
- [[TestExfiltrationDetection]] - `uses` [INFERRED]
- [[TestFileSandbox]] - `uses` [INFERRED]
- [[TestHTTPSecurity]] - `uses` [INFERRED]
- [[TestInfoLeakage]] - `uses` [INFERRED]
- [[TestLoggingSecurity]] - `uses` [INFERRED]
- [[TestMCPSecurity]] - `uses` [INFERRED]
- [[TestNetworkSecurity]] - `uses` [INFERRED]
- [[TestPIIDetection_1]] - `uses` [INFERRED]
- [[TestPrivilegeEscalation]] - `uses` [INFERRED]
- [[TestPromptGuard]] - `uses` [INFERRED]
- [[TestResourceProtection]] - `uses` [INFERRED]
- [[TestSlowDripDetection]] - `uses` [INFERRED]
- [[TestSupplyChain]] - `uses` [INFERRED]
- [[TestTimingAttacks]] - `uses` [INFERRED]
- [[TestWebSecurity]] - `uses` [INFERRED]
- [[egress_monitor.py]] - `contains` [EXTRACTED]
- [[test_egress_monitor.py]] - `imports` [EXTRACTED]
- [[test_security_audit.py]] - `imports` [EXTRACTED]
- [[web_proxy.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Community_155