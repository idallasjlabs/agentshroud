---
type: community
cohesion: 0.14
members: 26
---

# _FakeAttack

**Cohesion:** 0.14 - loosely connected
**Members:** 26 nodes

## Members
- [[dot-_pipeline_with_trust()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_blocked_request_decays_trust_score()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_blocked_request_propagates_to_cross_bot_peer()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_clean_message_passes()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_clean_request_does_not_touch_trust_score()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_context_guard_error_fails_closed()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_critical_injection_blocks()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_high_injection_blocks()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_missing_trust_manager_does_not_raise()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_no_context_guard_passes_through()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_non_owner_block_does_not_emit_owner_bypass()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_owner_bypass_audited_at_every_guard()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_owner_bypass_is_recorded_in_audit_chain()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_owner_exempted_block_does_not_decay_trust()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_repetition_attack_does_not_block()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_skip_context_guard_bypasses_step0()]] - code - gateway/tests/test_pipeline_unit.py
- [[ContextGuard must run in SecurityPipeline.process_inbound() — A2.]] - rationale - gateway/tests/test_pipeline_unit.py
- [[Minimal SecurityPipeline with a real PII sanitizer stub.]] - rationale - gateway/tests/test_pipeline_unit.py
- [[No trust_manager configured — the hook must no-op, not crash the         request]] - rationale - gateway/tests/test_pipeline_unit.py
- [[Owner messages that would trip a guard are logged but never         blocked — re]] - rationale - gateway/tests/test_pipeline_unit.py
- [[SecurityPipeline._maybe_record_trust_violation — centralized hook that     fires]] - rationale - gateway/tests/test_pipeline_unit.py
- [[TestContextGuardInPipeline]] - code - gateway/tests/test_pipeline_unit.py
- [[TestTrustViolationRecording]] - code - gateway/tests/test_pipeline_unit.py
- [[_FakeAttack]] - code - gateway/tests/test_pipeline_unit.py
- [[_make_pipeline()_3]] - code - gateway/tests/test_pipeline_unit.py
- [[skip_context_guard=True must prevent ContextGuard from running — used by Telegra]] - rationale - gateway/tests/test_pipeline_unit.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/_FakeAttack
SORT file.name ASC
```

## Connections to other communities
- 15 edges to [[_COMMUNITY_OutboundInfoFilter]]
- 10 edges to [[_COMMUNITY_PIIConfig]]
- 9 edges to [[_COMMUNITY_KeyVault]]
- 7 edges to [[_COMMUNITY_EnvelopeSigner]]
- 5 edges to [[_COMMUNITY_AsyncMock]]
- 4 edges to [[_COMMUNITY_TrustConfig]]
- 3 edges to [[_COMMUNITY_PipelineAction]]
- 3 edges to [[_COMMUNITY_InjectionAction]]
- 3 edges to [[_COMMUNITY_AuditChain]]
- 3 edges to [[_COMMUNITY_CrossBotTrustLedger]]

## Top bridge nodes
- [[_FakeAttack]] - degree 27, connects to 9 communities
- [[TestContextGuardInPipeline]] - degree 27, connects to 9 communities
- [[TestTrustViolationRecording]] - degree 23, connects to 9 communities
- [[_make_pipeline()_3]] - degree 17, connects to 4 communities
- [[dot-_pipeline_with_trust()]] - degree 9, connects to 3 communities
