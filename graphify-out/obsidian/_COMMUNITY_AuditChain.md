---
type: community
cohesion: 0.08
members: 38
---

# AuditChain

**Cohesion:** 0.08 - loosely connected
**Members:** 38 nodes

## Members
- [[dot-__init__()_77]] - code - gateway/proxy/pipeline.py
- [[dot-__len__()]] - code - gateway/proxy/pipeline.py
- [[dot-get_stats()_10]] - code - gateway/proxy/pipeline.py
- [[dot-last_hash()]] - code - gateway/proxy/pipeline.py
- [[dot-test_append_chain()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_append_owner_bypass_persists_high_severity()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_append_single()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_audit_chain_hash_chained()]] - code - gateway/tests/test_e2e_watchtower.py
- [[dot-test_chain_continuity_preserved_across_wrap()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_content_hash_deterministic()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_default_window_is_10k()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_different_content_different_hash()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_entries_returns_copy()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_genesis()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_metadata()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_persisted_event_records_true_previous_hash()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_tamper_in_retained_window_detected()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_unwrapped_chain_must_anchor_at_genesis()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_verify_chain_valid_after_wrap()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_verify_tampered_chain_hash()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_verify_tampered_previous_hash()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_verify_valid()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_window_capped_at_max_entries()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-total_appended()]] - code - gateway/proxy/pipeline.py
- [[dot-verify_audit_chain()]] - code - gateway/proxy/pipeline.py
- [[dot-verify_chain()]] - code - gateway/proxy/pipeline.py
- [[A self-consistent window on a forged anchor must fail when the         chain nev]] - rationale - gateway/tests/test_pipeline_unit.py
- [[Audit chain is a hash chain each entry references the previous hash.]] - rationale - gateway/tests/test_e2e_watchtower.py
- [[AuditChain]] - code - gateway/proxy/pipeline.py
- [[SHA-256 hash chain for tamper-evident audit logging.]] - rationale - gateway/proxy/pipeline.py
- [[TestAuditChain_1]] - code - gateway/tests/test_pipeline_unit.py
- [[TestAuditChainBounded]] - code - gateway/tests/test_pipeline_unit.py
- [[Tests for the SHA-256 hash chain.]] - rationale - gateway/tests/test_pipeline_unit.py
- [[The fire-and-forget SQLite log must record the entry's actual         previous_h]] - rationale - gateway/tests/test_pipeline_unit.py
- [[The in-memory window must be bounded; full history lives in SQLite.]] - rationale - gateway/tests/test_pipeline_unit.py
- [[Verify the integrity of the retained hash-chain window.          When the bounde]] - rationale - gateway/proxy/pipeline.py
- [[append_owner_bypass writes to the hash chain AND persists a HIGH         'owner_]] - rationale - gateway/tests/test_pipeline_unit.py
- [[audit_chain()]] - code - gateway/tests/test_web_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/AuditChain
SORT file.name ASC
```

## Connections to other communities
- 22 edges to [[_COMMUNITY_PIIConfig]]
- 17 edges to [[_COMMUNITY_WebProxyConfig]]
- 16 edges to [[_COMMUNITY_OutboundInfoFilter]]
- 7 edges to [[_COMMUNITY_PipelineAction]]
- 7 edges to [[_COMMUNITY_KeyVault]]
- 6 edges to [[_COMMUNITY_test_e2e_proxy.py]]
- 5 edges to [[_COMMUNITY_EnvelopeSigner]]
- 3 edges to [[_COMMUNITY_TrustConfig]]
- 3 edges to [[_COMMUNITY_InjectionAction]]
- 3 edges to [[_COMMUNITY_CrossBotTrustLedger]]
- 3 edges to [[_COMMUNITY__FakeAttack]]
- 2 edges to [[_COMMUNITY_RBACConfig]]
- 2 edges to [[_COMMUNITY_AsyncMock]]
- 1 edge to [[_COMMUNITY_TestAuditChain]]
- 1 edge to [[_COMMUNITY_KillSwitchMonitor]]
- 1 edge to [[_COMMUNITY_TestSSRFBlocking]]
- 1 edge to [[_COMMUNITY_MCPAuditTrail]]

## Top bridge nodes
- [[AuditChain]] - degree 89, connects to 16 communities
- [[TestAuditChain_1]] - degree 27, connects to 8 communities
- [[TestAuditChainBounded]] - degree 25, connects to 8 communities
- [[dot-get_stats()_10]] - degree 3, connects to 2 communities
- [[dot-__init__()_77]] - degree 3, connects to 2 communities
