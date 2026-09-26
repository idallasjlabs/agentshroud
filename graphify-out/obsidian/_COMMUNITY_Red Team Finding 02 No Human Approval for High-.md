---
type: community
cohesion: 0.50
members: 4
---

# Red Team Finding 02: No Human Approval for High-

**Cohesion:** 0.50 - moderately connected
**Members:** 4 nodes

## Members
- [[.test_collaborator_aws_credentials_probe_is_blocked_and_quarantined()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_collaborator_metadata_endpoint_probe_is_blocked_and_quarantined()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[AWS credentials path probes should be blocked and quarantined.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Cloud metadata endpoint probes should be blocked and quarantined.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Red_Team_Finding_02_No_Human_Approval_for_High-
SORT file.name ASC
```

## Connections to other communities
- 10 edges to [[_COMMUNITY_ingest_apimain.py]]
- 2 edges to [[_COMMUNITY_test_soc_bots.py]]

## Top bridge nodes
- [[.test_collaborator_metadata_endpoint_probe_is_blocked_and_quarantined()]] - degree 8, connects to 2 communities
- [[.test_collaborator_aws_credentials_probe_is_blocked_and_quarantined()]] - degree 7, connects to 2 communities