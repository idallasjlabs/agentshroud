---
type: community
members: 58
---

# Community 24

**Members:** 58 nodes

## Members
- [[._blocking_prompt_guard()]] - code - gateway/tests/test_pipeline_unit.py
- [[._make_vault_pipeline()]] - code - gateway/tests/test_pipeline_unit.py
- [[._passthrough_pii()_1]] - code - gateway/tests/test_pipeline_unit.py
- [[._pipeline()]] - code - gateway/tests/test_pipeline_unit.py
- [[._redacting_pii()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_append_owner_bypass_persists_high_severity()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_block_clean_message_forwards()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_clean_response_passes_unchanged()_1]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_detector_failure_fails_closed_for_non_owner()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_envelope_metadata_in_audit_entry()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_full_trust_tool_result_injection_audited_not_blocked()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_generic_key_pattern_audited_but_not_blocked()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_inbound_block()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_inbound_redact_unchanged()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_key_leak_increments_sanitized_stat_and_audits()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_no_signer_leaves_envelope_empty()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_non_owner_inbound_query_still_redacted()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_outbound_block()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_outbound_redact_unchanged()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_outbound_response_is_signed_and_verifiable()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_owner_inbound_query_not_pii_redacted()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_persisted_event_records_true_previous_hash()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_signer_failure_never_blocks()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_standard_trust_tool_result_injection_is_blocked()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_stored_key_value_redacted_from_outbound()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_tool_result_uses_wrap_tool_result()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_untrusted_tool_result_injection_is_blocked()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_unwrapped_chain_must_anchor_at_genesis()]] - code - gateway/tests/test_pipeline_unit.py
- [[A self-consistent window on a forged anchor must fail when the         chain nev]] - rationale - gateway/tests/test_pipeline_unit.py
- [[EnvelopeSigner must attest outbound responses — C46 wiring.]] - rationale - gateway/tests/test_pipeline_unit.py
- [[FULL-trust owner response scan runs, detection audited, delivery NOT blocked.]] - rationale - gateway/tests/test_pipeline_unit.py
- [[InjectionAction]] - code - gateway/security/tool_result_injection.py
- [[KeyLeakDetector wiring — stored credential values must never leave the gateway.]] - rationale - gateway/tests/test_pipeline_unit.py
- [[KeyVaultConfig]] - code - gateway/security/key_vault.py
- [[Non-owner query must still be PII-scrubbed (detector + threshold unchanged).]] - rationale - gateway/tests/test_pipeline_unit.py
- [[Owner query must pass through PII sanitisation unchanged; sanitiser not called.]] - rationale - gateway/tests/test_pipeline_unit.py
- [[PII sanitiser mock that simulates two entity redactions.]] - rationale - gateway/tests/test_pipeline_unit.py
- [[Regression filter_result was possibly-unbound in process_outbound when no     o]] - rationale - gateway/tests/test_pipeline_unit.py
- [[SCRUM-202 enforcement_action=block must actually block in the pipeline.]] - rationale - gateway/tests/test_pipeline_unit.py
- [[STANDARD-trust source also blocked — only FULL bypasses the block.]] - rationale - gateway/tests/test_pipeline_unit.py
- [[ScanResult_1]] - code - gateway/security/prompt_guard.py
- [[Step 1.76 PromptGuard tool-result scan must respect user_trust_level.      CVE-2]] - rationale - gateway/tests/test_pipeline_unit.py
- [[Step 2 PII sanitisation must be skipped for the authenticated owner.      Non-ow]] - rationale - gateway/tests/test_pipeline_unit.py
- [[TestAuditChainBounded]] - code - gateway/tests/test_pipeline_unit.py
- [[TestEnvelopeSignerInPipeline]] - code - gateway/tests/test_pipeline_unit.py
- [[TestInboundPIIOwnerExemption]] - code - gateway/tests/test_pipeline_unit.py
- [[TestKeyLeakDetection_1]] - code - gateway/tests/test_pipeline_unit.py
- [[TestOutboundFilterResultBinding]] - code - gateway/tests/test_pipeline_unit.py
- [[TestPIIBlockModeInPipeline]] - code - gateway/tests/test_pipeline_unit.py
- [[TestPromptGuardToolResultTrustGate]] - code - gateway/tests/test_pipeline_unit.py
- [[The fire-and-forget SQLite log must record the entry's actual         previous_h]] - rationale - gateway/tests/test_pipeline_unit.py
- [[The in-memory window must be bounded; full history lives in SQLite.]] - rationale - gateway/tests/test_pipeline_unit.py
- [[ThreatAction]] - code - gateway/security/prompt_guard.py
- [[UNTRUSTED source tool-result injection scan blocks as before (CVE-2026-31045).]] - rationale - gateway/tests/test_pipeline_unit.py
- [[_FakeIntegrityScore]] - code - gateway/tests/test_pipeline_unit.py
- [[_make_signer_pipeline()]] - code - gateway/tests/test_pipeline_unit.py
- [[append_owner_bypass writes to the hash chain AND persists a HIGH         'owner_]] - rationale - gateway/tests/test_pipeline_unit.py
- [[test_pipeline_unit.py]] - code - gateway/tests/test_pipeline_unit.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_24
SORT file.name ASC
```

## Connections to other communities
- 60 edges to [[_COMMUNITY_Community 84]]
- 33 edges to [[_COMMUNITY_Community 684]]
- 23 edges to [[_COMMUNITY_Community 1566]]
- 20 edges to [[_COMMUNITY_Community 80]]
- 18 edges to [[_COMMUNITY_Community 88]]
- 18 edges to [[_COMMUNITY_Community 531]]
- 11 edges to [[_COMMUNITY_Community 52]]
- 10 edges to [[_COMMUNITY_Community 98]]
- 9 edges to [[_COMMUNITY_Community 0]]
- 9 edges to [[_COMMUNITY_Community 154]]
- 8 edges to [[_COMMUNITY_Community 22]]
- 7 edges to [[_COMMUNITY_Community 1352]]
- 6 edges to [[_COMMUNITY_Community 37]]
- 5 edges to [[_COMMUNITY_Community 63]]
- 4 edges to [[_COMMUNITY_Community 8]]
- 2 edges to [[_COMMUNITY_Community 68]]
- 2 edges to [[_COMMUNITY_Community 151]]
- 1 edge to [[_COMMUNITY_Community 557]]
- 1 edge to [[_COMMUNITY_Community 394]]
- 1 edge to [[_COMMUNITY_Community 121]]
- 1 edge to [[_COMMUNITY_Community 140]]
- 1 edge to [[_COMMUNITY_Community 304]]
- 1 edge to [[_COMMUNITY_Community 1119]]
- 1 edge to [[_COMMUNITY_Community 1284]]

## Top bridge nodes
- [[KeyVaultConfig]] - degree 43, connects to 10 communities
- [[test_pipeline_unit.py]] - degree 34, connects to 9 communities
- [[InjectionAction]] - degree 35, connects to 8 communities
- [[ThreatAction]] - degree 34, connects to 8 communities
- [[TestKeyLeakDetection_1]] - degree 26, connects to 7 communities