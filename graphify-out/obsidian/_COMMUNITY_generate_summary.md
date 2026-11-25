---
type: community
members: 33
---

# generate_summary

**Members:** 33 nodes

## Members
- [[dot-test_clean_when_installed_not_running()_1]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_get_fim_events()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_get_rootkit_events()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_level_to_severity()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_not_run_when_no_alert_dir()_1]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_parse_empty()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_parse_fim_event()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_parse_rootkit_event()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_returns_summary_for_empty_dir()_1]] - code - gateway/tests/test_scanner_integration.py
- [[Any_38]] - code
- [[Filter alerts to file integrity monitoring events only. Args alerts List of…]] - rationale - gateway/security/wazuh_client.py
- [[Filter alerts to rootkit detection events only. Args alerts List of parsed…]] - rationale - gateway/security/wazuh_client.py
- [[Generate a summary dict suitable for the health report. Args alerts List of…_1]] - rationale - gateway/security/wazuh_client.py
- [[Map Wazuh alert level to severity string. Args level Wazuh alert level…]] - rationale - gateway/security/wazuh_client.py
- [[Parse a single Wazuh alert. Args raw Raw Wazuh alert JSON. Returns Parsed…]] - rationale - gateway/security/wazuh_client.py
- [[Path_30]] - code
- [[Read Wazuh alerts from the alert directory. Args alert_dir Directory…]] - rationale - gateway/security/wazuh_client.py
- [[Return True if a non-zombie falco process is running inside this container.]] - rationale - gateway/security/scanner_integration.py
- [[Return latest Falco alert summary from the local alert directory. CC-20 If…]] - rationale - gateway/security/scanner_integration.py
- [[Return recent Wazuh HIDS alerts with FIM and rootkit summary.]] - rationale - gateway/ingest_api/main.py
- [[TestGetFalcoSummary]] - code - gateway/tests/test_scanner_integration.py
- [[TestWazuhParser]] - code - gateway/tests/test_security_toolchain.py
- [[_is_falco_running()]] - code - gateway/security/scanner_integration.py
- [[datetime_3]] - code
- [[generate_summary()_2]] - code - gateway/security/wazuh_client.py
- [[get_falco_summary()]] - code - gateway/security/scanner_integration.py
- [[get_fim_events()]] - code - gateway/security/wazuh_client.py
- [[get_rootkit_events()]] - code - gateway/security/wazuh_client.py
- [[level_to_severity()]] - code - gateway/security/wazuh_client.py
- [[parse_alert()_1]] - code - gateway/security/wazuh_client.py
- [[read_alerts()_1]] - code - gateway/security/wazuh_client.py
- [[wazuh_alerts()]] - code - gateway/ingest_api/main.py
- [[wazuh_client.py_2]] - code - gateway/security/wazuh_client.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/generate_summary
SORT file.name ASC
```

## Connections to other communities
- 7 edges to [[_COMMUNITY_test_security_toolchain.py]]
- 4 edges to [[_COMMUNITY_ingest_apimain.py]]
- 4 edges to [[_COMMUNITY_scanner_integration.py]]
- 2 edges to [[_COMMUNITY_test_scanner_integration.py]]
- 2 edges to [[_COMMUNITY_get_wazuh_summary]]
- 2 edges to [[_COMMUNITY_Any]]
- 1 edge to [[_COMMUNITY_get_trivy_summary]]
- 1 edge to [[_COMMUNITY_aggregate_results]]
- 1 edge to [[_COMMUNITY_compute_scorecard]]
- 1 edge to [[_COMMUNITY_get_trivy_image_summaries]]
- 1 edge to [[_COMMUNITY_middleware.py]]
- 1 edge to [[_COMMUNITY_lifespan.py]]

## Top bridge nodes
- [[generate_summary()_2]] - degree 13, connects to 6 communities
- [[get_falco_summary()]] - degree 12, connects to 5 communities
- [[wazuh_client.py_2]] - degree 11, connects to 4 communities
- [[read_alerts()_1]] - degree 10, connects to 2 communities
- [[wazuh_alerts()]] - degree 8, connects to 1 community
