---
type: community
cohesion: 0.02
members: 123
---

# EgressPolicy

**Cohesion:** 0.02 - loosely connected
**Members:** 123 nodes

## Members
- [[._hash_content()]] - code - gateway/ingest_api/ledger.py
- [[.close()_5]] - code - gateway/ingest_api/ledger.py
- [[.delete_entry()]] - code - gateway/ingest_api/ledger.py
- [[.disabled_client()]] - code - gateway/tests/test_ssh_endpoints.py
- [[.enforce_retention()]] - code - gateway/ingest_api/ledger.py
- [[.initialize()_2]] - code - gateway/ingest_api/ledger.py
- [[.ledger()]] - code - gateway/tests/test_performance.py
- [[.ledger()_1]] - code - gateway/tests/test_performance.py
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
- [[Agent with low trust cannot perform elevated actions.]] - rationale - gateway/tests/test_security_integration.py
- [[AppState]] - code - gateway/ingest_api/state.py
- [[Async SQLite-backed data ledger      Records all content forwarded through the g]] - rationale - gateway/ingest_api/ledger.py
- [[CI has no real agentshroud.yaml (gitignored, per-deployment secret     config) —]] - rationale - gateway/tests/conftest.py
- [[Can retrieve specific entry by ID for verification.]] - rationale - gateway/tests/test_audit_chain.py
- [[Chain with many entries — verify integrity.]] - rationale - gateway/tests/test_audit_chain.py
- [[Clean message flows through entire pipeline without issues.]] - rationale - gateway/tests/test_security_integration.py
- [[Close database connection]] - rationale - gateway/ingest_api/ledger.py
- [[Concurrent writes and reads don't conflict.]] - rationale - gateway/tests/test_audit_chain.py
- [[Concurrent writes to chain.]] - rationale - gateway/tests/test_audit_chain.py
- [[Config with all security modules enabled.]] - rationale - gateway/tests/test_security_integration.py
- [[Container for application-wide state]] - rationale - gateway/ingest_api/state.py
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
- [[Even if trust allows an action, egress filter blocks unauthorized destinations.]] - rationale - gateway/tests/test_security_integration.py
- [[Export chain and re-verify.]] - rationale - gateway/tests/test_audit_chain.py
- [[Filter entries by source.]] - rationale - gateway/tests/test_audit_chain.py
- [[Forget this' - permanently delete a ledger entry          Implements right to er]] - rationale - gateway/ingest_api/ledger.py
- [[GatewayConfig_2]] - code - gateway/tests/conftest.py
- [[GatewayConfig_4]] - code - gateway/tests/test_mcp_result_endpoint.py
- [[LedgerConfig]] - code - gateway/ingest_api/config.py
- [[Looking up nonexistent entry returns None.]] - rationale - gateway/tests/test_audit_chain.py
- [[Message with PII gets sanitized and logged correctly.]] - rationale - gateway/tests/test_security_integration.py
- [[Multiple messages through pipeline concurrently — thread safety.]] - rationale - gateway/tests/test_security_integration.py
- [[Outbound responses have credentials blocked for untrusted sources.]] - rationale - gateway/tests/test_security_integration.py
- [[PIISanitizer_2]] - code - gateway/tests/conftest.py
- [[Paginated queries return correct subsets.]] - rationale - gateway/tests/test_audit_chain.py
- [[Re-initializing must not orphan the first aiosqlite connection.      aiosqlite c_1]] - rationale - gateway/tests/test_ledger.py
- [[Retention enforcement removes expired entries.]] - rationale - gateway/tests/test_audit_chain.py
- [[Retention enforcement.]] - rationale - gateway/tests/test_audit_chain.py
- [[Return Authorization headers with test token]] - rationale - gateway/tests/conftest.py
- [[SHA-256 hash of content string          Args             content Text to hash]] - rationale - gateway/ingest_api/ledger.py
- [[Sensitive audit data can be encrypted at rest.]] - rationale - gateway/tests/test_security_integration.py
- [[Stats reflect actual data.]] - rationale - gateway/tests/test_audit_chain.py
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
- [[When both PII sanitizer and prompt guard detect issues.]] - rationale - gateway/tests/test_security_integration.py
- [[Write 1000 entries and verify they're all there.]] - rationale - gateway/tests/test_audit_chain.py
- [[_ensure_agentshroud_config_resolvable()]] - code - gateway/tests/conftest.py
- [[auth_headers()]] - code - gateway/tests/conftest.py
- [[conftest.py]] - code - gateway/tests/conftest.py
- [[encrypted_store()]] - code - gateway/tests/test_security_integration.py
- [[full_pipeline_config()]] - code - gateway/tests/test_security_integration.py
- [[ledger()]] - code - gateway/tests/test_audit_chain.py
- [[ledger()_2]] - code - gateway/tests/test_security_integration.py
- [[ledger.py]] - code - gateway/ingest_api/ledger.py
- [[sanitizer()]] - code - gateway/tests/conftest.py
- [[state.py]] - code - gateway/ingest_api/state.py
- [[test_audit_chain.py]] - code - gateway/tests/test_audit_chain.py
- [[test_client()]] - code - gateway/tests/conftest.py
- [[test_config()]] - code - gateway/tests/conftest.py
- [[test_config()_1]] - code - gateway/tests/test_mcp_result_endpoint.py
- [[test_config_with_ssh()]] - code - gateway/tests/test_ssh_endpoints.py
- [[test_delete_entry()]] - code - gateway/tests/test_ledger.py
- [[test_delete_nonexistent()]] - code - gateway/tests/test_ledger.py
- [[test_egress_blocks_unauthorized_after_trust_check()]] - code - gateway/tests/test_security_integration.py
- [[test_encrypted_store_in_pipeline()]] - code - gateway/tests/test_security_integration.py
- [[test_full_pipeline_clean_message()]] - code - gateway/tests/test_security_integration.py
- [[test_full_pipeline_pii_message()]] - code - gateway/tests/test_security_integration.py
- [[test_get_entry()]] - code - gateway/tests/test_ledger.py
- [[test_get_stats()_2]] - code - gateway/tests/test_ledger.py
- [[test_initialize_is_idempotent()_1]] - code - gateway/tests/test_ledger.py
- [[test_ledger()]] - code - gateway/tests/conftest.py
- [[test_ledger.py]] - code - gateway/tests/test_ledger.py
- [[test_pii_and_prompt_guard_both_trigger()]] - code - gateway/tests/test_security_integration.py
- [[test_pipeline_concurrent_messages()]] - code - gateway/tests/test_security_integration.py
- [[test_query_ledger()]] - code - gateway/tests/test_ledger.py
- [[test_query_with_filter()]] - code - gateway/tests/test_ledger.py
- [[test_query_with_forwarded_to_filter()]] - code - gateway/tests/test_ledger.py
- [[test_query_with_time_filters()]] - code - gateway/tests/test_ledger.py
- [[test_record_entry()]] - code - gateway/tests/test_ledger.py
- [[test_response_credential_blocking()]] - code - gateway/tests/test_security_integration.py
- [[test_security_integration.py]] - code - gateway/tests/test_security_integration.py
- [[test_trust_insufficient_action_blocked()]] - code - gateway/tests/test_security_integration.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/EgressPolicy
SORT file.name ASC
```

## Connections to other communities
- 35 edges to [[_COMMUNITY_TelegramAPIProxy]]
- 25 edges to [[_COMMUNITY_ResourceGuard]]
- 23 edges to [[_COMMUNITY_ModeRequest]]
- 17 edges to [[_COMMUNITY_ServiceManager]]
- 15 edges to [[_COMMUNITY_TelegramAPIProxy]]
- 14 edges to [[_COMMUNITY_ApprovalRequest]]
- 11 edges to [[_COMMUNITY_SSHProxy]]
- 5 edges to [[_COMMUNITY_test_telegram_proxy_outbound.py]]
- 5 edges to [[_COMMUNITY__wrap_response()]]
- 5 edges to [[_COMMUNITY_MemoryIntegrityMonitor]]
- 5 edges to [[_COMMUNITY_lifespan.py]]
- 4 edges to [[_COMMUNITY_PipelineAction]]
- 3 edges to [[_COMMUNITY_chatbotmain.py]]
- 3 edges to [[_COMMUNITY_Production Safety Checklist (SKILL)]]
- 2 edges to [[_COMMUNITY_TestFluentBitSummary]]
- 2 edges to [[_COMMUNITY_.test_allowed_collaborator_model_command_with_me]]
- 2 edges to [[_COMMUNITY_Test-Driven Development README]]
- 2 edges to [[_COMMUNITY_KeyVaultConfig]]
- 2 edges to [[_COMMUNITY_ConsentFramework]]
- 1 edge to [[_COMMUNITY_main.rs]]
- 1 edge to [[_COMMUNITY_STPA-Sec Analysis of AgentShroud]]
- 1 edge to [[_COMMUNITY_archive_old_events()]]
- 1 edge to [[_COMMUNITY_A2APolicyEngine]]
- 1 edge to [[_COMMUNITY_TestCollaboratorPromptClassifiers]]
- 1 edge to [[_COMMUNITY_RateLimiter]]
- 1 edge to [[_COMMUNITY_start-agentshroud.sh]]
- 1 edge to [[_COMMUNITY_test_daily_cve_report.py]]
- 1 edge to [[_COMMUNITY_GitGuard]]
- 1 edge to [[_COMMUNITY_test_llm_proxy_local_parity.py]]
- 1 edge to [[_COMMUNITY_falco_monitor.py]]
- 1 edge to [[_COMMUNITY_RBACConfig]]
- 1 edge to [[_COMMUNITY_test_soc_bots.py]]
- 1 edge to [[_COMMUNITY_Safe Refactor Specialist]]
- 1 edge to [[_COMMUNITY_EgressApprovalQueue]]

## Top bridge nodes
- [[state.py]] - degree 37, connects to 23 communities
- [[LedgerConfig]] - degree 62, connects to 11 communities
- [[DataLedger]] - degree 67, connects to 10 communities
- [[test_security_integration.py]] - degree 37, connects to 10 communities
- [[.disabled_client()]] - degree 11, connects to 5 communities