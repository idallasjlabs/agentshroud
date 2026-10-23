---
type: community
cohesion: 0.08
members: 38
---

# AuditChain

**Cohesion:** 0.08 - loosely connected
**Members:** 38 nodes

## Members
- [[dot-__init__()_87]] - code - gateway/proxy/pipeline.py
- [[dot-__len__()_1]] - code - gateway/proxy/pipeline.py
- [[dot-entries()_1]] - code - gateway/proxy/pipeline.py
- [[dot-last_hash()_1]] - code - gateway/proxy/pipeline.py
- [[dot-test_append_chain()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_append_owner_bypass_persists_high_severity()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_append_single()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_audit_chain_hash_chained()]] - code - gateway/tests/test_e2e_watchtower.py
- [[dot-test_blocked_message_has_audit_entry()]] - code - gateway/tests/test_e2e_watchtower.py
- [[dot-test_chain_continuity_preserved_across_wrap()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_content_hash_deterministic()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_default_window_is_10k()_1]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_different_content_different_hash()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_entries_returns_copy()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_forwarded_message_has_audit_entry()]] - code - gateway/tests/test_e2e_watchtower.py
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
- [[dot-total_appended()_1]] - code - gateway/proxy/pipeline.py
- [[A self-consistent window on a forged anchor must fail when the         chain nev]] - rationale - gateway/tests/test_pipeline_unit.py
- [[Audit chain is a hash chain each entry references the previous hash.]] - rationale - gateway/tests/test_e2e_watchtower.py
- [[AuditChain]] - code - gateway/proxy/pipeline.py
- [[E2E-08 Every pipeline event — block or forward — produces an audit entry.]] - rationale - gateway/tests/test_e2e_watchtower.py
- [[SHA-256 hash chain for tamper-evident audit logging.]] - rationale - gateway/proxy/pipeline.py
- [[TestAuditChain]] - code - gateway/tests/test_pipeline_unit.py
- [[TestAuditChainBounded]] - code - gateway/tests/test_pipeline_unit.py
- [[TestE2E08AuditChainIntegrity]] - code - gateway/tests/test_e2e_watchtower.py
- [[Tests for the SHA-256 hash chain.]] - rationale - gateway/tests/test_pipeline_unit.py
- [[The fire-and-forget SQLite log must record the entry's actual         previous_h]] - rationale - gateway/tests/test_pipeline_unit.py
- [[The in-memory window must be bounded; full history lives in SQLite.]] - rationale - gateway/tests/test_pipeline_unit.py
- [[append_owner_bypass writes to the hash chain AND persists a HIGH         'owner_]] - rationale - gateway/tests/test_pipeline_unit.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/AuditChain
SORT file.name ASC
```

## Connections to other communities
- 30 edges to [[_COMMUNITY_KeyVaultConfig]]
- 17 edges to [[_COMMUNITY_test_soc_realtime_coverage.py]]
- 17 edges to [[_COMMUNITY_SecurityPipeline (2)]]
- 13 edges to [[_COMMUNITY_ApprovalQueueConfig]]
- 7 edges to [[_COMMUNITY_socrouter.py]]
- 6 edges to [[_COMMUNITY_AgentTarget]]
- 4 edges to [[_COMMUNITY_KeyVault]]
- 2 edges to [[_COMMUNITY_api.py (2)]]
- 2 edges to [[_COMMUNITY_MiddlewareManager (2)]]
- 1 edge to [[_COMMUNITY_ContextGuard]]
- 1 edge to [[_COMMUNITY_What Does OpenClaw Actually Need to Write]]
- 1 edge to [[_COMMUNITY_KillSwitchMonitor]]
- 1 edge to [[_COMMUNITY_TestAllowlistMode]]
- 1 edge to [[_COMMUNITY_AgentShroud v0.8.0 — 25-Domain Prompt Injection Defense Assessment & Roadmap]]
- 1 edge to [[_COMMUNITY_openclawskillsi-crSKILL]]
- 1 edge to [[_COMMUNITY_MCPPermissionManager]]
- 1 edge to [[_COMMUNITY_test_agent_cve_registry.py (2)]]
- 1 edge to [[_COMMUNITY_PromptGuard]]

## Top bridge nodes
- [[AuditChain]] - degree 89, connects to 11 communities
- [[TestE2E08AuditChainIntegrity]] - degree 16, connects to 8 communities
- [[TestAuditChain]] - degree 27, connects to 4 communities
- [[TestAuditChainBounded]] - degree 25, connects to 4 communities
- [[dot-__init__()_87]] - degree 3, connects to 2 communities
