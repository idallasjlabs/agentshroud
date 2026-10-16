---
type: community
cohesion: 0.04
members: 77
---

# OutboundInfoFilter

**Cohesion:** 0.04 - loosely connected
**Members:** 77 nodes

## Members
- [[dot-__init__()_11]] - code - gateway/security/outbound_filter.py
- [[dot-_blocking_prompt_guard()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-_check_encoded_content()]] - code - gateway/security/prompt_guard.py
- [[dot-_check_unicode_tricks()]] - code - gateway/security/prompt_guard.py
- [[dot-_classify_response_risk()]] - code - gateway/security/outbound_filter.py
- [[dot-_compile_patterns()_1]] - code - gateway/security/outbound_filter.py
- [[dot-_is_allowed_for_trust()]] - code - gateway/security/outbound_filter.py
- [[dot-_passthrough_pii()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-_redacting_pii()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-filter_response()]] - code - gateway/security/outbound_filter.py
- [[dot-get_stats()_3]] - code - gateway/security/outbound_filter.py
- [[dot-scan()_1]] - code - gateway/security/prompt_guard.py
- [[dot-scan_tool_result()]] - code - gateway/security/prompt_guard.py
- [[dot-setup_method()_1]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_full_trust_tool_result_injection_audited_not_blocked()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_high_score_forwards_and_records()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_lockdown_block_is_audited()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_lockdown_score_allows_owner()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_lockdown_score_blocks_non_owner()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_no_outbound_filter_does_not_unbind()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_no_scorer_leaves_result_unscored()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_non_owner_inbound_query_still_redacted()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_outbound_filter_still_escalates_fabricated_notice()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_owner_inbound_query_not_pii_redacted()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_scorer_error_allows_owner()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_scorer_error_fails_closed_non_owner()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_scorer_invoked_with_session_segments()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_standard_trust_tool_result_injection_is_blocked()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_untrusted_tool_result_injection_is_blocked()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_warn_zone_forwards()]] - code - gateway/tests/test_pipeline_unit.py
- [[0.3 ≤ score  0.6 warns but never blocks.]] - rationale - gateway/tests/test_pipeline_unit.py
- [[A single match found by the outbound filter.]] - rationale - gateway/security/outbound_filter.py
- [[Any_3]] - code - gateway/security/outbound_filter.py
- [[Check for suspicious base64 content that decodes to injection attempts.]] - rationale - gateway/security/prompt_guard.py
- [[Check if a disclosure category is permitted for the user's trust level.]] - rationale - gateway/security/outbound_filter.py
- [[Classify the risk level of a response based on info disclosure density.]] - rationale - gateway/security/outbound_filter.py
- [[Compile all filter patterns into regex objects.]] - rationale - gateway/security/outbound_filter.py
- [[ContextIntegrityScorer must run in process_inbound() — C21 wiring.]] - rationale - gateway/tests/test_pipeline_unit.py
- [[Detect potential base64-encoded payloads in text.     Returns list of decoded st]] - rationale - gateway/security/input_normalizer.py
- [[Detect unicode obfuscation tricks.]] - rationale - gateway/security/prompt_guard.py
- [[FR4 Data Confidentiality]] - concept - docs/compliance/iec-62443-matrix.md
- [[FULL-trust owner response scan runs, detection audited, delivery NOT blocked.]] - rationale - gateway/tests/test_pipeline_unit.py
- [[Filter agent response for sensitive information disclosure.          Args]] - rationale - gateway/security/outbound_filter.py
- [[FilterMatch]] - code - gateway/security/outbound_filter.py
- [[FilterResult]] - code - gateway/security/outbound_filter.py
- [[Get filter statistics.]] - rationale - gateway/security/outbound_filter.py
- [[Initialize the outbound information filter.          Args             config C]] - rationale - gateway/security/outbound_filter.py
- [[Main outbound information filtering engine.      Uses compiled regex patterns to]] - rationale - gateway/security/outbound_filter.py
- [[Non-owner query must still be PII-scrubbed (detector + threshold unchanged).]] - rationale - gateway/tests/test_pipeline_unit.py
- [[Outbound Information Filter Tests]] - code - gateway/tests/test_outbound_filter.py
- [[OutboundInfoFilter]] - code - gateway/security/outbound_filter.py
- [[Owner query must pass through PII sanitisation unchanged; sanitiser not called.]] - rationale - gateway/tests/test_pipeline_unit.py
- [[PII sanitiser mock that simulates two entity redactions.]] - rationale - gateway/tests/test_pipeline_unit.py
- [[Pipeline with ContextGuard + ContextIntegrityScorer mocks.]] - rationale - gateway/tests/test_pipeline_unit.py
- [[Prompt Guard Module Badge Icon]] - image - branding/icons/modules/prompt-guard-256x256.png
- [[Regression filter_result was possibly-unbound in process_outbound when no     o]] - rationale - gateway/tests/test_pipeline_unit.py
- [[Result of filtering agent response content.]] - rationale - gateway/security/outbound_filter.py
- [[STANDARD-trust source also blocked — only FULL bypasses the block.]] - rationale - gateway/tests/test_pipeline_unit.py
- [[Scan input text for prompt injection patterns.          Args             text]] - rationale - gateway/security/prompt_guard.py
- [[Scan tool result content for indirect prompt injection.          Tool results (w]] - rationale - gateway/security/prompt_guard.py
- [[ScanResult_1]] - code - gateway/security/prompt_guard.py
- [[Step 1.76 PromptGuard tool-result scan must respect user_trust_level.      CVE-2]] - rationale - gateway/tests/test_pipeline_unit.py
- [[Step 2 PII sanitisation must be skipped for the authenticated owner.      Non-ow]] - rationale - gateway/tests/test_pipeline_unit.py
- [[TestContextIntegrityInPipeline]] - code - gateway/tests/test_pipeline_unit.py
- [[TestInboundPIIOwnerExemption]] - code - gateway/tests/test_pipeline_unit.py
- [[TestOutboundFilterResultBinding]] - code - gateway/tests/test_pipeline_unit.py
- [[TestPromptGuardToolResultTrustGate]] - code - gateway/tests/test_pipeline_unit.py
- [[ThreatAction]] - code - gateway/security/prompt_guard.py
- [[UNTRUSTED source tool-result injection scan blocks as before (CVE-2026-31045).]] - rationale - gateway/tests/test_pipeline_unit.py
- [[_FakeIntegrityScore]] - code - gateway/tests/test_pipeline_unit.py
- [[_make_integrity_pipeline()]] - code - gateway/tests/test_pipeline_unit.py
- [[detect_base64_payloads()]] - code - gateway/security/input_normalizer.py
- [[outbound_filter.py]] - code - gateway/security/outbound_filter.py
- [[pipeline.py]] - code - gateway/proxy/pipeline.py
- [[prompt_guard.py]] - code - gateway/security/prompt_guard.py
- [[test_multilingual_injection.py]] - code - gateway/tests/test_multilingual_injection.py
- [[test_pipeline_unit.py]] - code - gateway/tests/test_pipeline_unit.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/OutboundInfoFilter
SORT file.name ASC
```

## Connections to other communities
- 31 edges to [[_COMMUNITY_PIIConfig]]
- 25 edges to [[_COMMUNITY_KeyVault]]
- 17 edges to [[_COMMUNITY_EnvelopeSigner]]
- 16 edges to [[_COMMUNITY_AuditChain]]
- 15 edges to [[_COMMUNITY__FakeAttack]]
- 13 edges to [[_COMMUNITY_PipelineAction]]
- 12 edges to [[_COMMUNITY_AgentRegistry]]
- 9 edges to [[_COMMUNITY_TestFabricatedSecurityNotice]]
- 7 edges to [[_COMMUNITY_TrustConfig]]
- 7 edges to [[_COMMUNITY_CrossBotTrustLedger]]
- 7 edges to [[_COMMUNITY_InjectionAction]]
- 6 edges to [[_COMMUNITY_Enum]]
- 6 edges to [[_COMMUNITY_TestOutboundInfoFilter]]
- 5 edges to [[_COMMUNITY_lifespan.py]]
- 4 edges to [[_COMMUNITY_AsyncMock]]
- 3 edges to [[_COMMUNITY_agentshroud-blueteamSKILL]]
- 2 edges to [[_COMMUNITY_DataLedger]]
- 2 edges to [[_COMMUNITY_TelegramAPIProxy_1]]
- 2 edges to [[_COMMUNITY_IEC 62443 Compliance Matrix — AgentShroud]]
- 1 edge to [[_COMMUNITY_RBACConfig]]
- 1 edge to [[_COMMUNITY_dot-analyze_message]]
- 1 edge to [[_COMMUNITY_MiddlewareManager]]
- 1 edge to [[_COMMUNITY_ContextSegment]]
- 1 edge to [[_COMMUNITY_FR3 System Integrity]]
- 1 edge to [[_COMMUNITY_EgressFilterConfig]]
- 1 edge to [[_COMMUNITY_First Time Setup]]
- 1 edge to [[_COMMUNITY_AGENTSHROUD_MODE]]
- 1 edge to [[_COMMUNITY_TestNewPatternsV080]]
- 1 edge to [[_COMMUNITY_EgressFilter]]
- 1 edge to [[_COMMUNITY_TestEgressSSRF]]
- 1 edge to [[_COMMUNITY_TestMultilingualInjection]]
- 1 edge to [[_COMMUNITY_ToolResultSanitizer]]
- 1 edge to [[_COMMUNITY_diagramsREADME]]
- 1 edge to [[_COMMUNITY_PHASE_3A_3B_IMPLEMENTATION]]
- 1 edge to [[_COMMUNITY_AgentShroud macOS App Icon (1024x1024, Rounded Squircle)]]

## Top bridge nodes
- [[prompt_guard.py]] - degree 17, connects to 11 communities
- [[ThreatAction]] - degree 33, connects to 10 communities
- [[pipeline.py]] - degree 14, connects to 10 communities
- [[test_pipeline_unit.py]] - degree 31, connects to 9 communities
- [[OutboundInfoFilter]] - degree 38, connects to 8 communities
