---
type: community
members: 57
---

# AuditChain

**Members:** 57 nodes

## Members
- [[dot-__init__()_183]] - code - gateway/proxy/pipeline.py
- [[dot-__init__()_184]] - code - gateway/proxy/pipeline.py
- [[dot-__len__()_1]] - code - gateway/proxy/pipeline.py
- [[dot-_maybe_record_trust_violation()]] - code - gateway/proxy/pipeline.py
- [[dot-_process_inbound_core()]] - code - gateway/proxy/pipeline.py
- [[dot-_process_outbound_core()]] - code - gateway/proxy/pipeline.py
- [[dot-append()_1]] - code - gateway/proxy/pipeline.py
- [[dot-append_block()]] - code - gateway/proxy/pipeline.py
- [[dot-append_owner_bypass()]] - code - gateway/proxy/pipeline.py
- [[dot-entries()_1]] - code - gateway/proxy/pipeline.py
- [[dot-get_stats()_14]] - code - gateway/proxy/pipeline.py
- [[dot-last_hash()_1]] - code - gateway/proxy/pipeline.py
- [[dot-process_inbound()_4]] - code - gateway/proxy/pipeline.py
- [[dot-process_outbound()_5]] - code - gateway/proxy/pipeline.py
- [[dot-test_append_chain()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_append_owner_bypass_persists_high_severity()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_append_single()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_chain_continuity_preserved_across_wrap()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_content_hash_deterministic()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_default_window_is_10k()_1]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_different_content_different_hash()_1]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_entries_returns_copy()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_genesis()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_metadata()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_persisted_event_records_true_previous_hash()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_tamper_in_retained_window_detected()_1]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_unwrapped_chain_must_anchor_at_genesis()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_verify_chain_valid_after_wrap()_1]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_verify_tampered_chain_hash()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_verify_tampered_previous_hash()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_verify_valid()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_window_capped_at_max_entries()_1]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-to_dict()_11]] - code - gateway/proxy/pipeline.py
- [[dot-total_appended()_1]] - code - gateway/proxy/pipeline.py
- [[dot-verify_chain()_2]] - code - gateway/proxy/pipeline.py
- [[A self-consistent window on a forged anchor must fail when the chain never…]] - rationale - gateway/tests/test_pipeline_unit.py
- [[An entry in the SHA-256 hash chain audit ledger.]] - rationale - gateway/proxy/pipeline.py
- [[Any_74]] - code
- [[Append to the chain with guaranteed SQLite persistence. Used exclusively for…]] - rationale - gateway/proxy/pipeline.py
- [[AuditChain]] - code - gateway/proxy/pipeline.py
- [[AuditChainEntry]] - code - gateway/proxy/pipeline.py
- [[PipelineResult]] - code - gateway/proxy/pipeline.py
- [[Process an inbound message through the full security pipeline.]] - rationale - gateway/proxy/pipeline.py
- [[Process an inbound message through the full security pipeline. Thin wrapper…]] - rationale - gateway/proxy/pipeline.py
- [[Process an outbound response through the security pipeline.]] - rationale - gateway/proxy/pipeline.py
- [[Process an outbound response through the security pipeline. Thin wrapper around…]] - rationale - gateway/proxy/pipeline.py
- [[Record a trust-score violation and propagate cross-bot decay. Called once,…]] - rationale - gateway/proxy/pipeline.py
- [[Record an owner guard-bypass in the tamper-evident chain (SCRUM-95). The owner…]] - rationale - gateway/proxy/pipeline.py
- [[Result of running a message through the security pipeline.]] - rationale - gateway/proxy/pipeline.py
- [[SHA-256 hash chain for tamper-evident audit logging.]] - rationale - gateway/proxy/pipeline.py
- [[TestAuditChain_1]] - code - gateway/tests/test_pipeline_unit.py
- [[TestAuditChainBounded]] - code - gateway/tests/test_pipeline_unit.py
- [[Tests for the SHA-256 hash chain.]] - rationale - gateway/tests/test_pipeline_unit.py
- [[The fire-and-forget SQLite log must record the entry's actual previous_hash,…]] - rationale - gateway/tests/test_pipeline_unit.py
- [[The in-memory window must be bounded; full history lives in SQLite.]] - rationale - gateway/tests/test_pipeline_unit.py
- [[Verify the integrity of the retained hash-chain window. When the bounded window…]] - rationale - gateway/proxy/pipeline.py
- [[append_owner_bypass writes to the hash chain AND persists a HIGH 'owner_bypass'…]] - rationale - gateway/tests/test_pipeline_unit.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/AuditChain
SORT file.name ASC
```

## Connections to other communities
- 7 edges to [[_COMMUNITY_SecurityPipeline]]
- 5 edges to [[_COMMUNITY_test_e2e_proxy.py]]
- 5 edges to [[_COMMUNITY_asyncio_1]]
- 3 edges to [[_COMMUNITY_test_e2e_watchtower.py]]
- 3 edges to [[_COMMUNITY_lifespan.py]]
- 2 edges to [[_COMMUNITY_AsyncMock]]
- 2 edges to [[_COMMUNITY_WebProxy]]
- 2 edges to [[_COMMUNITY_test_telegram_pipeline.py]]
- 2 edges to [[_COMMUNITY_socmodels.py]]
- 1 edge to [[_COMMUNITY_middleware.py]]

## Top bridge nodes
- [[AuditChain]] - degree 43, connects to 5 communities
- [[PipelineResult]] - degree 10, connects to 2 communities
- [[dot-_process_inbound_core()]] - degree 6, connects to 2 communities
- [[dot-_process_outbound_core()]] - degree 6, connects to 2 communities
- [[dot-test_append_owner_bypass_persists_high_severity()]] - degree 5, connects to 2 communities
