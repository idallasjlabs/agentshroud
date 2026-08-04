---
type: community
cohesion: 0.10
members: 29
---

# Module Group 163

**Cohesion:** 0.10 - loosely connected
**Members:** 29 nodes

## Members
- [[.test_clean_when_installed_not_running()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_get_fim_events()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_get_rootkit_events()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_level_to_severity()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_not_run_when_no_alert_dir()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_parse_empty()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_parse_fim_event()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_parse_rootkit_event()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_returns_summary_for_empty_dir()]] - code - gateway/tests/test_scanner_integration.py
- [[Any_58]] - code - gateway/security/wazuh_client.py
- [[Filter alerts to file integrity monitoring events only.      Args         alert]] - rationale - gateway/security/wazuh_client.py
- [[Filter alerts to rootkit detection events only.      Args         alerts List]] - rationale - gateway/security/wazuh_client.py
- [[Generate a summary dict suitable for the health report.      Args         alert_1]] - rationale - gateway/security/wazuh_client.py
- [[Map Wazuh alert level to severity string.      Args         level Wazuh alert]] - rationale - gateway/security/wazuh_client.py
- [[Parse a single Wazuh alert.      Args         raw Raw Wazuh alert JSON.      R]] - rationale - gateway/security/wazuh_client.py
- [[Path_18]] - code - gateway/security/wazuh_client.py
- [[Read Wazuh alerts from the alert directory.      Args         alert_dir Direct]] - rationale - gateway/security/wazuh_client.py
- [[Return latest Falco alert summary from the local alert directory.      CC-20 If]] - rationale - gateway/security/scanner_integration.py
- [[TestGetFalcoSummary]] - code - gateway/tests/test_scanner_integration.py
- [[TestWazuhParser]] - code - gateway/tests/test_security_toolchain.py
- [[datetime_3]] - code - gateway/security/wazuh_client.py
- [[generate_summary()_3]] - code - gateway/security/wazuh_client.py
- [[get_falco_summary()]] - code - gateway/security/scanner_integration.py
- [[get_fim_events()]] - code - gateway/security/wazuh_client.py
- [[get_rootkit_events()]] - code - gateway/security/wazuh_client.py
- [[level_to_severity()]] - code - gateway/security/wazuh_client.py
- [[parse_alert()_1]] - code - gateway/security/wazuh_client.py
- [[read_alerts()_1]] - code - gateway/security/wazuh_client.py
- [[wazuh_client.py]] - code - gateway/security/wazuh_client.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_163
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_Module Group 141]]
- 5 edges to [[_COMMUNITY_Security Scanner Integration]]
- 4 edges to [[_COMMUNITY_Module Group 228]]
- 2 edges to [[_COMMUNITY_Module Group 210]]
- 2 edges to [[_COMMUNITY_Scanner Integration Tests]]
- 1 edge to [[_COMMUNITY_Gateway Config & Lifespan]]
- 1 edge to [[_COMMUNITY_CLI & Core Gateway Routes]]
- 1 edge to [[_COMMUNITY_Alert Dispatcher]]
- 1 edge to [[_COMMUNITY_Module Group 381]]
- 1 edge to [[_COMMUNITY_Module Group 437]]
- 1 edge to [[_COMMUNITY_Module Group 134]]
- 1 edge to [[_COMMUNITY_PII Sanitizer & Resource Guard]]

## Top bridge nodes
- [[generate_summary()_3]] - degree 12, connects to 6 communities
- [[get_falco_summary()]] - degree 13, connects to 4 communities
- [[wazuh_client.py]] - degree 10, connects to 3 communities
- [[read_alerts()_1]] - degree 9, connects to 2 communities
- [[TestWazuhParser]] - degree 8, connects to 2 communities
