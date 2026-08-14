---
type: community
members: 107
---

# MCP Proxy Config

**Members:** 107 nodes

## Members
- [[.__init__()_83]] - code - gateway/security/instruction_envelope.py
- [[.__init__()_88]] - code - gateway/security/key_vault.py
- [[._blocking_prompt_guard()]] - code - gateway/tests/test_pipeline_unit.py
- [[._compute_signature()]] - code - gateway/security/instruction_envelope.py
- [[._make_vault_pipeline()]] - code - gateway/tests/test_pipeline_unit.py
- [[._passthrough_pii()]] - code - gateway/tests/test_pipeline_unit.py
- [[._passthrough_pii()_1]] - code - gateway/tests/test_pipeline_unit.py
- [[._pipeline_with_trust()]] - code - gateway/tests/test_pipeline_unit.py
- [[._redacting_pii()]] - code - gateway/tests/test_pipeline_unit.py
- [[.sign()]] - code - gateway/security/instruction_envelope.py
- [[.test_blocked_request_decays_trust_score()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_blocked_request_propagates_to_cross_bot_peer()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_clean_message_passes()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_clean_request_does_not_touch_trust_score()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_clean_response_passes_unchanged()_1]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_context_guard_error_fails_closed()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_critical_injection_blocks()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_detect_api_key_patterns()]] - code - gateway/tests/test_key_vault.py
- [[.test_detect_key_in_outbound()]] - code - gateway/tests/test_key_vault.py
- [[.test_detector_failure_fails_closed_for_non_owner()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_envelope_metadata_in_audit_entry()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_full_trust_tool_result_injection_audited_not_blocked()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_generic_key_pattern_audited_but_not_blocked()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_high_injection_blocks()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_high_score_forwards_and_records()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_key_leak_increments_sanitized_stat_and_audits()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_leak_detection_logged()]] - code - gateway/tests/test_key_vault.py
- [[.test_lockdown_block_is_audited()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_lockdown_score_allows_owner()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_lockdown_score_blocks_non_owner()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_missing_trust_manager_does_not_raise()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_no_context_guard_passes_through()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_no_leak_clean_message()]] - code - gateway/tests/test_key_vault.py
- [[.test_no_outbound_filter_does_not_unbind()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_no_scorer_leaves_result_unscored()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_no_signer_leaves_envelope_empty()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_non_owner_block_does_not_emit_owner_bypass()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_non_owner_inbound_query_still_redacted()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_outbound_filter_still_escalates_fabricated_notice()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_outbound_response_is_signed_and_verifiable()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_owner_bypass_audited_at_every_guard()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_owner_bypass_is_recorded_in_audit_chain()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_owner_exempted_block_does_not_decay_trust()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_owner_inbound_query_not_pii_redacted()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_repetition_attack_does_not_block()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_scorer_error_allows_owner()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_scorer_error_fails_closed_non_owner()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_scorer_invoked_with_session_segments()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_signer_failure_never_blocks()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_skip_context_guard_bypasses_step0()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_standard_trust_tool_result_injection_is_blocked()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_stored_key_value_redacted_from_outbound()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_tool_result_uses_wrap_tool_result()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_untrusted_tool_result_injection_is_blocked()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_warn_zone_forwards()]] - code - gateway/tests/test_pipeline_unit.py
- [[.verify()]] - code - gateway/security/instruction_envelope.py
- [[.wrap_system_prompt()]] - code - gateway/security/instruction_envelope.py
- [[.wrap_tool_result()]] - code - gateway/security/instruction_envelope.py
- [[0.3 ≤ score  0.6 warns but never blocks.]] - rationale - gateway/tests/test_pipeline_unit.py
- [[A signed instruction or tool result.]] - rationale - gateway/security/instruction_envelope.py
- [[ContextGuard must run in SecurityPipeline.process_inbound() — A2.]] - rationale - gateway/tests/test_pipeline_unit.py
- [[ContextIntegrityScorer must run in process_inbound() — C21 wiring.]] - rationale - gateway/tests/test_pipeline_unit.py
- [[Convenience sign a system prompt as issuer='system'.]] - rationale - gateway/security/instruction_envelope.py
- [[Convenience sign a tool result as issuer='tooltool_name'.]] - rationale - gateway/security/instruction_envelope.py
- [[EnvelopeSigner]] - code - gateway/security/instruction_envelope.py
- [[EnvelopeSigner must attest outbound responses — C46 wiring.]] - rationale - gateway/tests/test_pipeline_unit.py
- [[FULL-trust owner response scan runs, detection audited, delivery NOT blocked.]] - rationale - gateway/tests/test_pipeline_unit.py
- [[InstructionEnvelope]] - code - gateway/security/instruction_envelope.py
- [[KeyLeakDetector]] - code - gateway/security/key_vault.py
- [[KeyLeakDetector wiring — stored credential values must never leave the gateway.]] - rationale - gateway/tests/test_pipeline_unit.py
- [[Minimal SecurityPipeline with a real PII sanitizer stub.]] - rationale - gateway/tests/test_pipeline_unit.py
- [[No trust_manager configured — the hook must no-op, not crash the         request]] - rationale - gateway/tests/test_pipeline_unit.py
- [[Non-owner query must still be PII-scrubbed (detector + threshold unchanged).]] - rationale - gateway/tests/test_pipeline_unit.py
- [[Owner messages that would trip a guard are logged but never         blocked — re]] - rationale - gateway/tests/test_pipeline_unit.py
- [[Owner query must pass through PII sanitisation unchanged; sanitiser not called.]] - rationale - gateway/tests/test_pipeline_unit.py
- [[PII sanitiser mock that simulates two entity redactions.]] - rationale - gateway/tests/test_pipeline_unit.py
- [[Pipeline with ContextGuard + ContextIntegrityScorer mocks.]] - rationale - gateway/tests/test_pipeline_unit.py
- [[Regression filter_result was possibly-unbound in process_outbound when no     o]] - rationale - gateway/tests/test_pipeline_unit.py
- [[Return True if the envelope's signature is valid.]] - rationale - gateway/security/instruction_envelope.py
- [[Return a signed envelope for content.]] - rationale - gateway/security/instruction_envelope.py
- [[STANDARD-trust source also blocked — only FULL bypasses the block.]] - rationale - gateway/tests/test_pipeline_unit.py
- [[ScanResult_1]] - code - gateway/security/prompt_guard.py
- [[SecurityPipeline._maybe_record_trust_violation — centralized hook that     fires]] - rationale - gateway/tests/test_pipeline_unit.py
- [[Signs and verifies InstructionEnvelopes.      Usage          signer = Envelope]] - rationale - gateway/security/instruction_envelope.py
- [[Step 1.76 PromptGuard tool-result scan must respect user_trust_level.      CVE-2]] - rationale - gateway/tests/test_pipeline_unit.py
- [[Step 2 PII sanitisation must be skipped for the authenticated owner.      Non-ow]] - rationale - gateway/tests/test_pipeline_unit.py
- [[TestContextGuardInPipeline]] - code - gateway/tests/test_pipeline_unit.py
- [[TestContextIntegrityInPipeline]] - code - gateway/tests/test_pipeline_unit.py
- [[TestEnvelopeSignerInPipeline]] - code - gateway/tests/test_pipeline_unit.py
- [[TestInboundPIIOwnerExemption]] - code - gateway/tests/test_pipeline_unit.py
- [[TestKeyLeakDetection]] - code - gateway/tests/test_key_vault.py
- [[TestKeyLeakDetection_1]] - code - gateway/tests/test_pipeline_unit.py
- [[TestOutboundFilterResultBinding]] - code - gateway/tests/test_pipeline_unit.py
- [[TestPromptGuardToolResultTrustGate]] - code - gateway/tests/test_pipeline_unit.py
- [[TestTrustViolationRecording]] - code - gateway/tests/test_pipeline_unit.py
- [[ThreatAction]] - code - gateway/security/prompt_guard.py
- [[UNTRUSTED source tool-result injection scan blocks as before (CVE-2026-31045).]] - rationale - gateway/tests/test_pipeline_unit.py
- [[_FakeAttack]] - code - gateway/tests/test_pipeline_unit.py
- [[_FakeIntegrityScore]] - code - gateway/tests/test_pipeline_unit.py
- [[_make_integrity_pipeline()]] - code - gateway/tests/test_pipeline_unit.py
- [[_make_pipeline()_2]] - code - gateway/tests/test_pipeline_unit.py
- [[_make_signer_pipeline()]] - code - gateway/tests/test_pipeline_unit.py
- [[instruction_envelope.py]] - code - gateway/security/instruction_envelope.py
- [[signer()]] - code - gateway/tests/test_instruction_envelope.py
- [[skip_context_guard=True must prevent ContextGuard from running — used by Telegra]] - rationale - gateway/tests/test_pipeline_unit.py
- [[test_instruction_envelope.py]] - code - gateway/tests/test_instruction_envelope.py
- [[test_pipeline_unit.py]] - code - gateway/tests/test_pipeline_unit.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/MCP_Proxy_Config
SORT file.name ASC
```

## Connections to other communities
- 59 edges to [[_COMMUNITY_SOC RBAC & Auth]]
- 40 edges to [[_COMMUNITY_Auth & Exception Types]]
- 13 edges to [[_COMMUNITY_MCP Policy Engine]]
- 12 edges to [[_COMMUNITY_Bot CVE Scorecard]]
- 12 edges to [[_COMMUNITY_Gateway Test Suite]]
- 11 edges to [[_COMMUNITY_Gateway Test Suite]]
- 11 edges to [[_COMMUNITY_Gateway Test Suite]]
- 11 edges to [[_COMMUNITY_Gateway Test Suite]]
- 8 edges to [[_COMMUNITY_Audit Export Pipeline]]
- 6 edges to [[_COMMUNITY_Gateway Test Suite]]
- 5 edges to [[_COMMUNITY_Gateway Test Suite]]
- 4 edges to [[_COMMUNITY_Slack API Proxy]]
- 2 edges to [[_COMMUNITY_Gateway Test Suite]]
- 1 edge to [[_COMMUNITY_Gateway Test Suite]]
- 1 edge to [[_COMMUNITY_Gateway Test Suite]]
- 1 edge to [[_COMMUNITY_Gateway Test Suite]]
- 1 edge to [[_COMMUNITY_Security Docs]]
- 1 edge to [[_COMMUNITY_Bot Skill Config]]
- 1 edge to [[_COMMUNITY_Planning Docs]]

## Top bridge nodes
- [[ThreatAction]] - degree 33, connects to 11 communities
- [[test_pipeline_unit.py]] - degree 31, connects to 7 communities
- [[_FakeAttack]] - degree 27, connects to 7 communities
- [[TestContextGuardInPipeline]] - degree 27, connects to 7 communities
- [[TestContextIntegrityInPipeline]] - degree 26, connects to 7 communities