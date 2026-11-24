---
type: community
members: 56
---

# web_proxy.py

**Members:** 56 nodes

## Members
- [[dot-__init__()_66]] - code - gateway/security/egress_monitor.py
- [[dot-check_anomalies()]] - code - gateway/security/egress_monitor.py
- [[dot-daily_summary()]] - code - gateway/security/egress_monitor.py
- [[dot-get_events()_1]] - code - gateway/security/egress_monitor.py
- [[dot-record()]] - code - gateway/security/egress_monitor.py
- [[dot-test_alert_has_description()]] - code - gateway/tests/test_egress_monitor.py
- [[dot-test_alert_has_severity()]] - code - gateway/tests/test_egress_monitor.py
- [[dot-test_alert_monitor_mode_no_block()]] - code - gateway/tests/test_egress_monitor.py
- [[dot-test_default_mode_is_enforce()_2]] - code - gateway/tests/test_egress_monitor.py
- [[dot-test_empty_summary()]] - code - gateway/tests/test_egress_monitor.py
- [[dot-test_generous_baselines()]] - code - gateway/tests/test_egress_monitor.py
- [[dot-test_high_volume_triggers_alert()]] - code - gateway/tests/test_egress_monitor.py
- [[dot-test_normal_multi_channel_not_flagged()]] - code - gateway/tests/test_egress_monitor.py
- [[dot-test_normal_volume_no_alert()]] - code - gateway/tests/test_egress_monitor.py
- [[dot-test_passthrough_adds_header()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_passthrough_allows_everything()_1]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_passthrough_skips_content_scan()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_record_dns_event()]] - code - gateway/tests/test_egress_monitor.py
- [[dot-test_record_file_event()]] - code - gateway/tests/test_egress_monitor.py
- [[dot-test_record_http_event()]] - code - gateway/tests/test_egress_monitor.py
- [[dot-test_record_mcp_event()]] - code - gateway/tests/test_egress_monitor.py
- [[dot-test_slow_drip_across_channels()]] - code - gateway/tests/test_egress_monitor.py
- [[dot-test_summary_report()]] - code - gateway/tests/test_egress_monitor.py
- [[dot-test_unusual_destination_flagged()]] - code - gateway/tests/test_egress_monitor.py
- [[AlertSeverity]] - code - gateway/security/egress_monitor.py
- [[Alerts in monitor mode should never block.]] - rationale - gateway/tests/test_egress_monitor.py
- [[AnomalyAlert]] - code - gateway/security/egress_monitor.py
- [[Default mode is enforce after v0.8.0 enforcement hardening._1]] - rationale - gateway/tests/test_egress_monitor.py
- [[EgressChannel]] - code - gateway/security/egress_monitor.py
- [[EgressEvent]] - code - gateway/security/egress_monitor.py
- [[EgressMonitor]] - code - gateway/security/egress_monitor.py
- [[EgressMonitorConfig]] - code - gateway/security/egress_monitor.py
- [[EgressSummary]] - code - gateway/security/egress_monitor.py
- [[Enum_15]] - code
- [[Enum_16]] - code
- [[IntEnum_1]] - code
- [[Normal usage across channels should not trigger drip detection.]] - rationale - gateway/tests/test_egress_monitor.py
- [[ProxyAction]] - code - gateway/proxy/web_proxy.py
- [[Small amounts across multiple channels should be detected.]] - rationale - gateway/tests/test_egress_monitor.py
- [[TestAlertGeneration]] - code - gateway/tests/test_egress_monitor.py
- [[TestAnomalyDetection_1]] - code - gateway/tests/test_egress_monitor.py
- [[TestDailySummary]] - code - gateway/tests/test_egress_monitor.py
- [[TestEgressMonitorConfig]] - code - gateway/tests/test_egress_monitor.py
- [[TestEventRecording]] - code - gateway/tests/test_egress_monitor.py
- [[TestPassthroughMode_1]] - code - gateway/tests/test_web_proxy.py
- [[TestSlowDripDetection]] - code - gateway/tests/test_egress_monitor.py
- [[Tests for unified egress monitoring.]] - rationale - gateway/tests/test_egress_monitor.py
- [[default_config()_2]] - code - gateway/tests/test_egress_monitor.py
- [[egress_monitor.py_2]] - code - gateway/security/egress_monitor.py
- [[fixture_40]] - code
- [[monitor()]] - code - gateway/tests/test_egress_monitor.py
- [[monitor_config()_1]] - code - gateway/tests/test_egress_monitor.py
- [[str_9]] - code
- [[str_10]] - code
- [[test_egress_monitor.py]] - code - gateway/tests/test_egress_monitor.py
- [[web_proxy.py_2]] - code - gateway/proxy/web_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/web_proxypy
SORT file.name ASC
```

## Connections to other communities
- 15 edges to [[_COMMUNITY_WebProxy]]
- 4 edges to [[_COMMUNITY_MiddlewareManager]]
- 3 edges to [[_COMMUNITY_DNSFilterConfig]]
- 3 edges to [[_COMMUNITY_test_security_audit.py]]
- 3 edges to [[_COMMUNITY_middleware.py]]
- 3 edges to [[_COMMUNITY_lifespan.py]]
- 2 edges to [[_COMMUNITY_WebProxyResult]]
- 2 edges to [[_COMMUNITY_URLAnalyzer]]
- 2 edges to [[_COMMUNITY_EnvironmentGuard]]
- 2 edges to [[_COMMUNITY_TestWebProxySecurityIntegration]]
- 2 edges to [[_COMMUNITY_SubagentMonitor]]
- 2 edges to [[_COMMUNITY_BrowserSecurityGuard]]
- 2 edges to [[_COMMUNITY_WebContentScanner]]
- 2 edges to [[_COMMUNITY_NetworkValidator]]
- 1 edge to [[_COMMUNITY_MetadataGuard]]
- 1 edge to [[_COMMUNITY_HTTPConnectProxy]]
- 1 edge to [[_COMMUNITY_test_http_proxy_coverage.py]]

## Top bridge nodes
- [[web_proxy.py_2]] - degree 30, connects to 11 communities
- [[EgressEvent]] - degree 28, connects to 5 communities
- [[EgressMonitorConfig]] - degree 14, connects to 5 communities
- [[EgressMonitor]] - degree 14, connects to 3 communities
- [[EgressChannel]] - degree 13, connects to 2 communities
