---
type: community
cohesion: 0.02
members: 126
---

# ServiceManager

**Cohesion:** 0.02 - loosely connected
**Members:** 126 nodes

## Members
- [[--- new instructions patterns should be stripped.]] - rationale - gateway/tests/test_prompt_guard.py
- [[.__init__()_66]] - code - gateway/security/context_integrity.py
- [[._check_encoded_content()]] - code - gateway/security/prompt_guard.py
- [[._check_unicode_tricks()]] - code - gateway/security/prompt_guard.py
- [[._get_hmac_key()]] - code - gateway/security/prompt_guard.py
- [[.get_segment_provenance()]] - code - gateway/security/context_guard.py
- [[.guard()_2]] - code - gateway/tests/test_performance.py
- [[.guard()_4]] - code - gateway/tests/test_prompt_guard.py
- [[.guard()_3]] - code - gateway/tests/test_prompt_guard.py
- [[.guard()_5]] - code - gateway/tests/test_security_audit.py
- [[.pg()_1]] - code - gateway/tests/test_prompt_guard.py
- [[.pipeline()_1]] - code - gateway/tests/test_performance.py
- [[.reanchor_delimiters()]] - code - gateway/security/prompt_guard.py
- [[.record_segment()]] - code - gateway/security/context_guard.py
- [[.register_system_prompt()]] - code - gateway/security/prompt_guard.py
- [[.scan()_4]] - code - gateway/security/prompt_guard.py
- [[.scan_tool_result()_2]] - code - gateway/security/prompt_guard.py
- [[.score_context()]] - code - gateway/security/context_integrity.py
- [[.tag_segment()]] - code - gateway/security/context_guard.py
- [[.test_10000_lookups_under_1s()]] - code - gateway/tests/test_performance.py
- [[.test_1000_entries_under_5s()]] - code - gateway/tests/test_performance.py
- [[.test_1000_messages_under_5s()]] - code - gateway/tests/test_performance.py
- [[.test_below_alert_threshold_logs_warning()]] - code - gateway/tests/test_context_integrity.py
- [[.test_benign_tool_result_passes()]] - code - gateway/tests/test_prompt_guard.py
- [[.test_detection_accuracy_at_scale()]] - code - gateway/tests/test_performance.py
- [[.test_direct_injection_in_tool_result_blocked()]] - code - gateway/tests/test_prompt_guard.py
- [[.test_duplicate_hashes_detected()]] - code - gateway/tests/test_context_integrity.py
- [[.test_empty_context_scores_clean()]] - code - gateway/tests/test_context_integrity.py
- [[.test_empty_prompt()]] - code - gateway/tests/test_prompt_guard.py
- [[.test_empty_tool_result_passes()]] - code - gateway/tests/test_prompt_guard.py
- [[.test_explicit_key_used()]] - code - gateway/tests/test_prompt_guard.py
- [[.test_injected_untrusted_segment_lowers_score()]] - code - gateway/tests/test_context_integrity.py
- [[.test_lower_threshold_than_direct_scan()]] - code - gateway/tests/test_prompt_guard.py
- [[.test_preserves_legitimate_markdown()]] - code - gateway/tests/test_prompt_guard.py
- [[.test_pristine_context_scores_high()]] - code - gateway/tests/test_context_integrity.py
- [[.test_prompt_guard_instantiates()]] - code - gateway/tests/test_all_modules_enforce.py
- [[.test_prompt_guard_large_input()]] - code - gateway/tests/test_security_audit.py
- [[.test_query_after_1000_entries()]] - code - gateway/tests/test_performance.py
- [[.test_register_and_verify()]] - code - gateway/tests/test_prompt_guard.py
- [[.test_role_override_in_tool_result_blocked()]] - code - gateway/tests/test_prompt_guard.py
- [[.test_single_message_pipeline_under_100ms()]] - code - gateway/tests/test_performance.py
- [[.test_strips_fake_system_tags()]] - code - gateway/tests/test_prompt_guard.py
- [[.test_strips_separator_overrides()]] - code - gateway/tests/test_prompt_guard.py
- [[.test_tamper_detected()]] - code - gateway/tests/test_prompt_guard.py
- [[.test_tampered_system_prompt_lowers_score()]] - code - gateway/tests/test_context_integrity.py
- [[.test_trust_update_performance()]] - code - gateway/tests/test_performance.py
- [[.test_write_baseline_json()]] - code - gateway/tests/test_performance.py
- [[.verify_system_prompt()]] - code - gateway/security/prompt_guard.py
- [[1000 trust updates (mix of successfailure).]] - rationale - gateway/tests/test_performance.py
- [[10000 trust lookups in under 1 second.]] - rationale - gateway/tests/test_performance.py
- [[system style fake tags should be stripped.]] - rationale - gateway/tests/test_prompt_guard.py
- [[A well-formed context with valid HMAC should score close to 1.0.]] - rationale - gateway/tests/test_context_integrity.py
- [[Any_36]] - code - gateway/security/context_integrity.py
- [[Audit chain 1000 entries in  5s.]] - rationale - gateway/tests/test_performance.py
- [[CVE-2026-31045 — indirect prompt injection via tool results]] - concept - gateway/tests/test_prompt_guard.py
- [[Check for suspicious base64 content that decodes to injection attempts.]] - rationale - gateway/security/prompt_guard.py
- [[Collect and write benchmark baselines to .benchmarksbaseline-v1.0.0.json.]] - rationale - gateway/tests/test_performance.py
- [[Compute a 0.0–1.0 integrity score for the given context segments.          Args]] - rationale - gateway/security/context_integrity.py
- [[Compute and return an HMAC-SHA256 fingerprint for the system prompt.]] - rationale - gateway/security/prompt_guard.py
- [[ContextIntegrityScorer]] - code - gateway/security/context_integrity.py
- [[ContextSegment]] - code - gateway/security/context_guard.py
- [[Create a PromptGuard instance for testing]] - rationale - gateway/tests/test_prompt_guard.py
- [[Create a provenance record for a context segment.]] - rationale - gateway/security/context_guard.py
- [[Detect and block prompt injection attempts.]] - rationale - gateway/security/prompt_guard.py
- [[Detect potential base64-encoded payloads in text.     Returns list of decoded st]] - rationale - gateway/security/input_normalizer.py
- [[Detect unicode obfuscation tricks.]] - rationale - gateway/security/prompt_guard.py
- [[Duplicate content hashes reduce score.]] - rationale - gateway/tests/test_context_integrity.py
- [[Empty prompt should still register and verify cleanly.]] - rationale - gateway/tests/test_prompt_guard.py
- [[Empty segment list should not penalize the score.]] - rationale - gateway/tests/test_context_integrity.py
- [[End-to-end pipeline latency for a single message.]] - rationale - gateway/tests/test_performance.py
- [[Explicit ignore-instructions payload embedded in a tool result.]] - rationale - gateway/tests/test_prompt_guard.py
- [[Explicit key parameter should override session key.]] - rationale - gateway/tests/test_prompt_guard.py
- [[HMAC-SHA256 fingerprint for a registered system prompt.]] - rationale - gateway/security/prompt_guard.py
- [[Injection attempts should be detected even under load.]] - rationale - gateway/tests/test_performance.py
- [[IntegrityScore]] - code - gateway/security/context_integrity.py
- [[Large inputs shouldn't crash prompt guard.]] - rationale - gateway/tests/test_security_audit.py
- [[Mismatched HMAC should reduce score by at least 0.15.]] - rationale - gateway/tests/test_context_integrity.py
- [[Normal markdown headers ( Title) should not be stripped.]] - rationale - gateway/tests/test_prompt_guard.py
- [[Prompt guard 1000 messages in  5s.]] - rationale - gateway/tests/test_performance.py
- [[PromptGuard]] - code - gateway/security/prompt_guard.py
- [[Query performance after 1000 entries.]] - rationale - gateway/tests/test_performance.py
- [[Return HMAC key env var preferred, session-scoped random fallback.]] - rationale - gateway/security/prompt_guard.py
- [[Return True if prompt_text matches the stored HMAC fingerprint.]] - rationale - gateway/security/prompt_guard.py
- [[Return ordered list of provenance records for the session.]] - rationale - gateway/security/context_guard.py
- [[Rolling context integrity score for a session.]] - rationale - gateway/security/context_integrity.py
- [[Run standard benchmarks and write results to .benchmarksbaseline-v1.0.0.json.]] - rationale - gateway/tests/test_performance.py
- [[Scan 1000 messages in under 5 seconds.]] - rationale - gateway/tests/test_performance.py
- [[Scan input text for prompt injection patterns.          Args             text]] - rationale - gateway/security/prompt_guard.py
- [[Scan tool result content for indirect prompt injection.          Tool results (w]] - rationale - gateway/security/prompt_guard.py
- [[Score below 0.6 should produce a warning log.]] - rationale - gateway/tests/test_context_integrity.py
- [[Scores the integrity of a session's context.      Usage          scorer = Cont]] - rationale - gateway/security/context_integrity.py
- [[Single message through full pipeline in under 100ms.]] - rationale - gateway/tests/test_performance.py
- [[Strip injected fake delimiters and return sanitized message.          Called whe]] - rationale - gateway/security/prompt_guard.py
- [[SystemPromptFingerprint]] - code - gateway/security/prompt_guard.py
- [[Tag a segment and append it to the session's provenance log.]] - rationale - gateway/security/context_guard.py
- [[Tagged provenance record for a context segment.]] - rationale - gateway/security/context_guard.py
- [[Test PromptGuard initialization]] - rationale - gateway/tests/test_prompt_guard.py
- [[Test that normal messages pass through]] - rationale - gateway/tests/test_prompt_guard.py
- [[TestAuditChainPerformance]] - code - gateway/tests/test_performance.py
- [[TestBenchmarkBaseline]] - code - gateway/tests/test_performance.py
- [[TestContextIntegrityScorer]] - code - gateway/tests/test_context_integrity.py
- [[TestFullPipelineLatency]] - code - gateway/tests/test_performance.py
- [[TestPromptGuardPerformance]] - code - gateway/tests/test_performance.py
- [[TestReanchorDelimiters]] - code - gateway/tests/test_prompt_guard.py
- [[TestSystemPromptHMAC]] - code - gateway/tests/test_prompt_guard.py
- [[TestToolResultScan]] - code - gateway/tests/test_prompt_guard.py
- [[TestTrustManagerPerformance]] - code - gateway/tests/test_performance.py
- [[Tests for indirect prompt injection detection in tool results.]] - rationale - gateway/tests/test_prompt_guard.py
- [[Tool result scan blocks at score ≥ 0.6 vs direct scan threshold of 0.8.]] - rationale - gateway/tests/test_prompt_guard.py
- [[Trust check 10000 lookups in  1s.]] - rationale - gateway/tests/test_performance.py
- [[Untrusted segment injected after system segment reduces score.]] - rationale - gateway/tests/test_context_integrity.py
- [[Verifying a tampered prompt should return False.]] - rationale - gateway/tests/test_prompt_guard.py
- [[Write 1000 audit entries in under 5 seconds.]] - rationale - gateway/tests/test_performance.py
- [[_make_segment()]] - code - gateway/tests/test_context_integrity.py
- [[context_integrity.py]] - code - gateway/security/context_integrity.py
- [[detect_base64_payloads()]] - code - gateway/security/input_normalizer.py
- [[guard()_1]] - code - gateway/tests/test_context_integrity.py
- [[prompt_guard()_1]] - code - gateway/tests/test_prompt_guard.py
- [[prompt_guard()_2]] - code - gateway/tests/test_security_integration.py
- [[register_system_prompt + verify_system_prompt should succeed.]] - rationale - gateway/tests/test_prompt_guard.py
- [[scorer()]] - code - gateway/tests/test_context_integrity.py
- [[test_benign_message()]] - code - gateway/tests/test_prompt_guard.py
- [[test_context_integrity.py]] - code - gateway/tests/test_context_integrity.py
- [[test_performance.py]] - code - gateway/tests/test_performance.py
- [[test_prompt_guard.py]] - code - gateway/tests/test_prompt_guard.py
- [[test_prompt_guard_init()]] - code - gateway/tests/test_prompt_guard.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/ServiceManager
SORT file.name ASC
```

## Connections to other communities
- 24 edges to [[_COMMUNITY_lifespan.py]]
- 23 edges to [[_COMMUNITY_ResourceGuard]]
- 17 edges to [[_COMMUNITY_EgressPolicy]]
- 15 edges to [[_COMMUNITY_WebProxyConfig]]
- 13 edges to [[_COMMUNITY_RBACConfig]]
- 12 edges to [[_COMMUNITY_BotConfig]]
- 11 edges to [[_COMMUNITY_TrustManager]]
- 11 edges to [[_COMMUNITY_MemoryIntegrityMonitor]]
- 7 edges to [[_COMMUNITY_KillSwitchMonitor]]
- 7 edges to [[_COMMUNITY_ConsentFramework]]
- 6 edges to [[_COMMUNITY_EgressFilter]]
- 5 edges to [[_COMMUNITY_test_scanner_integration.py]]
- 4 edges to [[_COMMUNITY__wrap_response()]]
- 4 edges to [[_COMMUNITY_WS-E Security Audit — AgentShroud v1.2 (Gateway]]
- 4 edges to [[_COMMUNITY_A2AGovernanceProxy]]
- 3 edges to [[_COMMUNITY_chatbotmain.py]]
- 3 edges to [[_COMMUNITY_PipelineAction]]
- 3 edges to [[_COMMUNITY_test_approval_queue.py]]
- 3 edges to [[_COMMUNITY_TestApprovalHardening]]
- 2 edges to [[_COMMUNITY_FileSandbox]]
- 2 edges to [[_COMMUNITY_awslabs.aws-api-mcp-server configuration (--read]]
- 2 edges to [[_COMMUNITY_ProgressiveLockdown]]
- 2 edges to [[_COMMUNITY_Local LLM Support — Implementation Review]]
- 1 edge to [[_COMMUNITY_SSHProxy]]
- 1 edge to [[_COMMUNITY_test_llm_proxy_failover.py]]
- 1 edge to [[_COMMUNITY_test_mfa_guard.py]]
- 1 edge to [[_COMMUNITY_EgressApprovalQueue]]
- 1 edge to [[_COMMUNITY_1Password op-proxy (POST credentialsop-proxy;]]
- 1 edge to [[_COMMUNITY_Skill Technical Illustrator (TI)]]
- 1 edge to [[_COMMUNITY_test_dashboard.py]]

## Top bridge nodes
- [[PromptGuard]] - degree 150, connects to 25 communities
- [[test_performance.py]] - degree 16, connects to 5 communities
- [[test_prompt_guard.py]] - degree 14, connects to 4 communities
- [[TestAuditChainPerformance]] - degree 12, connects to 4 communities
- [[TestPromptGuardPerformance]] - degree 12, connects to 4 communities