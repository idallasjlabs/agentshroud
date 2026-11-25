---
type: community
members: 84
---

# asyncio

**Members:** 84 nodes

## Members
- [[dot-_blocking_prompt_guard()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-_make_vault_pipeline()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-_passthrough_pii()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-_passthrough_pii()_1]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-_pipeline()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-_pipeline_with_trust()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_block_clean_message_forwards()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_blocked_request_decays_trust_score()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_blocked_request_propagates_to_cross_bot_peer()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_clean_message_passes()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_clean_request_does_not_touch_trust_score()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_clean_response_passes_unchanged()_1]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_context_guard_error_fails_closed()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_critical_injection_blocks()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_detector_failure_fails_closed_for_non_owner()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_envelope_metadata_in_audit_entry()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_full_trust_tool_result_injection_audited_not_blocked()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_generic_key_pattern_audited_but_not_blocked()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_high_injection_blocks()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_high_score_forwards_and_records()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_inbound_block()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_inbound_redact_unchanged()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_key_leak_increments_sanitized_stat_and_audits()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_lockdown_block_is_audited()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_lockdown_score_allows_owner()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_lockdown_score_blocks_non_owner()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_missing_trust_manager_does_not_raise()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_no_context_guard_passes_through()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_no_outbound_filter_does_not_unbind()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_no_scorer_leaves_result_unscored()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_no_signer_leaves_envelope_empty()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_non_owner_block_does_not_emit_owner_bypass()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_outbound_block()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_outbound_filter_still_escalates_fabricated_notice()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_outbound_redact_unchanged()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_outbound_response_is_signed_and_verifiable()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_owner_bypass_audited_at_every_guard()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_owner_bypass_is_recorded_in_audit_chain()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_owner_exempted_block_does_not_decay_trust()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_repetition_attack_does_not_block()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_scorer_error_allows_owner()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_scorer_error_fails_closed_non_owner()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_scorer_invoked_with_session_segments()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_signer_failure_never_blocks()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_skip_context_guard_bypasses_step0()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_standard_trust_tool_result_injection_is_blocked()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_stored_key_value_redacted_from_outbound()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_tool_result_uses_wrap_tool_result()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_untrusted_tool_result_injection_is_blocked()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_warn_zone_forwards()]] - code - gateway/tests/test_pipeline_unit.py
- [[0.3 ≤ score  0.6 warns but never blocks.]] - rationale - gateway/tests/test_pipeline_unit.py
- [[ContextGuard must run in SecurityPipeline.process_inbound() — A2.]] - rationale - gateway/tests/test_pipeline_unit.py
- [[ContextIntegrityScorer must run in process_inbound() — C21 wiring.]] - rationale - gateway/tests/test_pipeline_unit.py
- [[EnvelopeSigner must attest outbound responses — C46 wiring.]] - rationale - gateway/tests/test_pipeline_unit.py
- [[FULL-trust owner response scan runs, detection audited, delivery NOT blocked.]] - rationale - gateway/tests/test_pipeline_unit.py
- [[KeyLeakDetector wiring — stored credential values must never leave the gateway.]] - rationale - gateway/tests/test_pipeline_unit.py
- [[Minimal SecurityPipeline with a real PII sanitizer stub.]] - rationale - gateway/tests/test_pipeline_unit.py
- [[No trust_manager configured — the hook must no-op, not crash the request path.]] - rationale - gateway/tests/test_pipeline_unit.py
- [[Owner messages that would trip a guard are logged but never blocked —…]] - rationale - gateway/tests/test_pipeline_unit.py
- [[Pipeline with ContextGuard + ContextIntegrityScorer mocks.]] - rationale - gateway/tests/test_pipeline_unit.py
- [[Regression filter_result was possibly-unbound in process_outbound when no…]] - rationale - gateway/tests/test_pipeline_unit.py
- [[SCRUM-202 enforcement_action=block must actually block in the pipeline.]] - rationale - gateway/tests/test_pipeline_unit.py
- [[STANDARD-trust source also blocked — only FULL bypasses the block.]] - rationale - gateway/tests/test_pipeline_unit.py
- [[ScanResult]] - code - gateway/security/prompt_guard.py
- [[SecurityPipeline._maybe_record_trust_violation — centralized hook that fires…]] - rationale - gateway/tests/test_pipeline_unit.py
- [[Step 1.76 PromptGuard tool-result scan must respect user_trust_level.…]] - rationale - gateway/tests/test_pipeline_unit.py
- [[TestContextGuardInPipeline]] - code - gateway/tests/test_pipeline_unit.py
- [[TestContextIntegrityInPipeline]] - code - gateway/tests/test_pipeline_unit.py
- [[TestEnvelopeSignerInPipeline]] - code - gateway/tests/test_pipeline_unit.py
- [[TestKeyLeakDetection_1]] - code - gateway/tests/test_pipeline_unit.py
- [[TestOutboundFilterResultBinding]] - code - gateway/tests/test_pipeline_unit.py
- [[TestPIIBlockModeInPipeline]] - code - gateway/tests/test_pipeline_unit.py
- [[TestPromptGuardToolResultTrustGate]] - code - gateway/tests/test_pipeline_unit.py
- [[TestTrustViolationRecording]] - code - gateway/tests/test_pipeline_unit.py
- [[UNTRUSTED source tool-result injection scan blocks as before (CVE-2026-31045).]] - rationale - gateway/tests/test_pipeline_unit.py
- [[Unit tests for pipeline components.]] - rationale - gateway/tests/test_pipeline_unit.py
- [[_FakeAttack]] - code - gateway/tests/test_pipeline_unit.py
- [[_FakeIntegrityScore]] - code - gateway/tests/test_pipeline_unit.py
- [[_make_integrity_pipeline()]] - code - gateway/tests/test_pipeline_unit.py
- [[_make_pipeline()_1]] - code - gateway/tests/test_pipeline_unit.py
- [[_make_signer_pipeline()]] - code - gateway/tests/test_pipeline_unit.py
- [[asyncio_36]] - code
- [[skip_context_guard=True must prevent ContextGuard from running — used by…]] - rationale - gateway/tests/test_pipeline_unit.py
- [[test_pipeline_unit.py]] - code - gateway/tests/test_pipeline_unit.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/asyncio
SORT file.name ASC
```

## Connections to other communities
- 23 edges to [[_COMMUNITY_PIISanitizer]]
- 10 edges to [[_COMMUNITY_AsyncMock]]
- 9 edges to [[_COMMUNITY_KeyVault]]
- 6 edges to [[_COMMUNITY_test_e2e_proxy.py]]
- 6 edges to [[_COMMUNITY_service.py]]
- 5 edges to [[_COMMUNITY_PromptGuard]]
- 5 edges to [[_COMMUNITY_TrustManager]]
- 5 edges to [[_COMMUNITY_AuditChain]]
- 4 edges to [[_COMMUNITY_TrustConfig]]
- 3 edges to [[_COMMUNITY_OutboundInfoFilter]]
- 3 edges to [[_COMMUNITY_PIIConfig]]
- 2 edges to [[_COMMUNITY_ToolResultInjectionScanner]]

## Top bridge nodes
- [[test_pipeline_unit.py]] - degree 35, connects to 11 communities
- [[dot-_pipeline_with_trust()]] - degree 9, connects to 4 communities
- [[TestContextGuardInPipeline]] - degree 15, connects to 3 communities
- [[TestPIIBlockModeInPipeline]] - degree 12, connects to 3 communities
- [[TestTrustViolationRecording]] - degree 12, connects to 3 communities
