---
type: community
cohesion: 0.13
members: 24
---

# PipelineAction

**Cohesion:** 0.13 - loosely connected
**Members:** 24 nodes

## Members
- [[dot-_maybe_record_trust_violation()]] - code - gateway/proxy/pipeline.py
- [[dot-_process_inbound_core()]] - code - gateway/proxy/pipeline.py
- [[dot-_process_outbound_core()]] - code - gateway/proxy/pipeline.py
- [[dot-append()_1]] - code - gateway/proxy/pipeline.py
- [[dot-append_block()]] - code - gateway/proxy/pipeline.py
- [[dot-append_owner_bypass()]] - code - gateway/proxy/pipeline.py
- [[dot-entries()_1]] - code - gateway/proxy/pipeline.py
- [[dot-get_stats()_15]] - code - gateway/proxy/pipeline.py
- [[dot-process_inbound()_5]] - code - gateway/proxy/pipeline.py
- [[dot-process_outbound()_6]] - code - gateway/proxy/pipeline.py
- [[dot-to_dict()_8]] - code - gateway/proxy/pipeline.py
- [[dot-verify_audit_chain()]] - code - gateway/proxy/pipeline.py
- [[dot-verify_chain()_1]] - code - gateway/proxy/pipeline.py
- [[An entry in the SHA-256 hash chain audit ledger.]] - rationale - gateway/proxy/pipeline.py
- [[Any_51]] - code - gateway/proxy/pipeline.py
- [[Append to the chain with guaranteed SQLite persistence.          Used exclusivel]] - rationale - gateway/proxy/pipeline.py
- [[AuditChainEntry]] - code - gateway/proxy/pipeline.py
- [[Process an inbound message through the full security pipeline.]] - rationale - gateway/proxy/pipeline.py
- [[Process an inbound message through the full security pipeline.          Thin wra]] - rationale - gateway/proxy/pipeline.py
- [[Process an outbound response through the security pipeline.]] - rationale - gateway/proxy/pipeline.py
- [[Process an outbound response through the security pipeline.          Thin wrappe]] - rationale - gateway/proxy/pipeline.py
- [[Record a trust-score violation and propagate cross-bot decay.          Called on]] - rationale - gateway/proxy/pipeline.py
- [[Record an owner guard-bypass in the tamper-evident chain (SCRUM-95).          Th]] - rationale - gateway/proxy/pipeline.py
- [[Verify the integrity of the retained hash-chain window.          When the bounde]] - rationale - gateway/proxy/pipeline.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/PipelineAction
SORT file.name ASC
```

## Connections to other communities
- 10 edges to [[_COMMUNITY_AuditChain]]
- 7 edges to [[_COMMUNITY_PIIConfig]]
- 6 edges to [[_COMMUNITY_PipelineAction]]
- 2 edges to [[_COMMUNITY_TrustConfig]]
- 2 edges to [[_COMMUNITY_RBACConfig]]
- 2 edges to [[_COMMUNITY_CrossBotTrustLedger]]

## Top bridge nodes
- [[Any_51]] - degree 14, connects to 4 communities
- [[AuditChainEntry]] - degree 11, connects to 4 communities
- [[dot-_process_inbound_core()]] - degree 8, connects to 2 communities
- [[dot-_process_outbound_core()]] - degree 7, connects to 2 communities
- [[dot-process_inbound()_5]] - degree 6, connects to 2 communities
