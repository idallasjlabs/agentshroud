---
type: community
cohesion: 0.02
members: 150
---

# Gateway Config & PII Sanitizer

**Cohesion:** 0.02 - loosely connected
**Members:** 150 nodes

## Members
- [[dot-__init__()_69]] - code - gateway/ingest_api/ledger.py
- [[dot-_hash_content()]] - code - gateway/ingest_api/ledger.py
- [[dot-close()_10]] - code - gateway/ingest_api/ledger.py
- [[dot-delete_entry()]] - code - gateway/ingest_api/ledger.py
- [[dot-enforce_retention()]] - code - gateway/ingest_api/ledger.py
- [[dot-get_entry()]] - code - gateway/ingest_api/ledger.py
- [[dot-get_stats()_11]] - code - gateway/ingest_api/ledger.py
- [[dot-initialize()_1]] - code - gateway/ingest_api/ledger.py
- [[dot-ledger()]] - code - gateway/tests/test_performance.py
- [[dot-ledger()_1]] - code - gateway/tests/test_performance.py
- [[dot-query()]] - code - gateway/ingest_api/ledger.py
- [[dot-record()_2]] - code - gateway/ingest_api/ledger.py
- [[dot-test_10000_lookups_under_1s()]] - code - gateway/tests/test_performance.py
- [[dot-test_1000_entries_all_recorded()]] - code - gateway/tests/test_audit_chain.py
- [[dot-test_1000_entries_under_5s()]] - code - gateway/tests/test_performance.py
- [[dot-test_1000_messages_under_10s()]] - code - gateway/tests/test_performance.py
- [[dot-test_1000_messages_under_5s()]] - code - gateway/tests/test_performance.py
- [[dot-test_100_inbound_messages_under_5s()]] - code - gateway/tests/test_performance.py
- [[dot-test_100_outbound_messages_under_5s()]] - code - gateway/tests/test_performance.py
- [[dot-test_50_concurrent_writes()]] - code - gateway/tests/test_audit_chain.py
- [[dot-test_concurrent_write_and_read()]] - code - gateway/tests/test_audit_chain.py
- [[dot-test_content_hashes_are_unique()]] - code - gateway/tests/test_audit_chain.py
- [[dot-test_delete_entry_removes_it()]] - code - gateway/tests/test_audit_chain.py
- [[dot-test_delete_nonexistent_returns_false()]] - code - gateway/tests/test_audit_chain.py
- [[dot-test_detection_accuracy_at_scale()]] - code - gateway/tests/test_performance.py
- [[dot-test_enforce_retention_deletes_expired()]] - code - gateway/tests/test_audit_chain.py
- [[dot-test_entry_retrieval_by_id()]] - code - gateway/tests/test_audit_chain.py
- [[dot-test_hash_is_sha256()]] - code - gateway/tests/test_audit_chain.py
- [[dot-test_hash_matches_content()]] - code - gateway/tests/test_audit_chain.py
- [[dot-test_nonexistent_entry_returns_none()]] - code - gateway/tests/test_audit_chain.py
- [[dot-test_pii_detection_accuracy_at_scale()]] - code - gateway/tests/test_performance.py
- [[dot-test_pii_inbound_latency()]] - code - gateway/tests/test_performance.py
- [[dot-test_query_after_1000_entries()]] - code - gateway/tests/test_performance.py
- [[dot-test_query_filter_by_source()]] - code - gateway/tests/test_audit_chain.py
- [[dot-test_query_pagination()]] - code - gateway/tests/test_audit_chain.py
- [[dot-test_single_inbound_under_200ms()]] - code - gateway/tests/test_performance.py
- [[dot-test_single_outbound_under_200ms()]] - code - gateway/tests/test_performance.py
- [[dot-test_ssh_hosts_list()]] - code - gateway/tests/test_ssh_endpoints.py
- [[dot-test_stats_correct()]] - code - gateway/tests/test_audit_chain.py
- [[dot-test_trust_update_performance()]] - code - gateway/tests/test_performance.py
- [[100 messages through process_inbound in under 5 seconds.]] - rationale - gateway/tests/test_performance.py
- [[1000 trust updates (mix of successfailure).]] - rationale - gateway/tests/test_performance.py
- [[10000 trust lookups in under 1 second.]] - rationale - gateway/tests/test_performance.py
- [[50 concurrent write operations should all succeed.]] - rationale - gateway/tests/test_audit_chain.py
- [[Any_26]] - code - gateway/ingest_api/ledger.py
- [[Async SQLite-backed data ledger      Records all content forwarded through the g]] - rationale - gateway/ingest_api/ledger.py
- [[Audit chain 1000 entries in  5s.]] - rationale - gateway/tests/test_performance.py
- [[CI has no real agentshroud.yaml (gitignored, per-deployment secret     config) —]] - rationale - gateway/tests/conftest.py
- [[Can retrieve specific entry by ID for verification.]] - rationale - gateway/tests/test_audit_chain.py
- [[Chain with many entries — verify integrity.]] - rationale - gateway/tests/test_audit_chain.py
- [[Close database connection]] - rationale - gateway/ingest_api/ledger.py
- [[Collect and write benchmark baselines to .benchmarksbaseline-v1.0.0.json.]] - rationale - gateway/tests/test_performance.py
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
- [[End-to-end pipeline latency for a single message.]] - rationale - gateway/tests/test_performance.py
- [[Export chain and re-verify.]] - rationale - gateway/tests/test_audit_chain.py
- [[Fetch a single ledger entry by ID          Args             entry_id Entry UUI]] - rationale - gateway/ingest_api/ledger.py
- [[Filter entries by source.]] - rationale - gateway/tests/test_audit_chain.py
- [[Forget this' - permanently delete a ledger entry          Implements right to er]] - rationale - gateway/ingest_api/ledger.py
- [[GatewayConfig_1]] - code - gateway/tests/conftest.py
- [[GatewayConfig_2]] - code - gateway/tests/test_mcp_result_endpoint.py
- [[Get aggregate statistics          Returns             Dictionary with total ent]] - rationale - gateway/ingest_api/ledger.py
- [[Injection attempts should be detected even under load.]] - rationale - gateway/tests/test_performance.py
- [[LedgerConfig]] - code - gateway/ingest_api/config.py
- [[LedgerConfig_1]] - code - gateway/ingest_api/ledger.py
- [[LedgerEntry_1]] - code - gateway/ingest_api/ledger.py
- [[LedgerQueryResponse_1]] - code - gateway/ingest_api/ledger.py
- [[Looking up nonexistent entry returns None.]] - rationale - gateway/tests/test_audit_chain.py
- [[PII sanitizer 1000 messages in  10s.]] - rationale - gateway/tests/test_performance.py
- [[PII-laden messages through inbound pipeline — verify redaction + timing.]] - rationale - gateway/tests/test_performance.py
- [[PIISanitizer_1]] - code - gateway/tests/conftest.py
- [[Paginated queries return correct subsets.]] - rationale - gateway/tests/test_audit_chain.py
- [[Process 1000 mixed messages in under 10 seconds.]] - rationale - gateway/tests/test_performance.py
- [[Prompt guard 1000 messages in  5s.]] - rationale - gateway/tests/test_performance.py
- [[Query ledger entries with pagination and filters          Args             page]] - rationale - gateway/ingest_api/ledger.py
- [[Query performance after 1000 entries.]] - rationale - gateway/tests/test_performance.py
- [[Re-initializing must not orphan the first aiosqlite connection.      aiosqlite c]] - rationale - gateway/tests/test_ledger.py
- [[Retention enforcement removes expired entries.]] - rationale - gateway/tests/test_audit_chain.py
- [[Retention enforcement.]] - rationale - gateway/tests/test_audit_chain.py
- [[Return Authorization headers with test token]] - rationale - gateway/tests/conftest.py
- [[SHA-256 hash of content string          Args             content Text to hash]] - rationale - gateway/ingest_api/ledger.py
- [[Scan 1000 messages in under 5 seconds.]] - rationale - gateway/tests/test_performance.py
- [[SecurityPipeline.process_inboundoutbound latency via the real pipeline class.]] - rationale - gateway/tests/test_performance.py
- [[Single message through SecurityPipeline.process_inbound  200ms.]] - rationale - gateway/tests/test_performance.py
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
- [[TestAuditChainPerformance]] - code - gateway/tests/test_performance.py
- [[TestBenchmarkBaseline]] - code - gateway/tests/test_performance.py
- [[TestChainExportAndVerification]] - code - gateway/tests/test_audit_chain.py
- [[TestConcurrentWrites]] - code - gateway/tests/test_audit_chain.py
- [[TestFullPipelineLatency]] - code - gateway/tests/test_performance.py
- [[TestPIISanitizerPerformance]] - code - gateway/tests/test_performance.py
- [[TestPromptGuardPerformance]] - code - gateway/tests/test_performance.py
- [[TestRetention]] - code - gateway/tests/test_audit_chain.py
- [[TestSSHHosts]] - code - gateway/tests/test_ssh_endpoints.py
- [[TestSecurityPipelineChainLatency]] - code - gateway/tests/test_performance.py
- [[TestTamperDetection]] - code - gateway/tests/test_audit_chain.py
- [[TestTrustManagerPerformance]] - code - gateway/tests/test_performance.py
- [[Trust check 10000 lookups in  1s.]] - rationale - gateway/tests/test_performance.py
- [[Verify detection accuracy doesn't degrade at scale.]] - rationale - gateway/tests/test_performance.py
- [[Verify hash matches SHA-256 of the content.]] - rationale - gateway/tests/test_audit_chain.py
- [[Write 1000 audit entries in under 5 seconds.]] - rationale - gateway/tests/test_performance.py
- [[Write 1000 entries and verify they're all there.]] - rationale - gateway/tests/test_audit_chain.py
- [[_ensure_agentshroud_config_resolvable()]] - code - gateway/tests/conftest.py
- [[auth_headers()_2]] - code - gateway/tests/conftest.py
- [[conftest.py]] - code - gateway/tests/conftest.py
- [[ledger()]] - code - gateway/tests/test_audit_chain.py
- [[ledger()_1]] - code - gateway/tests/test_security_integration.py
- [[sanitizer()_3]] - code - gateway/tests/conftest.py
- [[test_audit_chain.py]] - code - gateway/tests/test_audit_chain.py
- [[test_client()]] - code - gateway/tests/conftest.py
- [[test_config()]] - code - gateway/tests/conftest.py
- [[test_config()_1]] - code - gateway/tests/test_mcp_result_endpoint.py
- [[test_delete_entry()]] - code - gateway/tests/test_ledger.py
- [[test_delete_nonexistent()]] - code - gateway/tests/test_ledger.py
- [[test_get_entry()]] - code - gateway/tests/test_ledger.py
- [[test_get_stats()_1]] - code - gateway/tests/test_ledger.py
- [[test_initialize_is_idempotent()]] - code - gateway/tests/test_ledger.py
- [[test_ledger()]] - code - gateway/tests/conftest.py
- [[test_ledger.py]] - code - gateway/tests/test_ledger.py
- [[test_performance.py]] - code - gateway/tests/test_performance.py
- [[test_query_ledger()]] - code - gateway/tests/test_ledger.py
- [[test_query_with_filter()]] - code - gateway/tests/test_ledger.py
- [[test_query_with_forwarded_to_filter()]] - code - gateway/tests/test_ledger.py
- [[test_query_with_time_filters()]] - code - gateway/tests/test_ledger.py
- [[test_record_entry()]] - code - gateway/tests/test_ledger.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Gateway_Config__PII_Sanitizer
SORT file.name ASC
```

## Connections to other communities
- 44 edges to [[_COMMUNITY_Approval Queue (WebSocket)]]
- 16 edges to [[_COMMUNITY_Approval Routing & Event Bus]]
- 15 edges to [[_COMMUNITY_PII Sanitizer & Redaction]]
- 14 edges to [[_COMMUNITY_Tool Result Sanitizer & XML Injection Filtering]]
- 13 edges to [[_COMMUNITY_Prompt Guard & Context Integrity]]
- 10 edges to [[_COMMUNITY_Cross-Bot Trust & A2A Governance]]
- 10 edges to [[_COMMUNITY_Ingest API & RBAC Core]]
- 8 edges to [[_COMMUNITY_Multi-Agent Router & Chat UI]]
- 8 edges to [[_COMMUNITY_Signed Instruction Envelopes & Security Pipeline]]
- 7 edges to [[_COMMUNITY_Enhanced Approval Queue]]
- 4 edges to [[_COMMUNITY_Community 322]]
- 4 edges to [[_COMMUNITY_Community 253]]
- 1 edge to [[_COMMUNITY_Community 153]]
- 1 edge to [[_COMMUNITY_Community 386]]
- 1 edge to [[_COMMUNITY_Community 180]]
- 1 edge to [[_COMMUNITY_Community 519]]
- 1 edge to [[_COMMUNITY_Community 418]]

## Top bridge nodes
- [[LedgerConfig]] - degree 62, connects to 7 communities
- [[test_performance.py]] - degree 16, connects to 6 communities
- [[conftest.py]] - degree 14, connects to 6 communities
- [[DataLedger]] - degree 67, connects to 5 communities
- [[TestSecurityPipelineChainLatency]] - degree 15, connects to 5 communities