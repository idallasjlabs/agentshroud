---
type: community
members: 21
---

# wazuh_client.py

**Members:** 21 nodes

## Members
- [[dot-test_get_fim_events()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_get_rootkit_events()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_level_to_severity()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_parse_empty()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_parse_fim_event()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_parse_rootkit_event()]] - code - gateway/tests/test_security_toolchain.py
- [[Any_37]] - code
- [[Filter alerts to file integrity monitoring events only. Args alerts List of…]] - rationale - gateway/security/wazuh_client.py
- [[Filter alerts to rootkit detection events only. Args alerts List of parsed…]] - rationale - gateway/security/wazuh_client.py
- [[Map Wazuh alert level to severity string. Args level Wazuh alert level…]] - rationale - gateway/security/wazuh_client.py
- [[Parse a single Wazuh alert. Args raw Raw Wazuh alert JSON. Returns Parsed…]] - rationale - gateway/security/wazuh_client.py
- [[Path_32]] - code
- [[Read Wazuh alerts from the alert directory. Args alert_dir Directory…]] - rationale - gateway/security/wazuh_client.py
- [[TestWazuhParser]] - code - gateway/tests/test_security_toolchain.py
- [[datetime_3]] - code
- [[get_fim_events()]] - code - gateway/security/wazuh_client.py
- [[get_rootkit_events()]] - code - gateway/security/wazuh_client.py
- [[level_to_severity()]] - code - gateway/security/wazuh_client.py
- [[parse_alert()_1]] - code - gateway/security/wazuh_client.py
- [[read_alerts()_1]] - code - gateway/security/wazuh_client.py
- [[wazuh_client.py_2]] - code - gateway/security/wazuh_client.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/wazuh_clientpy
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_test_security_toolchain.py]]
- 5 edges to [[_COMMUNITY_scanner_integration.py]]
- 4 edges to [[_COMMUNITY_ingest_apimain.py]]
- 1 edge to [[_COMMUNITY_get_falco_summary]]
- 1 edge to [[_COMMUNITY_get_wazuh_summary]]
- 1 edge to [[_COMMUNITY_lifespan.py]]
- 1 edge to [[_COMMUNITY_test_security_audit.py]]

## Top bridge nodes
- [[wazuh_client.py_2]] - degree 11, connects to 5 communities
- [[read_alerts()_1]] - degree 10, connects to 4 communities
- [[get_fim_events()]] - degree 7, connects to 3 communities
- [[get_rootkit_events()]] - degree 7, connects to 3 communities
- [[TestWazuhParser]] - degree 7, connects to 1 community
