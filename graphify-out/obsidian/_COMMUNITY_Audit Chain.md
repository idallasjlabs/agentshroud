---
type: community
cohesion: 0.05
members: 39
---

# Audit Chain

**Cohesion:** 0.05 - loosely connected
**Members:** 39 nodes

## Members
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
- [[Can retrieve specific entry by ID for verification.]] - rationale - gateway/tests/test_audit_chain.py
- [[Chain with many entries — verify integrity.]] - rationale - gateway/tests/test_audit_chain.py
- [[Concurrent writes and reads don't conflict.]] - rationale - gateway/tests/test_audit_chain.py
- [[Concurrent writes to chain.]] - rationale - gateway/tests/test_audit_chain.py
- [[Content hash should be a valid SHA-256 hex digest.]] - rationale - gateway/tests/test_audit_chain.py
- [[Deleted entry is gone (right to erasure).]] - rationale - gateway/tests/test_audit_chain.py
- [[Deleting nonexistent entry returns False.]] - rationale - gateway/tests/test_audit_chain.py
- [[Different content should produce different hashes.]] - rationale - gateway/tests/test_audit_chain.py
- [[Export chain and re-verify.]] - rationale - gateway/tests/test_audit_chain.py
- [[Filter entries by source.]] - rationale - gateway/tests/test_audit_chain.py
- [[Looking up nonexistent entry returns None.]] - rationale - gateway/tests/test_audit_chain.py
- [[Paginated queries return correct subsets.]] - rationale - gateway/tests/test_audit_chain.py
- [[Retention enforcement removes expired entries.]] - rationale - gateway/tests/test_audit_chain.py
- [[Retention enforcement.]] - rationale - gateway/tests/test_audit_chain.py
- [[Stats reflect actual data.]] - rationale - gateway/tests/test_audit_chain.py
- [[Tamper detection at various chain positions.]] - rationale - gateway/tests/test_audit_chain.py
- [[TestAuditChainIntegrity]] - code - gateway/tests/test_audit_chain.py
- [[TestChainExportAndVerification]] - code - gateway/tests/test_audit_chain.py
- [[TestConcurrentWrites]] - code - gateway/tests/test_audit_chain.py
- [[TestRetention]] - code - gateway/tests/test_audit_chain.py
- [[TestTamperDetection]] - code - gateway/tests/test_audit_chain.py
- [[Verify hash matches SHA-256 of the content.]] - rationale - gateway/tests/test_audit_chain.py
- [[Write 1000 entries and verify they're all there.]] - rationale - gateway/tests/test_audit_chain.py
- [[test_audit_chain.py]] - code - gateway/tests/test_audit_chain.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Audit_Chain
SORT file.name ASC
```

## Connections to other communities
- 13 edges to [[_COMMUNITY_Security Fixes & SSH Write Endpoint]]

## Top bridge nodes
- [[test_audit_chain.py]] - degree 8, connects to 1 community
- [[TestAuditChainIntegrity]] - degree 8, connects to 1 community
- [[TestTamperDetection]] - degree 8, connects to 1 community
- [[TestChainExportAndVerification]] - degree 7, connects to 1 community
- [[TestConcurrentWrites]] - degree 6, connects to 1 community