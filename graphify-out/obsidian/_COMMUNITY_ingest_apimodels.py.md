---
type: community
cohesion: 0.06
members: 42
---

# ingest_api/models.py

**Cohesion:** 0.06 - loosely connected
**Members:** 42 nodes

## Members
- [[dot-__init__()_55]] - code - gateway/ingest_api/ledger.py
- [[dot-body_not_empty()]] - code - gateway/ingest_api/models.py
- [[dot-get_entry()]] - code - gateway/ingest_api/ledger.py
- [[dot-get_stats()_6]] - code - gateway/ingest_api/ledger.py
- [[dot-path_not_empty()]] - code - gateway/ingest_api/models.py
- [[dot-query()]] - code - gateway/ingest_api/ledger.py
- [[dot-subject_not_empty()]] - code - gateway/ingest_api/models.py
- [[dot-validate_base64()]] - code - gateway/ingest_api/models.py
- [[Any_23]] - code - gateway/ingest_api/ledger.py
- [[Dependency Graph_1]] - document - docs/vault/09 - Diagrams/Dependency Graph.md
- [[Dependency Graph]] - document - docs/vault/09 - Diagrams/Dependency Graph.md
- [[EmailSendRequest]] - code - gateway/ingest_api/models.py
- [[Fetch a single ledger entry by ID          Args             entry_id Entry UUI]] - rationale - gateway/ingest_api/ledger.py
- [[ForwardResponse]] - code - gateway/ingest_api/models.py
- [[Gateway Module Dependencies]] - document - docs/vault/09 - Diagrams/Dependency Graph.md
- [[Gateway Startup Initialization Order]] - concept - docs/vault/09 - Diagrams/Dependency Graph.md
- [[Get aggregate statistics          Returns             Dictionary with total ent]] - rationale - gateway/ingest_api/ledger.py
- [[Key Initialization Order (main.py lifespan)]] - document - docs/vault/09 - Diagrams/Dependency Graph.md
- [[LedgerConfig]] - code - gateway/ingest_api/ledger.py
- [[LedgerEntry]] - code - gateway/ingest_api/models.py
- [[LedgerEntry_1]] - code - gateway/ingest_api/ledger.py
- [[LedgerQueryResponse]] - code - gateway/ingest_api/models.py
- [[LedgerQueryResponse_1]] - code - gateway/ingest_api/ledger.py
- [[Paginated ledger query results]] - rationale - gateway/ingest_api/models.py
- [[Python Package Dependencies]] - document - docs/vault/09 - Diagrams/Dependency Graph.md
- [[Query ledger entries with pagination and filters          Args             page]] - rationale - gateway/ingest_api/ledger.py
- [[Related Notes_18]] - document - docs/vault/09 - Diagrams/Dependency Graph.md
- [[Request to execute an SSH command]] - rationale - gateway/ingest_api/models.py
- [[Request to send an email through the gateway (P3 channel ownership).      The b]] - rationale - gateway/ingest_api/models.py
- [[Request to write file content to an allowlisted SSH host.      Unlike SSHExecReq]] - rationale - gateway/ingest_api/models.py
- [[Response after content is ingested, sanitized, and logged]] - rationale - gateway/ingest_api/models.py
- [[Response from POST sshwrite_file.      success reflects whether the remote wri]] - rationale - gateway/ingest_api/models.py
- [[Response from SSH command execution]] - rationale - gateway/ingest_api/models.py
- [[SSHExecRequest]] - code - gateway/ingest_api/models.py
- [[SSHExecResponse]] - code - gateway/ingest_api/models.py
- [[SSHWriteFileRequest]] - code - gateway/ingest_api/models.py
- [[SSHWriteFileResponse]] - code - gateway/ingest_api/models.py
- [[Single entry from the data ledger]] - rationale - gateway/ingest_api/models.py
- [[Store configuration          Actual database connection created in initialize().]] - rationale - gateway/ingest_api/ledger.py
- [[gatewayREADME]] - document - gateway/README.md
- [[ingest_apimodels.py]] - code - gateway/ingest_api/models.py
- [[ledger.py_1]] - code - gateway/ingest_api/ledger.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/ingest_api/modelspy
SORT file.name ASC
```

## Connections to other communities
- 17 edges to [[_COMMUNITY_DataLedger]]
- 8 edges to [[_COMMUNITY_socrouter.py]]
- 4 edges to [[_COMMUNITY_ToolResultSanitizer]]
- 4 edges to [[_COMMUNITY_create_auth_dependency]]
- 4 edges to [[_COMMUNITY_forward.py]]
- 2 edges to [[_COMMUNITY_ApprovalQueueItem]]
- 2 edges to [[_COMMUNITY_load_config]]
- 2 edges to [[_COMMUNITY_test_mfa_guard.py]]
- 1 edge to [[_COMMUNITY_gatewayingest_apimain.py (hermes-dashboard HTTP + WebSocket reverse proxy)]]
- 1 edge to [[_COMMUNITY_AgentTarget]]
- 1 edge to [[_COMMUNITY_Request]]
- 1 edge to [[_COMMUNITY_lifespan.py]]
- 1 edge to [[_COMMUNITY_All Dependencies]]
- 1 edge to [[_COMMUNITY_ForwardRequest]]
- 1 edge to [[_COMMUNITY_ApprovalRequest]]
- 1 edge to [[_COMMUNITY_Features]]
- 1 edge to [[_COMMUNITY_Network Topology]]

## Top bridge nodes
- [[ingest_apimodels.py]] - degree 27, connects to 10 communities
- [[gatewayREADME]] - degree 11, connects to 8 communities
- [[ledger.py_1]] - degree 10, connects to 4 communities
- [[LedgerEntry]] - degree 9, connects to 2 communities
- [[LedgerQueryResponse]] - degree 9, connects to 2 communities
