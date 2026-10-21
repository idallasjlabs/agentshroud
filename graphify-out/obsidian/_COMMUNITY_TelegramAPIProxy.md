---
type: community
members: 98
---

# TelegramAPIProxy

**Members:** 98 nodes

## Members
- [[--- new instructions patterns should be stripped.]] - rationale - gateway/tests/test_prompt_guard.py
- [[dot-__init__()_133]] - code - gateway/security/context_integrity.py
- [[dot-_get_hmac_key()]] - code - gateway/security/prompt_guard.py
- [[dot-get_segment_provenance()]] - code - gateway/security/context_guard.py
- [[dot-guard()_1]] - code - gateway/tests/test_performance.py
- [[dot-guard()_2]] - code - gateway/tests/test_prompt_guard.py
- [[dot-guard()_3]] - code - gateway/tests/test_prompt_guard.py
- [[dot-guard()_4]] - code - gateway/tests/test_security_audit.py
- [[dot-pg()]] - code - gateway/tests/test_prompt_guard.py
- [[dot-pg()_1]] - code - gateway/tests/test_prompt_guard.py
- [[dot-reanchor_delimiters()]] - code - gateway/security/prompt_guard.py
- [[dot-record_segment()]] - code - gateway/security/context_guard.py
- [[dot-register_system_prompt()]] - code - gateway/security/prompt_guard.py
- [[dot-score_context()]] - code - gateway/security/context_integrity.py
- [[dot-tag_segment()]] - code - gateway/security/context_guard.py
- [[dot-test_below_alert_threshold_logs_warning()]] - code - gateway/tests/test_context_integrity.py
- [[dot-test_benign_tool_result_passes()]] - code - gateway/tests/test_prompt_guard.py
- [[dot-test_direct_injection_in_tool_result_blocked()]] - code - gateway/tests/test_prompt_guard.py
- [[dot-test_duplicate_hashes_detected()]] - code - gateway/tests/test_context_integrity.py
- [[dot-test_empty_context_scores_clean()]] - code - gateway/tests/test_context_integrity.py
- [[dot-test_empty_prompt()]] - code - gateway/tests/test_prompt_guard.py
- [[dot-test_empty_tool_result_passes()]] - code - gateway/tests/test_prompt_guard.py
- [[dot-test_explicit_key_used()]] - code - gateway/tests/test_prompt_guard.py
- [[dot-test_injected_untrusted_segment_lowers_score()]] - code - gateway/tests/test_context_integrity.py
- [[dot-test_lower_threshold_than_direct_scan()]] - code - gateway/tests/test_prompt_guard.py
- [[dot-test_preserves_legitimate_markdown()]] - code - gateway/tests/test_prompt_guard.py
- [[dot-test_pristine_context_scores_high()]] - code - gateway/tests/test_context_integrity.py
- [[dot-test_prompt_guard_instantiates()]] - code - gateway/tests/test_all_modules_enforce.py
- [[dot-test_prompt_guard_large_input()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_register_and_verify()]] - code - gateway/tests/test_prompt_guard.py
- [[dot-test_role_override_in_tool_result_blocked()]] - code - gateway/tests/test_prompt_guard.py
- [[dot-test_strips_fake_system_tags()]] - code - gateway/tests/test_prompt_guard.py
- [[dot-test_strips_separator_overrides()]] - code - gateway/tests/test_prompt_guard.py
- [[dot-test_tamper_detected()]] - code - gateway/tests/test_prompt_guard.py
- [[dot-test_tampered_system_prompt_lowers_score()]] - code - gateway/tests/test_context_integrity.py
- [[dot-test_write_baseline_json()]] - code - gateway/tests/test_performance.py
- [[dot-verify_system_prompt()]] - code - gateway/security/prompt_guard.py
- [[system style fake tags should be stripped.]] - rationale - gateway/tests/test_prompt_guard.py
- [[A well-formed context with valid HMAC should score close to 1.0.]] - rationale - gateway/tests/test_context_integrity.py
- [[Any_48]] - code - gateway/security/context_integrity.py
- [[CVE-2026-31045 — indirect prompt injection via tool results]] - concept - gateway/tests/test_prompt_guard.py
- [[Compute a 0.0–1.0 integrity score for the given context segments.          Args]] - rationale - gateway/security/context_integrity.py
- [[Compute and return an HMAC-SHA256 fingerprint for the system prompt.]] - rationale - gateway/security/prompt_guard.py
- [[ContextIntegrityScorer]] - code - gateway/security/context_integrity.py
- [[ContextSegment]] - code - gateway/security/context_guard.py
- [[Create a PromptGuard instance for testing]] - rationale - gateway/tests/test_prompt_guard.py
- [[Create a provenance record for a context segment.]] - rationale - gateway/security/context_guard.py
- [[Detect and block prompt injection attempts.]] - rationale - gateway/security/prompt_guard.py
- [[Double-base64 encoded lower-ranked injection is caught (was top-5 only).]] - rationale - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[Duplicate content hashes reduce score.]] - rationale - gateway/tests/test_context_integrity.py
- [[Empty prompt should still register and verify cleanly.]] - rationale - gateway/tests/test_prompt_guard.py
- [[Empty segment list should not penalize the score.]] - rationale - gateway/tests/test_context_integrity.py
- [[Explicit ignore-instructions payload embedded in a tool result.]] - rationale - gateway/tests/test_prompt_guard.py
- [[Explicit key parameter should override session key.]] - rationale - gateway/tests/test_prompt_guard.py
- [[HMAC-SHA256 fingerprint for a registered system prompt.]] - rationale - gateway/security/prompt_guard.py
- [[IntegrityScore]] - code - gateway/security/context_integrity.py
- [[Large inputs shouldn't crash prompt guard.]] - rationale - gateway/tests/test_security_audit.py
- [[Mismatched HMAC should reduce score by at least 0.15.]] - rationale - gateway/tests/test_context_integrity.py
- [[Normal markdown headers ( Title) should not be stripped.]] - rationale - gateway/tests/test_prompt_guard.py
- [[PromptGuard]] - code - gateway/security/prompt_guard.py
- [[Return HMAC key env var preferred, session-scoped random fallback.]] - rationale - gateway/security/prompt_guard.py
- [[Return True if prompt_text matches the stored HMAC fingerprint.]] - rationale - gateway/security/prompt_guard.py
- [[Return ordered list of provenance records for the session.]] - rationale - gateway/security/context_guard.py
- [[Rolling context integrity score for a session.]] - rationale - gateway/security/context_integrity.py
- [[Run standard benchmarks and write results to .benchmarksbaseline-v1.0.0.json.]] - rationale - gateway/tests/test_performance.py
- [[Score below 0.6 should produce a warning log.]] - rationale - gateway/tests/test_context_integrity.py
- [[Scores the integrity of a session's context.      Usage          scorer = Cont]] - rationale - gateway/security/context_integrity.py
- [[Strip injected fake delimiters and return sanitized message.          Called whe]] - rationale - gateway/security/prompt_guard.py
- [[SystemPromptFingerprint]] - code - gateway/security/prompt_guard.py
- [[Tag a segment and append it to the session's provenance log.]] - rationale - gateway/security/context_guard.py
- [[Tagged provenance record for a context segment.]] - rationale - gateway/security/context_guard.py
- [[Test PromptGuard initialization]] - rationale - gateway/tests/test_prompt_guard.py
- [[Test that normal messages pass through]] - rationale - gateway/tests/test_prompt_guard.py
- [[TestContextIntegrityScorer]] - code - gateway/tests/test_context_integrity.py
- [[TestReanchorDelimiters]] - code - gateway/tests/test_prompt_guard.py
- [[TestSystemPromptHMAC]] - code - gateway/tests/test_prompt_guard.py
- [[TestToolResultScan]] - code - gateway/tests/test_prompt_guard.py
- [[Tests for indirect prompt injection detection in tool results.]] - rationale - gateway/tests/test_prompt_guard.py
- [[ThreatAction]] - code - gateway/security/prompt_guard.py
- [[Tool result scan blocks at score ≥ 0.6 vs direct scan threshold of 0.8.]] - rationale - gateway/tests/test_prompt_guard.py
- [[Untrusted segment injected after system segment reduces score.]] - rationale - gateway/tests/test_context_integrity.py
- [[Verifying a tampered prompt should return False.]] - rationale - gateway/tests/test_prompt_guard.py
- [[_make_segment()]] - code - gateway/tests/test_context_integrity.py
- [[`_check_encoded_content` now matches rules beyond the old top-5 slice.      Fail]] - rationale - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[canary_pipeline()]] - code - gateway/tests/test_canary.py
- [[context_integrity.py]] - code - gateway/security/context_integrity.py
- [[guard()_3]] - code - gateway/tests/test_context_integrity.py
- [[prompt_guard()]] - code - gateway/tests/test_e2e_proxy.py
- [[prompt_guard()_1]] - code - gateway/tests/test_prompt_guard.py
- [[prompt_guard()_2]] - code - gateway/tests/test_security_integration.py
- [[register_system_prompt + verify_system_prompt should succeed.]] - rationale - gateway/tests/test_prompt_guard.py
- [[scorer()]] - code - gateway/tests/test_context_integrity.py
- [[test_benign_message()]] - code - gateway/tests/test_prompt_guard.py
- [[test_context_integrity.py]] - code - gateway/tests/test_context_integrity.py
- [[test_prompt_guard.py]] - code - gateway/tests/test_prompt_guard.py
- [[test_prompt_guard_double_encoded_uses_full_ruleset()]] - code - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[test_prompt_guard_encoded_check_uses_full_ruleset()]] - code - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[test_prompt_guard_init()]] - code - gateway/tests/test_prompt_guard.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TelegramAPIProxy
SORT file.name ASC
```

## Connections to other communities
- 27 edges to [[_COMMUNITY_ApprovalQueueConfig]]
- 18 edges to [[_COMMUNITY_EgressFilterConfig]]
- 17 edges to [[_COMMUNITY_TelegramAPIProxy (2)]]
- 12 edges to [[_COMMUNITY_test_soc_egress_endpoints.py]]
- 11 edges to [[_COMMUNITY_MiddlewareManager]]
- 8 edges to [[_COMMUNITY__wrap_response() (2)_1]]
- 7 edges to [[_COMMUNITY__wrap_response()]]
- 6 edges to [[_COMMUNITY_AgentTarget]]
- 5 edges to [[_COMMUNITY_Google Services Setup - Calendar, Contacts, Keep]]
- 5 edges to [[_COMMUNITY_ApprovalQueueConfig (4)]]
- 5 edges to [[_COMMUNITY_ApprovalQueueConfig (2)_1]]
- 4 edges to [[_COMMUNITY_socrouter.py]]
- 4 edges to [[_COMMUNITY__t]]
- 4 edges to [[_COMMUNITY_PortManager]]
- 3 edges to [[_COMMUNITY_MiddlewareManager (4)]]
- 3 edges to [[_COMMUNITY_A2APolicyEngine (2)]]
- 3 edges to [[_COMMUNITY_TelegramAPIProxy (3)_1]]
- 3 edges to [[_COMMUNITY_DelegationManager]]
- 2 edges to [[_COMMUNITY_test_agent_cve_registry.py]]
- 2 edges to [[_COMMUNITY_dot-_make_proxy()]]
- 2 edges to [[_COMMUNITY_AgentTarget (2)_1]]
- 2 edges to [[_COMMUNITY_EgressFilterConfig (2)]]
- 2 edges to [[_COMMUNITY__wrap_response() (5)]]
- 2 edges to [[_COMMUNITY_MCPPermissionManager]]
- 2 edges to [[_COMMUNITY__wrap_response() (3)_1]]
- 2 edges to [[_COMMUNITY_test_a2a_policy.py]]
- 2 edges to [[_COMMUNITY_socrouter.py (2)]]
- 2 edges to [[_COMMUNITY_test_soc_router_coverage.py]]
- 1 edge to [[_COMMUNITY_agentshroud-blueteamSKILL]]
- 1 edge to [[_COMMUNITY_KillSwitchMonitor]]
- 1 edge to [[_COMMUNITY_test_collaborator_tracker.py]]
- 1 edge to [[_COMMUNITY__make_proxy()]]
- 1 edge to [[_COMMUNITY_Common Queries]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy (2)_1]]
- 1 edge to [[_COMMUNITY__wrap_response() (4)]]
- 1 edge to [[_COMMUNITY_test_playback_state.c]]
- 1 edge to [[_COMMUNITY_test_agent_cve_registry.py (2)]]
- 1 edge to [[_COMMUNITY_ApprovalQueueConfig (3)_1]]

## Top bridge nodes
- [[PromptGuard]] - degree 148, connects to 34 communities
- [[ThreatAction]] - degree 33, connects to 14 communities
- [[test_prompt_guard.py]] - degree 14, connects to 4 communities
- [[canary_pipeline()]] - degree 6, connects to 4 communities
- [[SystemPromptFingerprint]] - degree 13, connects to 2 communities
