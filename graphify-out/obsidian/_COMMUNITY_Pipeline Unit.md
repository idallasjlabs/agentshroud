---
type: community
cohesion: 0.08
members: 38
---

# Pipeline Unit

**Cohesion:** 0.08 - loosely connected
**Members:** 38 nodes

## Members
- [[.__init__()_33]] - code - gateway/proxy/pipeline.py
- [[.__len__()_1]] - code - gateway/proxy/pipeline.py
- [[.last_hash()_1]] - code - gateway/proxy/pipeline.py
- [[.test_append_chain()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_append_owner_bypass_persists_high_severity()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_append_single()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_audit_chain_hash_chained()]] - code - gateway/tests/test_e2e_watchtower.py
- [[.test_chain_continuity_preserved_across_wrap()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_content_hash_deterministic()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_default_window_is_10k()_1]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_different_content_different_hash()_1]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_entries_returns_copy()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_genesis()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_metadata()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_persisted_event_records_true_previous_hash()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_tamper_in_retained_window_detected()_1]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_unwrapped_chain_must_anchor_at_genesis()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_verify_chain_valid_after_wrap()_1]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_verify_tampered_chain_hash()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_verify_tampered_previous_hash()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_verify_valid()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_window_capped_at_max_entries()_1]] - code - gateway/tests/test_pipeline_unit.py
- [[.total_appended()_1]] - code - gateway/proxy/pipeline.py
- [[A self-consistent window on a forged anchor must fail when the         chain nev]] - rationale - gateway/tests/test_pipeline_unit.py
- [[Audit chain is a hash chain each entry references the previous hash.]] - rationale - gateway/tests/test_e2e_watchtower.py
- [[AuditChain]] - code - gateway/proxy/pipeline.py
- [[SHA-256 hash chain for tamper-evident audit logging.]] - rationale - gateway/proxy/pipeline.py
- [[TestAuditChain]] - code - gateway/tests/test_pipeline_unit.py
- [[TestAuditChainBounded]] - code - gateway/tests/test_pipeline_unit.py
- [[Tests for the SHA-256 hash chain.]] - rationale - gateway/tests/test_pipeline_unit.py
- [[The fire-and-forget SQLite log must record the entry's actual         previous_h]] - rationale - gateway/tests/test_pipeline_unit.py
- [[The in-memory window must be bounded; full history lives in SQLite.]] - rationale - gateway/tests/test_pipeline_unit.py
- [[Verify empty audit chain is valid.]] - rationale - gateway/tests/test_e2e_proxy.py
- [[Verify single-entry chain is valid.]] - rationale - gateway/tests/test_e2e_proxy.py
- [[append_owner_bypass writes to the hash chain AND persists a HIGH         'owner_]] - rationale - gateway/tests/test_pipeline_unit.py
- [[audit_chain()]] - code - gateway/tests/test_web_proxy.py
- [[test_audit_chain_empty_valid()]] - code - gateway/tests/test_e2e_proxy.py
- [[test_audit_chain_single_entry()]] - code - gateway/tests/test_e2e_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Pipeline_Unit
SORT file.name ASC
```

## Connections to other communities
- 23 edges to [[_COMMUNITY_Security Audit & Watchtower Tests]]
- 22 edges to [[_COMMUNITY_Pipeline Unit]]
- 17 edges to [[_COMMUNITY_Web Proxy]]
- 7 edges to [[_COMMUNITY_Key Vault]]
- 5 edges to [[_COMMUNITY_Pipeline (proxy)]]
- 5 edges to [[_COMMUNITY_E2e Proxy]]
- 3 edges to [[_COMMUNITY_Cross Bot Trust Ledger]]
- 3 edges to [[_COMMUNITY_Tool Chain & CVE Triage]]
- 2 edges to [[_COMMUNITY_Tool ACL & Group RBAC]]
- 2 edges to [[_COMMUNITY_Outbound Filter]]
- 2 edges to [[_COMMUNITY_Security Regressions V1 2]]
- 2 edges to [[_COMMUNITY_Slack Proxy Coverage]]
- 1 edge to [[_COMMUNITY_Mcp Audit (proxy)]]
- 1 edge to [[_COMMUNITY_Killswitch Monitor & Observatory Mode]]
- 1 edge to [[_COMMUNITY_Progressive Trust Integration]]
- 1 edge to [[_COMMUNITY_Web Proxy]]
- 1 edge to [[_COMMUNITY_Web Proxy]]

## Top bridge nodes
- [[AuditChain]] - degree 89, connects to 14 communities
- [[TestAuditChain]] - degree 27, connects to 7 communities
- [[TestAuditChainBounded]] - degree 25, connects to 7 communities
- [[.__init__()_33]] - degree 3, connects to 2 communities
- [[.test_append_owner_bypass_persists_high_severity()]] - degree 4, connects to 1 community