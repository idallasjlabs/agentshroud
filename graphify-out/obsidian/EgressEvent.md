---
source_file: "gateway/security/egress_monitor.py"
type: "code"
community: "Community 95"
location: "L40"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Community_95
---

# EgressEvent

## Connections
- [[.get_events()_2]] - `references` [EXTRACTED]
- [[.record()_1]] - `references` [EXTRACTED]
- [[.scan_response()]] - `calls` [EXTRACTED]
- [[.test_alert_has_description()]] - `calls` [EXTRACTED]
- [[.test_alert_has_severity()]] - `calls` [EXTRACTED]
- [[.test_alert_monitor_mode_no_block()]] - `calls` [EXTRACTED]
- [[.test_high_volume_triggers_alert()]] - `calls` [EXTRACTED]
- [[.test_normal_multi_channel_not_flagged()]] - `calls` [EXTRACTED]
- [[.test_normal_volume_no_alert()]] - `calls` [EXTRACTED]
- [[.test_record_dns_event()]] - `calls` [EXTRACTED]
- [[.test_record_file_event()]] - `calls` [EXTRACTED]
- [[.test_record_http_event()]] - `calls` [EXTRACTED]
- [[.test_record_mcp_event()]] - `calls` [EXTRACTED]
- [[.test_slow_drip_across_channels()]] - `calls` [EXTRACTED]
- [[.test_summary_report()]] - `calls` [EXTRACTED]
- [[.test_unusual_destination_flagged()]] - `calls` [EXTRACTED]
- [[MockEgressEvent]] - `shares_data_with` [AMBIGUOUS]
- [[TestAlertGeneration]] - `uses` [INFERRED]
- [[TestAnomalyDetection]] - `uses` [INFERRED]
- [[TestAuditTrail_1]] - `uses` [INFERRED]
- [[TestAuth_1]] - `uses` [INFERRED]
- [[TestConcurrency]] - `uses` [INFERRED]
- [[TestContainerSecurity]] - `uses` [INFERRED]
- [[TestContextGuard_1]] - `uses` [INFERRED]
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
- [[TestSupplyChain_1]] - `uses` [INFERRED]
- [[TestTimingAttacks]] - `uses` [INFERRED]
- [[TestWebSecurity]] - `uses` [INFERRED]
- [[egress_monitor.py]] - `contains` [EXTRACTED]
- [[test_egress_monitor.py]] - `imports` [EXTRACTED]
- [[test_security_audit.py]] - `imports` [EXTRACTED]
- [[web_proxy.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Community_95