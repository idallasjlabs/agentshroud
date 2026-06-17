---
type: community
cohesion: 0.03
members: 105
---

# Ledger Config & Test Infra

**Cohesion:** 0.03 - loosely connected
**Members:** 105 nodes

## Members
- [[.__init__()_7]] - code - gateway/ingest_api/ledger.py
- [[._hash_content()]] - code - gateway/ingest_api/ledger.py
- [[.close()_2]] - code - gateway/ingest_api/ledger.py
- [[.delete_entry()]] - code - gateway/ingest_api/ledger.py
- [[.enforce_retention()]] - code - gateway/ingest_api/ledger.py
- [[.get_entry()]] - code - gateway/ingest_api/ledger.py
- [[.get_stats()_1]] - code - gateway/ingest_api/ledger.py
- [[.initialize()_2]] - code - gateway/ingest_api/ledger.py
- [[.ledger()]] - code - gateway/tests/test_performance.py
- [[.ledger()_1]] - code - gateway/tests/test_performance.py
- [[.query()]] - code - gateway/ingest_api/ledger.py
- [[.record()]] - code - gateway/ingest_api/ledger.py
- [[.test_1000_entries_all_recorded()]] - code - gateway/tests/test_audit_chain.py
- [[.test_50_concurrent_writes()]] - code - gateway/tests/test_audit_chain.py
- [[.test_concurrent_write_and_read()]] - code - gateway/tests/test_audit_chain.py
- [[.test_content_hashes_are_unique()]] - code - gateway/tests/test_audit_chain.py
- [[.test_delete_entry_removes_it()]] - code - gateway/tests/test_audit_chain.py
- [[.test_delete_nonexistent_returns_false()]] - code - gateway/tests/test_audit_chain.py
- [[.test_enforce_retention_deletes_expired()]] - code - gateway/tests/test_audit_chain.py
- [[.test_entry_retrieval_by_id()]] - code - gateway/tests/test_audit_chain.py
- [[.test_hash_is_sha256()]] - code - gateway/tests/test_audit_chain.py
- [[.test_hash_matches_content()]] - code - gateway/tests/test_audit_chain.py
- [[.test_nonexistent_entry_returns_none()]] - code - gateway/tests/test_audit_chain.py
- [[.test_query_filter_by_source()]] - code - gateway/tests/test_audit_chain.py
- [[.test_query_pagination()]] - code - gateway/tests/test_audit_chain.py
- [[.test_stats_correct()]] - code - gateway/tests/test_audit_chain.py
- [[50 concurrent write operations should all succeed.]] - rationale - gateway/tests/test_audit_chain.py
- [[Any_5]] - code - gateway/ingest_api/ledger.py
- [[Async SQLite-backed data ledger      Records all content forwarded through the g]] - rationale - gateway/ingest_api/ledger.py
- [[Can retrieve specific entry by ID for verification.]] - rationale - gateway/tests/test_audit_chain.py
- [[Chain with many entries — verify integrity.]] - rationale - gateway/tests/test_audit_chain.py
- [[Close database connection]] - rationale - gateway/ingest_api/ledger.py
- [[Concurrent writes and reads don't conflict.]] - rationale - gateway/tests/test_audit_chain.py
- [[Concurrent writes to chain.]] - rationale - gateway/tests/test_audit_chain.py
- [[Content hash should be a valid SHA-256 hex digest.]] - rationale - gateway/tests/test_audit_chain.py
- [[Create a FastAPI TestClient with test configuration      Note This doesn't init]] - rationale - gateway/tests/conftest.py
- [[Create a PIISanitizer instance for testing]] - rationale - gateway/tests/conftest.py
- [[Create a new ledger entry          Args             source Source identifier (]] - rationale - gateway/ingest_api/ledger.py
- [[Create a test configuration      Uses regex fallback for PII (no spaCy model req]] - rationale - gateway/tests/conftest.py
- [[Create an initialized in-memory ledger for testing      Yields the ledger, then]] - rationale - gateway/tests/conftest.py
- [[Create database, tables, and run initial cleanup          Must be called before]] - rationale - gateway/ingest_api/ledger.py
- [[Data ledger configuration]] - rationale - gateway/ingest_api/config.py
- [[DataLedger]] - code - gateway/ingest_api/ledger.py
- [[Delete entries older than retention_days          Returns             Number of]] - rationale - gateway/ingest_api/ledger.py
- [[Deleted entry is gone (right to erasure).]] - rationale - gateway/tests/test_audit_chain.py
- [[Deleting nonexistent entry returns False.]] - rationale - gateway/tests/test_audit_chain.py
- [[Different content should produce different hashes.]] - rationale - gateway/tests/test_audit_chain.py
- [[Export chain and re-verify.]] - rationale - gateway/tests/test_audit_chain.py
- [[Fetch a single ledger entry by ID          Args             entry_id Entry UUI]] - rationale - gateway/ingest_api/ledger.py
- [[Filter entries by source.]] - rationale - gateway/tests/test_audit_chain.py
- [[Forget this' - permanently delete a ledger entry          Implements right to er]] - rationale - gateway/ingest_api/ledger.py
- [[GatewayConfig_2]] - code - gateway/tests/conftest.py
- [[Get aggregate statistics          Returns             Dictionary with total ent]] - rationale - gateway/ingest_api/ledger.py
- [[LedgerConfig]] - code - gateway/ingest_api/config.py
- [[LedgerConfig_1]] - code - gateway/ingest_api/ledger.py
- [[LedgerEntry]] - code - gateway/ingest_api/ledger.py
- [[LedgerQueryResponse]] - code - gateway/ingest_api/ledger.py
- [[Looking up nonexistent entry returns None.]] - rationale - gateway/tests/test_audit_chain.py
- [[PIISanitizer_2]] - code - gateway/tests/conftest.py
- [[Paginated queries return correct subsets.]] - rationale - gateway/tests/test_audit_chain.py
- [[Query ledger entries with pagination and filters          Args             page]] - rationale - gateway/ingest_api/ledger.py
- [[Re-initializing must not orphan the first aiosqlite connection.      aiosqlite c_1]] - rationale - gateway/tests/test_ledger.py
- [[Retention enforcement removes expired entries.]] - rationale - gateway/tests/test_audit_chain.py
- [[Retention enforcement.]] - rationale - gateway/tests/test_audit_chain.py
- [[Return Authorization headers with test token]] - rationale - gateway/tests/conftest.py
- [[SHA-256 hash of content string          Args             content Text to hash]] - rationale - gateway/ingest_api/ledger.py
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
- [[auth_headers()]] - code - gateway/tests/conftest.py
- [[conftest.py]] - code - gateway/tests/conftest.py
- [[ledger()]] - code - gateway/tests/test_audit_chain.py
- [[ledger()_1]] - code - gateway/tests/test_security_integration.py
- [[sanitizer()]] - code - gateway/tests/conftest.py
- [[test_audit_chain.py]] - code - gateway/tests/test_audit_chain.py
- [[test_client()]] - code - gateway/tests/conftest.py
- [[test_config()]] - code - gateway/tests/conftest.py
- [[test_delete_entry()]] - code - gateway/tests/test_ledger.py
- [[test_delete_nonexistent()]] - code - gateway/tests/test_ledger.py
- [[test_get_entry()]] - code - gateway/tests/test_ledger.py
- [[test_get_stats()_1]] - code - gateway/tests/test_ledger.py
- [[test_initialize_is_idempotent()_1]] - code - gateway/tests/test_ledger.py
- [[test_ledger()]] - code - gateway/tests/conftest.py
- [[test_ledger.py]] - code - gateway/tests/test_ledger.py
- [[test_query_ledger()]] - code - gateway/tests/test_ledger.py
- [[test_query_with_filter()]] - code - gateway/tests/test_ledger.py
- [[test_query_with_forwarded_to_filter()]] - code - gateway/tests/test_ledger.py
- [[test_query_with_time_filters()]] - code - gateway/tests/test_ledger.py
- [[test_record_entry()]] - code - gateway/tests/test_ledger.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Ledger_Config__Test_Infra
SORT file.name ASC
```

## Connections to other communities
- 31 edges to [[_COMMUNITY_SSH Proxy & Gateway Config]]
- 19 edges to [[_COMMUNITY_Tool Result Sanitizer]]
- 11 edges to [[_COMMUNITY_Gateway Config & Lifespan]]
- 10 edges to [[_COMMUNITY_CLI & Core Gateway Routes]]
- 4 edges to [[_COMMUNITY_Enhanced Approval Queue]]
- 3 edges to [[_COMMUNITY_Module Group 216]]
- 2 edges to [[_COMMUNITY_Context Guard & Integrity]]
- 2 edges to [[_COMMUNITY_Module Group 322]]
- 2 edges to [[_COMMUNITY_Module Group 489]]
- 1 edge to [[_COMMUNITY_Module Group 83]]
- 1 edge to [[_COMMUNITY_Module Group 127]]
- 1 edge to [[_COMMUNITY_Module Group 255]]

## Top bridge nodes
- [[LedgerConfig]] - degree 53, connects to 10 communities
- [[DataLedger]] - degree 56, connects to 8 communities
- [[conftest.py]] - degree 12, connects to 3 communities
- [[GatewayConfig_2]] - degree 11, connects to 3 communities
- [[PIISanitizer_2]] - degree 8, connects to 3 communities