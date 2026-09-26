---
type: community
cohesion: 0.67
members: 3
---

# .test_allowed_collaborator_model_command_with_me

**Cohesion:** 0.67 - moderately connected
**Members:** 3 nodes

## Members
- [[.__init__()_13]] - code - gateway/ingest_api/ledger.py
- [[LedgerConfig_1]] - code - gateway/ingest_api/ledger.py
- [[Store configuration          Actual database connection created in initialize().]] - rationale - gateway/ingest_api/ledger.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_allowed_collaborator_model_command_with_me
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_EgressPolicy]]
- 2 edges to [[_COMMUNITY_SSHProxy]]

## Top bridge nodes
- [[LedgerConfig_1]] - degree 4, connects to 2 communities
- [[.__init__()_13]] - degree 3, connects to 1 community