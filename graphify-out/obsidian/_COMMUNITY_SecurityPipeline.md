---
type: community
members: 89
---

# SecurityPipeline

**Members:** 89 nodes

## Members
- [[dot-_blocking_prompt_guard()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-_passthrough_pii()_1]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-_pipeline()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-_pipeline_with_trust()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-_redacting_pii()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-set_global_mode()]] - code - gateway/proxy/pipeline.py
- [[dot-test_block_clean_message_forwards()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_blocked_request_decays_trust_score()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_blocked_request_propagates_to_cross_bot_peer()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_clean_message_passes()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_clean_request_does_not_touch_trust_score()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_context_guard_error_fails_closed()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_critical_injection_blocks()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_envelope_metadata_in_audit_entry()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_full_trust_tool_result_injection_audited_not_blocked()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_high_injection_blocks()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_high_score_forwards_and_records()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_inbound_block()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_inbound_redact_unchanged()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_lockdown_block_is_audited()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_lockdown_score_allows_owner()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_lockdown_score_blocks_non_owner()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_missing_trust_manager_does_not_raise()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_no_context_guard_passes_through()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_no_outbound_filter_does_not_unbind()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_no_scorer_leaves_result_unscored()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_no_signer_leaves_envelope_empty()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_non_owner_block_does_not_emit_owner_bypass()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_non_owner_inbound_query_still_redacted()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_outbound_block()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_outbound_redact_unchanged()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_owner_bypass_audited_at_every_guard()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_owner_bypass_is_recorded_in_audit_chain()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_owner_exempted_block_does_not_decay_trust()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_owner_inbound_query_not_pii_redacted()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_pipeline_raises_with_only_prompt_guard()]] - code - gateway/tests/test_e2e_watchtower.py
- [[dot-test_pipeline_raises_without_pii_sanitizer()]] - code - gateway/tests/test_e2e_watchtower.py
- [[dot-test_repetition_attack_does_not_block()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_scorer_error_allows_owner()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_scorer_error_fails_closed_non_owner()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_scorer_invoked_with_session_segments()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_signer_failure_never_blocks()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_skip_context_guard_bypasses_step0()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_standard_trust_tool_result_injection_is_blocked()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_tool_result_uses_wrap_tool_result()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_untrusted_tool_result_injection_is_blocked()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_warn_zone_forwards()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-verify_audit_chain()]] - code - gateway/proxy/pipeline.py
- [[0.3 ≤ score  0.6 warns but never blocks.]] - rationale - gateway/tests/test_pipeline_unit.py
- [[Attempting to create a pipeline with no PII sanitizer raises RuntimeError.]] - rationale - gateway/tests/test_e2e_watchtower.py
- [[ContextGuard must run in SecurityPipeline.process_inbound() — A2.]] - rationale - gateway/tests/test_pipeline_unit.py
- [[ContextIntegrityScorer must run in process_inbound() — C21 wiring.]] - rationale - gateway/tests/test_pipeline_unit.py
- [[E2E-10 SecurityPipeline refuses to operate without PII sanitizer.]] - rationale - gateway/tests/test_e2e_watchtower.py
- [[EnvelopeSigner must attest outbound responses — C46 wiring.]] - rationale - gateway/tests/test_pipeline_unit.py
- [[Even with PromptGuard, pipeline refuses to start without PII sanitizer.]] - rationale - gateway/tests/test_e2e_watchtower.py
- [[FULL-trust owner response scan runs, detection audited, delivery NOT blocked.]] - rationale - gateway/tests/test_pipeline_unit.py
- [[Main security pipeline that all messages pass through. Wires together…]] - rationale - gateway/proxy/pipeline.py
- [[Minimal SecurityPipeline with a real PII sanitizer stub.]] - rationale - gateway/tests/test_pipeline_unit.py
- [[No trust_manager configured — the hook must no-op, not crash the request path.]] - rationale - gateway/tests/test_pipeline_unit.py
- [[Non-owner query must still be PII-scrubbed (detector + threshold unchanged).]] - rationale - gateway/tests/test_pipeline_unit.py
- [[Owner messages that would trip a guard are logged but never blocked —…]] - rationale - gateway/tests/test_pipeline_unit.py
- [[Owner query must pass through PII sanitisation unchanged; sanitiser not called.]] - rationale - gateway/tests/test_pipeline_unit.py
- [[PII sanitiser mock that simulates two entity redactions.]] - rationale - gateway/tests/test_pipeline_unit.py
- [[Pipeline must refuse to start without PII sanitizer (fail-closed).]] - rationale - gateway/tests/test_redteam_probes.py
- [[Pipeline with ContextGuard + ContextIntegrityScorer mocks.]] - rationale - gateway/tests/test_pipeline_unit.py
- [[SCRUM-202 enforcement_action=block must actually block in the pipeline.]] - rationale - gateway/tests/test_pipeline_unit.py
- [[STANDARD-trust source also blocked — only FULL bypasses the block.]] - rationale - gateway/tests/test_pipeline_unit.py
- [[SecurityPipeline]] - code - gateway/proxy/pipeline.py
- [[SecurityPipeline._maybe_record_trust_violation — centralized hook that fires…]] - rationale - gateway/tests/test_pipeline_unit.py
- [[Set global observatory mode for all security modules. Args mode monitor or…]] - rationale - gateway/proxy/pipeline.py
- [[Step 1.76 PromptGuard tool-result scan must respect user_trust_level.…]] - rationale - gateway/tests/test_pipeline_unit.py
- [[Step 2 PII sanitisation must be skipped for the authenticated owner. Non-owner…]] - rationale - gateway/tests/test_pipeline_unit.py
- [[TestContextGuardInPipeline]] - code - gateway/tests/test_pipeline_unit.py
- [[TestContextIntegrityInPipeline]] - code - gateway/tests/test_pipeline_unit.py
- [[TestE2E10FailClosed]] - code - gateway/tests/test_e2e_watchtower.py
- [[TestEnvelopeSignerInPipeline]] - code - gateway/tests/test_pipeline_unit.py
- [[TestInboundPIIOwnerExemption]] - code - gateway/tests/test_pipeline_unit.py
- [[TestPIIBlockModeInPipeline]] - code - gateway/tests/test_pipeline_unit.py
- [[TestPromptGuardToolResultTrustGate]] - code - gateway/tests/test_pipeline_unit.py
- [[TestTrustViolationRecording]] - code - gateway/tests/test_pipeline_unit.py
- [[UNTRUSTED source tool-result injection scan blocks as before (CVE-2026-31045).]] - rationale - gateway/tests/test_pipeline_unit.py
- [[_FakeAttack]] - code - gateway/tests/test_pipeline_unit.py
- [[_FakeIntegrityScore]] - code - gateway/tests/test_pipeline_unit.py
- [[_make_integrity_pipeline()]] - code - gateway/tests/test_pipeline_unit.py
- [[_make_pipeline()_1]] - code - gateway/tests/test_pipeline_unit.py
- [[_make_signer_pipeline()]] - code - gateway/tests/test_pipeline_unit.py
- [[asyncio_34]] - code
- [[skip_context_guard=True must prevent ContextGuard from running — used by…]] - rationale - gateway/tests/test_pipeline_unit.py
- [[test_pipeline_fails_closed_without_pii()]] - code - gateway/tests/test_redteam_probes.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/SecurityPipeline
SORT file.name ASC
```

## Connections to other communities
- 24 edges to [[_COMMUNITY_TrustManager]]
- 16 edges to [[_COMMUNITY_lifespan.py]]
- 10 edges to [[_COMMUNITY_TestKeyLeakDetection]]
- 9 edges to [[_COMMUNITY_AsyncMock]]
- 9 edges to [[_COMMUNITY_AuditChain]]
- 6 edges to [[_COMMUNITY_test_e2e_watchtower.py]]
- 5 edges to [[_COMMUNITY_PipelineAction]]
- 5 edges to [[_COMMUNITY_OutboundInfoFilter]]
- 5 edges to [[_COMMUNITY_EnvelopeSigner]]
- 3 edges to [[_COMMUNITY_DataExfilVolumeGuard]]
- 3 edges to [[_COMMUNITY_TestObservatoryMode]]
- 3 edges to [[_COMMUNITY_RateLimitGuard]]
- 3 edges to [[_COMMUNITY_prompt_guard.py]]
- 2 edges to [[_COMMUNITY_ToolResultInjectionScanner]]
- 2 edges to [[_COMMUNITY_run]]
- 2 edges to [[_COMMUNITY_test_ws_e_rt2_inbound_encoding.py]]
- 2 edges to [[_COMMUNITY_ingest_apimain.py]]
- 2 edges to [[_COMMUNITY_test_docs_accuracy.py]]
- 2 edges to [[_COMMUNITY_test_e2e_proxy.py]]
- 1 edge to [[_COMMUNITY_MiddlewareManager]]
- 1 edge to [[_COMMUNITY_socrouter.py]]
- 1 edge to [[_COMMUNITY_test_observatory_mode.py]]
- 1 edge to [[_COMMUNITY_lifespan]]
- 1 edge to [[_COMMUNITY_ProgressiveTrustConfig]]

## Top bridge nodes
- [[SecurityPipeline]] - degree 83, connects to 21 communities
- [[asyncio_34]] - degree 45, connects to 4 communities
- [[TestContextGuardInPipeline]] - degree 15, connects to 3 communities
- [[TestPIIBlockModeInPipeline]] - degree 12, connects to 3 communities
- [[_make_signer_pipeline()]] - degree 7, connects to 3 communities
