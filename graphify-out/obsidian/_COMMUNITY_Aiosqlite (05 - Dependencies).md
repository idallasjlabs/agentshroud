---
type: community
cohesion: 0.08
members: 33
---

# Aiosqlite (05 - Dependencies)

**Cohesion:** 0.08 - loosely connected
**Members:** 33 nodes

## Members
- [[.query()]] - code - gateway/ingest_api/ledger.py
- [[Any_7]] - code - gateway/ingest_api/ledger.py
- [[Database Files]] - document - docs/vault/05 - Dependencies/aiosqlite.md
- [[Dependency Graph_1]] - document - docs/vault/09 - Diagrams/Dependency Graph.md
- [[Dependency Graph]] - document - docs/vault/09 - Diagrams/Dependency Graph.md
- [[ForwardResponse]] - code - gateway/ingest_api/models.py
- [[Gateway Module Dependencies]] - document - docs/vault/09 - Diagrams/Dependency Graph.md
- [[Gateway Startup Initialization Order]] - concept - docs/vault/09 - Diagrams/Dependency Graph.md
- [[Key Initialization Order (main.py lifespan)]] - document - docs/vault/09 - Diagrams/Dependency Graph.md
- [[LedgerConfig_1]] - code - gateway/ingest_api/ledger.py
- [[LedgerEntry_1]] - code - gateway/ingest_api/models.py
- [[LedgerEntry]] - code - gateway/ingest_api/ledger.py
- [[LedgerQueryResponse_1]] - code - gateway/ingest_api/models.py
- [[LedgerQueryResponse]] - code - gateway/ingest_api/ledger.py
- [[Paginated ledger query results]] - rationale - gateway/ingest_api/models.py
- [[Purpose_184]] - document - docs/vault/05 - Dependencies/aiosqlite.md
- [[Python Package Dependencies]] - document - docs/vault/09 - Diagrams/Dependency Graph.md
- [[Query ledger entries with pagination and filters          Args             page]] - rationale - gateway/ingest_api/ledger.py
- [[README_128]] - document - gateway/README.md
- [[Related Notes_39]] - document - docs/vault/05 - Dependencies/aiosqlite.md
- [[Related Notes_70]] - document - docs/vault/09 - Diagrams/Dependency Graph.md
- [[Response after content is ingested, sanitized, and logged]] - rationale - gateway/ingest_api/models.py
- [[Single entry from the data ledger]] - rationale - gateway/ingest_api/models.py
- [[WAL Mode]] - document - docs/vault/05 - Dependencies/aiosqlite.md
- [[WebSocket_2]] - code - gateway/ingest_api/main.py
- [[WebSocket relay for Slack Socket Mode inbound traffic.      Bot connects here (w]] - rationale - gateway/ingest_api/main.py
- [[Where Used]] - document - docs/vault/05 - Dependencies/aiosqlite.md
- [[aiosqlite_1]] - document - docs/vault/05 - Dependencies/aiosqlite.md
- [[aiosqlite]] - document - docs/vault/05 - Dependencies/aiosqlite.md
- [[ledger.py]] - code - gateway/ingest_api/ledger.py
- [[models.py]] - code - gateway/ingest_api/models.py
- [[slack_ws_relay()]] - code - gateway/ingest_api/main.py
- [[store.py]] - code - gateway/approval_queue/store.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Aiosqlite_05_-_Dependencies
SORT file.name ASC
```

## Connections to other communities
- 27 edges to [[_COMMUNITY_Ingest API Main & Models]]
- 13 edges to [[_COMMUNITY_Security Fixes & SSH Write Endpoint]]
- 4 edges to [[_COMMUNITY_Queue (approval_queue)]]
- 4 edges to [[_COMMUNITY_Security Audit & Watchtower Tests]]
- 4 edges to [[_COMMUNITY_RBAC & Ingest Middleware]]
- 4 edges to [[_COMMUNITY_Router]]
- 4 edges to [[_COMMUNITY_Forward (routes)]]
- 3 edges to [[_COMMUNITY_Router (soc)]]
- 3 edges to [[_COMMUNITY_Auth]]
- 3 edges to [[_COMMUNITY_Audit Export]]
- 2 edges to [[_COMMUNITY_Container errors (07 - Errors & Troubleshooting)]]
- 2 edges to [[_COMMUNITY_Config]]
- 2 edges to [[_COMMUNITY_Main Simple]]
- 2 edges to [[_COMMUNITY_Approval Queue]]
- 2 edges to [[_COMMUNITY_Soc Egress Endpoints]]
- 2 edges to [[_COMMUNITY_Tool Result Pii]]
- 1 edge to [[_COMMUNITY_Enhanced Approval]]
- 1 edge to [[_COMMUNITY_Mfa Guard]]
- 1 edge to [[_COMMUNITY_Egress Approval (security)]]
- 1 edge to [[_COMMUNITY_Config Validation & Router]]
- 1 edge to [[_COMMUNITY_Ci Workflows (03 - Configuration)]]
- 1 edge to [[_COMMUNITY_Network topology (09 - Diagrams)]]
- 1 edge to [[_COMMUNITY_Readme (gateway)]]

## Top bridge nodes
- [[models.py]] - degree 28, connects to 10 communities
- [[README_128]] - degree 11, connects to 8 communities
- [[WebSocket_2]] - degree 15, connects to 5 communities
- [[LedgerEntry_1]] - degree 19, connects to 4 communities
- [[LedgerQueryResponse_1]] - degree 19, connects to 4 communities