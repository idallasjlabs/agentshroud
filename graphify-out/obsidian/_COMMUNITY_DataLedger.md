---
type: community
cohesion: 0.02
members: 110
---

# DataLedger

**Cohesion:** 0.02 - loosely connected
**Members:** 110 nodes

## Members
- [[NOTE Called within _lock context]] - rationale - gateway/approval_queue/queue.py
- [[dot-__init__()_130]] - code - gateway/ingest_api/ledger.py
- [[dot-_hash_content()]] - code - gateway/ingest_api/ledger.py
- [[dot-close()_12]] - code - gateway/ingest_api/ledger.py
- [[dot-delete_entry()]] - code - gateway/ingest_api/ledger.py
- [[dot-enforce_retention()]] - code - gateway/ingest_api/ledger.py
- [[dot-get_entry()]] - code - gateway/ingest_api/ledger.py
- [[dot-get_stats()_14]] - code - gateway/ingest_api/ledger.py
- [[dot-initialize()_1]] - code - gateway/ingest_api/ledger.py
- [[dot-ledger()]] - code - gateway/tests/test_performance.py
- [[dot-ledger()_1]] - code - gateway/tests/test_performance.py
- [[dot-query()]] - code - gateway/ingest_api/ledger.py
- [[dot-record()_2]] - code - gateway/ingest_api/ledger.py
- [[dot-test_1000_entries_all_recorded()]] - code - gateway/tests/test_audit_chain.py
- [[dot-test_50_concurrent_writes()]] - code - gateway/tests/test_audit_chain.py
- [[dot-test_concurrent_write_and_read()]] - code - gateway/tests/test_audit_chain.py
- [[dot-test_content_hashes_are_unique()]] - code - gateway/tests/test_audit_chain.py
- [[dot-test_delete_entry_removes_it()]] - code - gateway/tests/test_audit_chain.py
- [[dot-test_delete_nonexistent_returns_false()]] - code - gateway/tests/test_audit_chain.py
- [[dot-test_enforce_retention_deletes_expired()]] - code - gateway/tests/test_audit_chain.py
- [[dot-test_entry_retrieval_by_id()]] - code - gateway/tests/test_audit_chain.py
- [[dot-test_hash_is_sha256()]] - code - gateway/tests/test_audit_chain.py
- [[dot-test_hash_matches_content()]] - code - gateway/tests/test_audit_chain.py
- [[dot-test_nonexistent_entry_returns_none()]] - code - gateway/tests/test_audit_chain.py
- [[dot-test_query_filter_by_source()]] - code - gateway/tests/test_audit_chain.py
- [[dot-test_query_pagination()]] - code - gateway/tests/test_audit_chain.py
- [[dot-test_stats_correct()]] - code - gateway/tests/test_audit_chain.py
- [[50 concurrent write operations should all succeed.]] - rationale - gateway/tests/test_audit_chain.py
- [[AgentShroud Security Dashboard (index.html)]] - code - gateway/dashboard/index.html
- [[Any_47]] - code - gateway/ingest_api/ledger.py
- [[Async SQLite-backed data ledger      Records all content forwarded through the g]] - rationale - gateway/ingest_api/ledger.py
- [[Can retrieve specific entry by ID for verification.]] - rationale - gateway/tests/test_audit_chain.py
- [[Chain with many entries — verify integrity.]] - rationale - gateway/tests/test_audit_chain.py
- [[Close database connection]] - rationale - gateway/ingest_api/ledger.py
- [[Concurrent writes and reads don't conflict.]] - rationale - gateway/tests/test_audit_chain.py
- [[Concurrent writes to chain.]] - rationale - gateway/tests/test_audit_chain.py
- [[Content hash should be a valid SHA-256 hex digest.]] - rationale - gateway/tests/test_audit_chain.py
- [[Create a new ledger entry          Args             source Source identifier (]] - rationale - gateway/ingest_api/ledger.py
- [[Create database, tables, and run initial cleanup          Must be called before]] - rationale - gateway/ingest_api/ledger.py
- [[DataLedger]] - code - gateway/ingest_api/ledger.py
- [[Delete entries older than retention_days          Returns             Number of]] - rationale - gateway/ingest_api/ledger.py
- [[Deleted entry is gone (right to erasure).]] - rationale - gateway/tests/test_audit_chain.py
- [[Deleting nonexistent entry returns False.]] - rationale - gateway/tests/test_audit_chain.py
- [[Dependency Graph_1]] - document - docs/vault/09 - Diagrams/Dependency Graph.md
- [[Dependency Graph]] - document - docs/vault/09 - Diagrams/Dependency Graph.md
- [[Different content should produce different hashes.]] - rationale - gateway/tests/test_audit_chain.py
- [[Export chain and re-verify.]] - rationale - gateway/tests/test_audit_chain.py
- [[Fetch a single ledger entry by ID          Args             entry_id Entry UUI]] - rationale - gateway/ingest_api/ledger.py
- [[Filter entries by source.]] - rationale - gateway/tests/test_audit_chain.py
- [[Forget this' - permanently delete a ledger entry          Implements right to er]] - rationale - gateway/ingest_api/ledger.py
- [[Gateway Module Dependencies]] - document - docs/vault/09 - Diagrams/Dependency Graph.md
- [[Gateway Startup Initialization Order]] - concept - docs/vault/09 - Diagrams/Dependency Graph.md
- [[Get aggregate statistics          Returns             Dictionary with total ent]] - rationale - gateway/ingest_api/ledger.py
- [[Key Initialization Order (main.py lifespan)]] - document - docs/vault/09 - Diagrams/Dependency Graph.md
- [[LedgerConfig]] - code - gateway/ingest_api/ledger.py
- [[LedgerEntry]] - code - gateway/ingest_api/models.py
- [[LedgerEntry_1]] - code - gateway/ingest_api/ledger.py
- [[LedgerQueryResponse]] - code - gateway/ingest_api/models.py
- [[LedgerQueryResponse_1]] - code - gateway/ingest_api/ledger.py
- [[Looking up nonexistent entry returns None.]] - rationale - gateway/tests/test_audit_chain.py
- [[MFAGuard.verify()]] - code - gateway/security/mfa_guard.py
- [[Minimal health check endpoint — no authentication required.      Returns only ba]] - rationale - gateway/ingest_api/routes/health.py
- [[Paginated ledger query results]] - rationale - gateway/ingest_api/models.py
- [[Paginated queries return correct subsets.]] - rationale - gateway/tests/test_audit_chain.py
- [[Python Package Dependencies]] - document - docs/vault/09 - Diagrams/Dependency Graph.md
- [[Query ledger entries with pagination and filters          Args             page]] - rationale - gateway/ingest_api/ledger.py
- [[Re-initializing must not orphan the first aiosqlite connection.      aiosqlite c]] - rationale - gateway/tests/test_ledger.py
- [[Related Notes_33]] - document - docs/vault/09 - Diagrams/Dependency Graph.md
- [[Retention enforcement removes expired entries.]] - rationale - gateway/tests/test_audit_chain.py
- [[Retention enforcement.]] - rationale - gateway/tests/test_audit_chain.py
- [[SHA-256 hash of content string          Args             content Text to hash]] - rationale - gateway/ingest_api/ledger.py
- [[Single entry from the data ledger]] - rationale - gateway/ingest_api/models.py
- [[Stats reflect actual data.]] - rationale - gateway/tests/test_audit_chain.py
- [[Store configuration          Actual database connection created in initialize().]] - rationale - gateway/ingest_api/ledger.py
- [[Tamper detection at various chain positions.]] - rationale - gateway/tests/test_audit_chain.py
- [[Test creating a ledger entry]] - rationale - gateway/tests/test_ledger.py
- [[Test deleting a ledger entry]] - rationale - gateway/tests/test_ledger.py
- [[Test deleting a non-existent entry]] - rationale - gateway/tests/test_ledger.py
- [[Test ledger query with source filter]] - rationale - gateway/tests/test_ledger.py
- [[Test paginated ledger query]] - rationale - gateway/tests/test_ledger.py
- [[Test querying ledger with forwarded_to filter]] - rationale - gateway/tests/test_ledger.py
- [[Test querying ledger with time range filters]] - rationale - gateway/tests/test_ledger.py
- [[Test retrieving a ledger entry by ID]] - rationale - gateway/tests/test_ledger.py
- [[Test stats calculation]] - rationale - gateway/tests/test_ledger.py
- [[TestAuditChainIntegrity]] - code - gateway/tests/test_audit_chain.py
- [[TestChainExportAndVerification]] - code - gateway/tests/test_audit_chain.py
- [[TestConcurrentWrites]] - code - gateway/tests/test_audit_chain.py
- [[TestRetention]] - code - gateway/tests/test_audit_chain.py
- [[TestTamperDetection]] - code - gateway/tests/test_audit_chain.py
- [[Verify hash matches SHA-256 of the content.]] - rationale - gateway/tests/test_audit_chain.py
- [[Write 1000 entries and verify they're all there.]] - rationale - gateway/tests/test_audit_chain.py
- [[gatewayREADME]] - document - gateway/README.md
- [[health.py]] - code - gateway/ingest_api/routes/health.py
- [[health_check()]] - code - gateway/ingest_api/routes/health.py
- [[ingest_apimodels.py]] - code - gateway/ingest_api/models.py
- [[ledger()]] - code - gateway/tests/test_audit_chain.py
- [[ledger.py_1]] - code - gateway/ingest_api/ledger.py
- [[queue.py]] - code - gateway/approval_queue/queue.py
- [[test_audit_chain.py]] - code - gateway/tests/test_audit_chain.py
- [[test_delete_entry()]] - code - gateway/tests/test_ledger.py
- [[test_delete_nonexistent()]] - code - gateway/tests/test_ledger.py
- [[test_get_entry()]] - code - gateway/tests/test_ledger.py
- [[test_get_stats()_2]] - code - gateway/tests/test_ledger.py
- [[test_initialize_is_idempotent()]] - code - gateway/tests/test_ledger.py
- [[test_ledger.py]] - code - gateway/tests/test_ledger.py
- [[test_query_ledger()]] - code - gateway/tests/test_ledger.py
- [[test_query_with_filter()]] - code - gateway/tests/test_ledger.py
- [[test_query_with_forwarded_to_filter()]] - code - gateway/tests/test_ledger.py
- [[test_query_with_time_filters()]] - code - gateway/tests/test_ledger.py
- [[test_record_entry()]] - code - gateway/tests/test_ledger.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/DataLedger
SORT file.name ASC
```

## Connections to other communities
- 45 edges to [[_COMMUNITY_ApprovalQueueConfig]]
- 11 edges to [[_COMMUNITY_AgentTarget]]
- 10 edges to [[_COMMUNITY_PIIConfig]]
- 5 edges to [[_COMMUNITY_socrouter.py]]
- 5 edges to [[_COMMUNITY_ApprovalQueueConfig_1]]
- 4 edges to [[_COMMUNITY_MiddlewareManager]]
- 4 edges to [[_COMMUNITY_forward.py]]
- 4 edges to [[_COMMUNITY_ToolResultSanitizer]]
- 3 edges to [[_COMMUNITY_main.py]]
- 3 edges to [[_COMMUNITY_test_mfa_guard.py]]
- 3 edges to [[_COMMUNITY_create_auth_dependency_1]]
- 2 edges to [[_COMMUNITY_create_auth_dependency]]
- 2 edges to [[_COMMUNITY_PIIConfig_1]]
- 2 edges to [[_COMMUNITY_ForwardRequest]]
- 1 edge to [[_COMMUNITY_All Dependencies_1]]
- 1 edge to [[_COMMUNITY_ingest_apimodels.py]]
- 1 edge to [[_COMMUNITY_gatewayingest_apimain.py (hermes-dashboard HTTP + WebSocket reverse proxy)]]
- 1 edge to [[_COMMUNITY_`SecurityPipeline`]]
- 1 edge to [[_COMMUNITY_AgentShroud macOS App Icon (1024x1024, Rounded Squircle)]]
- 1 edge to [[_COMMUNITY_get_engine]]
- 1 edge to [[_COMMUNITY_Features]]

## Top bridge nodes
- [[DataLedger]] - degree 67, connects to 7 communities
- [[ingest_apimodels.py]] - degree 27, connects to 7 communities
- [[gatewayREADME]] - degree 11, connects to 6 communities
- [[health.py]] - degree 9, connects to 5 communities
- [[queue.py]] - degree 14, connects to 4 communities
