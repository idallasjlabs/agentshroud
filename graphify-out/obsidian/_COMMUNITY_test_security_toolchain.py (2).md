---
type: community
members: 21
---

# test_security_toolchain.py (2)

**Members:** 21 nodes

## Members
- [[dot-test_get_fim_events()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_get_rootkit_events()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_level_to_severity()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_parse_empty()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_parse_fim_event()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_parse_rootkit_event()]] - code - gateway/tests/test_security_toolchain.py
- [[Any_56]] - code - gateway/security/wazuh_client.py
- [[Filter alerts to file integrity monitoring events only.      Args         alert]] - rationale - gateway/security/wazuh_client.py
- [[Filter alerts to rootkit detection events only.      Args         alerts List]] - rationale - gateway/security/wazuh_client.py
- [[Map Wazuh alert level to severity string.      Args         level Wazuh alert]] - rationale - gateway/security/wazuh_client.py
- [[Parse a single Wazuh alert.      Args         raw Raw Wazuh alert JSON.      R]] - rationale - gateway/security/wazuh_client.py
- [[Path_44]] - code - gateway/security/wazuh_client.py
- [[Read Wazuh alerts from the alert directory.      Args         alert_dir Direct]] - rationale - gateway/security/wazuh_client.py
- [[TestWazuhParser]] - code - gateway/tests/test_security_toolchain.py
- [[datetime_5]] - code - gateway/security/wazuh_client.py
- [[get_fim_events()]] - code - gateway/security/wazuh_client.py
- [[get_rootkit_events()]] - code - gateway/security/wazuh_client.py
- [[level_to_severity()]] - code - gateway/security/wazuh_client.py
- [[parse_alert()_1]] - code - gateway/security/wazuh_client.py
- [[read_alerts()_1]] - code - gateway/security/wazuh_client.py
- [[wazuh_client.py]] - code - gateway/security/wazuh_client.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_security_toolchainpy_2
SORT file.name ASC
```

## Connections to other communities
- 10 edges to [[_COMMUNITY_test_security_toolchain.py]]
- 2 edges to [[_COMMUNITY_AlertDispatcher]]
- 2 edges to [[_COMMUNITY_FalcoAlertWatcher]]
- 1 edge to [[_COMMUNITY_test_collaborator_greeter.py (3)]]
- 1 edge to [[_COMMUNITY_ApprovalQueueConfig (7)]]
- 1 edge to [[_COMMUNITY_test_collaborator_greeter.py (2)]]
- 1 edge to [[_COMMUNITY_api.py]]
- 1 edge to [[_COMMUNITY_scanner_integration.py]]

## Top bridge nodes
- [[wazuh_client.py]] - degree 13, connects to 5 communities
- [[read_alerts()_1]] - degree 9, connects to 3 communities
- [[TestWazuhParser]] - degree 8, connects to 2 communities
- [[get_fim_events()]] - degree 6, connects to 1 community
- [[get_rootkit_events()]] - degree 6, connects to 1 community
