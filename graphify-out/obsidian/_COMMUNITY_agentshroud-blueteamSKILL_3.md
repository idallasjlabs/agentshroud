---
type: community
cohesion: 0.04
members: 68
---

# agentshroud-blueteam/SKILL.md

**Cohesion:** 0.04 - loosely connected
**Members:** 68 nodes

## Members
- [[dot-__init__()_131]] - code - gateway/security/context_guard.py
- [[dot-_detect_hidden_instructions()]] - code - gateway/security/context_guard.py
- [[dot-_detect_instruction_injection()]] - code - gateway/security/context_guard.py
- [[dot-_detect_rapid_context_growth()]] - code - gateway/security/context_guard.py
- [[dot-_detect_repetition_attacks()]] - code - gateway/security/context_guard.py
- [[dot-analyze_message()]] - code - gateway/security/context_guard.py
- [[dot-cleanup_old_sessions()]] - code - gateway/security/context_guard.py
- [[dot-export_attack_report()]] - code - gateway/security/context_guard.py
- [[dot-get_attack_summary()]] - code - gateway/security/context_guard.py
- [[dot-get_session_risk_level()]] - code - gateway/security/context_guard.py
- [[dot-guard()_5]] - code - gateway/tests/test_context_guard.py
- [[dot-should_block_message()]] - code - gateway/security/context_guard.py
- [[dot-test_context_guard_session_isolation_under_load()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_context_guard_tool_manipulation()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_deeply_nested_context_attacks()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_empty_inputs_everywhere()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_empty_provenance_for_unknown_session()]] - code - gateway/tests/test_context_guard.py
- [[dot-test_few_repetitions_allowed()]] - code - gateway/tests/test_context_guard.py
- [[dot-test_json_injection_in_context()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_normal_message_allowed()]] - code - gateway/tests/test_context_guard.py
- [[dot-test_normal_sized_message_allowed()]] - code - gateway/tests/test_context_guard.py
- [[dot-test_oversized_json_payload()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_oversized_message_blocked()]] - code - gateway/tests/test_context_guard.py
- [[dot-test_repeated_pattern_flagged()]] - code - gateway/tests/test_context_guard.py
- [[dot-test_segment_hash_integrity()]] - code - gateway/tests/test_context_guard.py
- [[dot-test_segment_provenance_ordering()]] - code - gateway/tests/test_context_guard.py
- [[dot-test_segment_tagging_basic()]] - code - gateway/tests/test_context_guard.py
- [[dot-test_separate_sessions_isolated()]] - code - gateway/tests/test_context_guard.py
- [[dot-test_short_repetitions_allowed()]] - code - gateway/tests/test_context_guard.py
- [[Analyze a message for context poisoning attempts.          Args             ses]] - rationale - gateway/security/context_guard.py
- [[Any_47]] - code - gateway/security/context_guard.py
- [[CVE-2026-22172 — WebSocket Scope Self-Declaration]] - rationale - docs/security/cve-mitigation-matrix.md
- [[CVE-2026-22708 — AI Agent Container Escape via Prompt Injection]] - rationale - docs/security/cve-mitigation-matrix.md
- [[CVE-2026-30741 — RCE via Request-Side Prompt Injection]] - rationale - docs/security/cve-mitigation-matrix.md
- [[CVE-2026-32922 — Token Scope Expansion via device.token.rotate]] - rationale - docs/security/cve-mitigation-matrix.md
- [[CVE-2026-34425 — Preflight Validation Bypass (Shell-Bleed)]] - rationale - docs/security/cve-mitigation-matrix.md
- [[CVE-2026-3690 — Canvas Authentication Bypass]] - rationale - docs/security/cve-mitigation-matrix.md
- [[Check if message should be allowed, with detailed findings.      Args         t]] - rationale - gateway/security/context_guard.py
- [[Clean up old session data.]] - rationale - gateway/security/context_guard.py
- [[Context guard should detect tool result manipulation.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Context tracking for a session.]] - rationale - gateway/security/context_guard.py
- [[ContextAttack]] - code - gateway/security/context_guard.py
- [[ContextGuard]] - code - gateway/security/context_guard.py
- [[Detect hidden instructions buried in large text blocks.]] - rationale - gateway/security/context_guard.py
- [[Detect instruction injection attempts.]] - rationale - gateway/security/context_guard.py
- [[Detect rapid context window filling.]] - rationale - gateway/security/context_guard.py
- [[Detect repetition-based context stuffing attacks.]] - rationale - gateway/security/context_guard.py
- [[Detected context window attack attempt.]] - rationale - gateway/security/context_guard.py
- [[Determine if a message should be blocked.          Returns             Tuple of]] - rationale - gateway/security/context_guard.py
- [[Empty strings shouldn't crash any module.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Export attack detection report.]] - rationale - gateway/security/context_guard.py
- [[Get risk level for a session based on detected attacks.]] - rationale - gateway/security/context_guard.py
- [[Get summary of detected attacks.]] - rationale - gateway/security/context_guard.py
- [[Get the global context guard instance.]] - rationale - gateway/security/context_guard.py
- [[Guard against context window poisoning attacks.]] - rationale - gateway/security/context_guard.py
- [[JSON injection in message shouldn't manipulate context.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Nested context attacks shouldn't cause stack overflow.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[SessionContext_1]] - code - gateway/security/context_guard.py
- [[Sessions shouldn't leak data under concurrent access.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[TestCheckMessage]] - code - gateway/tests/test_context_guard.py
- [[TestSourceTagging]] - code - gateway/tests/test_context_guard.py
- [[Very large JSON shouldn't crash the parser.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[check_message()]] - code - gateway/security/context_guard.py
- [[context_guard.py]] - code - gateway/security/context_guard.py
- [[cve-mitigation-matrix]] - document - docs/security/cve-mitigation-matrix.md
- [[get_context_guard()]] - code - gateway/security/context_guard.py
- [[test_context_guard.py]] - code - gateway/tests/test_context_guard.py
- [[tool_result_injection.py]] - code - gateway/security/tool_result_injection.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/agentshroud-blueteam/SKILLmd
SORT file.name ASC
```

## Connections to other communities
- 27 edges to [[_COMMUNITY_AlertDispatcher]]
- 14 edges to [[_COMMUNITY_PipelineAction]]
- 13 edges to [[_COMMUNITY_MiddlewareManager]]
- 7 edges to [[_COMMUNITY_ContextSegment]]
- 7 edges to [[_COMMUNITY_MiddlewareManager_8]]
- 5 edges to [[_COMMUNITY_InjectionAction]]
- 4 edges to [[_COMMUNITY_MiddlewareManager_3]]
- 3 edges to [[_COMMUNITY_TelegramAPIProxy_2]]
- 2 edges to [[_COMMUNITY_InjectionAction_1]]
- 1 edge to [[_COMMUNITY_KillSwitchMonitor_1]]
- 1 edge to [[_COMMUNITY_system-requirements]]
- 1 edge to [[_COMMUNITY_sync-cve-registry.py]]
- 1 edge to [[_COMMUNITY_MiddlewareManager_2]]
- 1 edge to [[_COMMUNITY_AgentShroud™ CVE Mitigation Matrix]]
- 1 edge to [[_COMMUNITY_ResourceGuard]]
- 1 edge to [[_COMMUNITY_ToolResultSanitizer]]
- 1 edge to [[_COMMUNITY_KillSwitchMonitor]]
- 1 edge to [[_COMMUNITY_agentshroud-blueteamSKILL_2]]
- 1 edge to [[_COMMUNITY_egress_filter.py]]
- 1 edge to [[_COMMUNITY_MultiTurnTracker_1]]
- 1 edge to [[_COMMUNITY_ApprovalHardening_1]]
- 1 edge to [[_COMMUNITY_ApprovalQueueConfig_6]]
- 1 edge to [[_COMMUNITY_AlertDispatcher_1]]
- 1 edge to [[_COMMUNITY_dot-_filter_outbound]]
- 1 edge to [[_COMMUNITY_TrustConfig]]
- 1 edge to [[_COMMUNITY_colima-health-check.sh]]
- 1 edge to [[_COMMUNITY_DNSFilterConfig]]

## Top bridge nodes
- [[ContextGuard]] - degree 89, connects to 12 communities
- [[cve-mitigation-matrix]] - degree 14, connects to 8 communities
- [[tool_result_injection.py]] - degree 12, connects to 5 communities
- [[dot-analyze_message()]] - degree 12, connects to 2 communities
- [[context_guard.py]] - degree 9, connects to 2 communities
