---
type: community
members: 104
---

# agentshroud-blueteam/SKILL.md

**Members:** 104 nodes

## Members
- [[dot-__init__()_113]] - code - gateway/security/tool_result_injection.py
- [[dot-__init__()_114]] - code - gateway/security/xml_leak_filter.py
- [[dot-_detect_hidden_instructions()]] - code - gateway/security/context_guard.py
- [[dot-_detect_instruction_injection()]] - code - gateway/security/context_guard.py
- [[dot-_detect_rapid_context_growth()]] - code - gateway/security/context_guard.py
- [[dot-_detect_repetition_attacks()]] - code - gateway/security/context_guard.py
- [[dot-analyze_message()]] - code - gateway/security/context_guard.py
- [[dot-filter_function_calls_only()]] - code - gateway/security/xml_leak_filter.py
- [[dot-filter_response()_1]] - code - gateway/security/xml_leak_filter.py
- [[dot-guard()_2]] - code - gateway/tests/test_context_guard.py
- [[dot-scan_command_injection()]] - code - gateway/security/xml_leak_filter.py
- [[dot-setup_method()_19]] - code - gateway/tests/test_xml_leak_filter.py
- [[dot-should_block_message()]] - code - gateway/security/context_guard.py
- [[dot-test_clean_response_passes_through()]] - code - gateway/tests/test_xml_leak_filter.py
- [[dot-test_clean_text_passes()]] - code - gateway/tests/test_xml_leak_filter.py
- [[dot-test_empty_provenance_for_unknown_session()]] - code - gateway/tests/test_context_guard.py
- [[dot-test_empty_text_returns_clean()]] - code - gateway/tests/test_xml_leak_filter.py
- [[dot-test_few_repetitions_allowed()]] - code - gateway/tests/test_context_guard.py
- [[dot-test_file_path_removal()]] - code - gateway/tests/test_xml_leak_filter.py
- [[dot-test_function_calls_xml_removal()]] - code - gateway/tests/test_xml_leak_filter.py
- [[dot-test_normal_message_allowed()]] - code - gateway/tests/test_context_guard.py
- [[dot-test_normal_sized_message_allowed()]] - code - gateway/tests/test_context_guard.py
- [[dot-test_oversized_message_blocked()]] - code - gateway/tests/test_context_guard.py
- [[dot-test_python_eval_detected()]] - code - gateway/tests/test_xml_leak_filter.py
- [[dot-test_quick_function_calls_filter()]] - code - gateway/tests/test_xml_leak_filter.py
- [[dot-test_repeated_pattern_flagged()]] - code - gateway/tests/test_context_guard.py
- [[dot-test_segment_hash_integrity()]] - code - gateway/tests/test_context_guard.py
- [[dot-test_segment_provenance_ordering()]] - code - gateway/tests/test_context_guard.py
- [[dot-test_segment_tagging_basic()]] - code - gateway/tests/test_context_guard.py
- [[dot-test_separate_sessions_isolated()]] - code - gateway/tests/test_context_guard.py
- [[dot-test_shell_injection_detected()]] - code - gateway/tests/test_xml_leak_filter.py
- [[dot-test_short_repetitions_allowed()]] - code - gateway/tests/test_context_guard.py
- [[dot-test_sql_injection_detected()]] - code - gateway/tests/test_xml_leak_filter.py
- [[dot-xml_filter()]] - code - gateway/tests/test_xml_leak_filter.py
- [[AgentShroud Blue Team Security Auditor (SEC-DEFENSE)]] - document - .agents/skills/i-sec-defense/SKILL.md
- [[AgentShroud Module Inventory (Blue Team)]] - document - skills/custom/agentshroud-blueteam/references/module-inventory.md
- [[AgentShroud Module Inventory (Red Team)]] - document - skills/custom/agentshroud-redteam/references/module-inventory.md
- [[AgentShroud Red Team Adversarial Tester (SEC-OFFENSE)]] - document - .agents/skills/i-sec-offense/SKILL.md
- [[AgentShroud Skills Library]] - document - skills/README.md
- [[Analyze a message for context poisoning attempts.          Args             ses]] - rationale - gateway/security/context_guard.py
- [[Blue Team Security Auditor README]] - document - .agents/skills/i-sec-defense/README.md
- [[CVE-2026-22172 — WebSocket Scope Self-Declaration]] - rationale - docs/security/cve-mitigation-matrix.md
- [[CVE-2026-22708 — AI Agent Container Escape via Prompt Injection]] - rationale - docs/security/cve-mitigation-matrix.md
- [[CVE-2026-30741 — RCE via Request-Side Prompt Injection]] - rationale - docs/security/cve-mitigation-matrix.md
- [[CVE-2026-32922 — Token Scope Expansion via device.token.rotate]] - rationale - docs/security/cve-mitigation-matrix.md
- [[CVE-2026-34425 — Preflight Validation Bypass (Shell-Bleed)]] - rationale - docs/security/cve-mitigation-matrix.md
- [[CVE-2026-3690 — Canvas Authentication Bypass]] - rationale - docs/security/cve-mitigation-matrix.md
- [[Check if message should be allowed, with detailed findings.      Args         t]] - rationale - gateway/security/context_guard.py
- [[Context tracking for a session.]] - rationale - gateway/security/context_guard.py
- [[ContextAttack]] - code - gateway/security/context_guard.py
- [[Custom Skills]] - document - skills/README.md
- [[Detect hidden instructions buried in large text blocks.]] - rationale - gateway/security/context_guard.py
- [[Detect instruction injection attempts.]] - rationale - gateway/security/context_guard.py
- [[Detect rapid context window filling.]] - rationale - gateway/security/context_guard.py
- [[Detect repetition-based context stuffing attacks.]] - rationale - gateway/security/context_guard.py
- [[Detected context window attack attempt.]] - rationale - gateway/security/context_guard.py
- [[Determine if a message should be blocked.          Returns             Tuple of]] - rationale - gateway/security/context_guard.py
- [[Directory Structure_1]] - document - skills/README.md
- [[Enterprise Security Feature Priorities (Steve Hay Assessment, Red Team copy)]] - document - skills/custom/agentshroud-redteam/references/steve-hay-assessment.md
- [[Filter outbound response content to remove sensitive information.          Args]] - rationale - gateway/security/xml_leak_filter.py
- [[Filter to remove sensitive XML and path information from outbound responses.]] - rationale - gateway/security/xml_leak_filter.py
- [[FilterResult]] - code - gateway/security/xml_leak_filter.py
- [[Get the global context guard instance.]] - rationale - gateway/security/context_guard.py
- [[Initialize the filter with predefined patterns.]] - rationale - gateway/security/xml_leak_filter.py
- [[Initialize the scanner with optional custom rules.          Args             cu]] - rationale - gateway/security/tool_result_injection.py
- [[InjectionRule]] - code - gateway/security/tool_result_injection.py
- [[Module Coverage Heat Map Legend (EMAC—)]] - concept - skills/custom/agentshroud-blueteam/SKILL.md
- [[OpenClaw Built-in Skills]] - document - skills/README.md
- [[Quick filter that only removes function call XML (for performance).          Arg]] - rationale - gateway/security/xml_leak_filter.py
- [[Red Team Adversarial Tester README]] - document - .agents/skills/i-sec-offense/README.md
- [[Red Team Assessment Plan (Steve Hay Plan, Red Team copy)]] - document - skills/custom/agentshroud-redteam/references/steve-hay-plan.md
- [[Result from XML leak filtering.]] - rationale - gateway/security/xml_leak_filter.py
- [[Rule for detecting injection patterns in tool results.]] - rationale - gateway/security/tool_result_injection.py
- [[STPA-Sec Loss Categories (L-1 Data Disclosure, L-2 Unauthorized Actions, L-3 Agent Integrity, L-4 Audit Integrity)]] - concept - skills/custom/agentshroud-blueteam/references/steve-hay-assessment.md
- [[STPA-Sec Methodology]] - concept - .agents/skills/i-sec-defense/SKILL.md
- [[STPA-Sec Methodology_1]] - concept - docker/config/openclaw/skills/i-sec-defense/SKILL.md
- [[Scan outbound text for command  code injection patterns.          Does NOT modi]] - rationale - gateway/security/xml_leak_filter.py
- [[SessionContext]] - code - gateway/security/context_guard.py
- [[Set up test fixtures._4]] - rationale - gateway/tests/test_xml_leak_filter.py
- [[Steve Hay Adversary Model]] - concept - .agents/skills/i-sec-offense/SKILL.md
- [[Test cases for XMLLeakFilter.]] - rationale - gateway/tests/test_xml_leak_filter.py
- [[Test removal of file paths from responses.]] - rationale - gateway/tests/test_xml_leak_filter.py
- [[Test removal of function call XML blocks.]] - rationale - gateway/tests/test_xml_leak_filter.py
- [[Test that clean responses pass through unchanged.]] - rationale - gateway/tests/test_xml_leak_filter.py
- [[Test the performance-optimized function calls only filter.]] - rationale - gateway/tests/test_xml_leak_filter.py
- [[TestCheckMessage]] - code - gateway/tests/test_context_guard.py
- [[TestCommandInjectionScan]] - code - gateway/tests/test_xml_leak_filter.py
- [[TestSourceTagging]] - code - gateway/tests/test_context_guard.py
- [[TestXMLLeakFilter]] - code - gateway/tests/test_xml_leak_filter.py
- [[Unsafe Control Actions (UCA-1 through UCA-17)]] - concept - skills/custom/agentshroud-blueteam/references/steve-hay-assessment.md
- [[Usage_66]] - document - skills/README.md
- [[XMLLeakFilter]] - code - gateway/security/xml_leak_filter.py
- [[agentshroud-blueteamSKILL]] - document - skills/custom/agentshroud-blueteam/SKILL.md
- [[check_message()]] - code - gateway/security/context_guard.py
- [[context_guard.py]] - code - gateway/security/context_guard.py
- [[cve-mitigation-matrix]] - document - docs/security/cve-mitigation-matrix.md
- [[docsreviewsblue-team-audit-v0.7.0]] - concept - docs/reviews/blue-team-audit-v0.7.0.md
- [[docsreviewsred-team-report-v0.7.0]] - concept - docs/reviews/red-team-report-v0.7.0.md
- [[get_context_guard()]] - code - gateway/security/context_guard.py
- [[skillsREADME]] - document - skills/README.md
- [[test_context_guard.py]] - code - gateway/tests/test_context_guard.py
- [[test_xml_leak_filter.py]] - code - gateway/tests/test_xml_leak_filter.py
- [[tool_result_injection.py]] - code - gateway/security/tool_result_injection.py
- [[xml_leak_filter.py]] - code - gateway/security/xml_leak_filter.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/agentshroud-blueteam/SKILLmd
SORT file.name ASC
```

## Connections to other communities
- 31 edges to [[_COMMUNITY_AlertDispatcher]]
- 6 edges to [[_COMMUNITY_ToolResultSanitizer]]
- 5 edges to [[_COMMUNITY_TestToolChainAnalyzer]]
- 5 edges to [[_COMMUNITY_MiddlewareManager]]
- 4 edges to [[_COMMUNITY_agentshroud-blueteamSKILL.md (3)]]
- 4 edges to [[_COMMUNITY_ContextSegment]]
- 3 edges to [[_COMMUNITY_TelegramAPIProxy (3)]]
- 3 edges to [[_COMMUNITY_KillSwitchMonitor]]
- 2 edges to [[_COMMUNITY_gatewayingest_apimain.py (hermes-dashboard HTTP + WebSocket reverse proxy)]]
- 2 edges to [[_COMMUNITY_ApprovalQueueConfig (2)]]
- 2 edges to [[_COMMUNITY_TestOutboundInfoFilter]]
- 2 edges to [[_COMMUNITY_PipelineAction]]
- 2 edges to [[_COMMUNITY_ApprovalHardening]]
- 2 edges to [[_COMMUNITY_ApprovalQueueConfig (5)]]
- 2 edges to [[_COMMUNITY_AuditEvent]]
- 2 edges to [[_COMMUNITY_UserSessionManager]]
- 2 edges to [[_COMMUNITY_PipelineAction (2)]]
- 2 edges to [[_COMMUNITY_FR3 System Integrity]]
- 2 edges to [[_COMMUNITY_InjectionAction (2)]]
- 1 edge to [[_COMMUNITY_MiddlewareManager (4)]]
- 1 edge to [[_COMMUNITY_egress_filter.py]]
- 1 edge to [[_COMMUNITY_MiddlewareManager (5)]]
- 1 edge to [[_COMMUNITY_InjectionAction]]
- 1 edge to [[_COMMUNITY_AgentShroud™ CVE Mitigation Matrix]]
- 1 edge to [[_COMMUNITY_system-requirements]]
- 1 edge to [[_COMMUNITY_AgentShroud Blue Team Security Auditor (4)]]
- 1 edge to [[_COMMUNITY_AuditChain]]
- 1 edge to [[_COMMUNITY_colima-health-check.sh]]
- 1 edge to [[_COMMUNITY_DNSFilterConfig]]
- 1 edge to [[_COMMUNITY_test_agent_cve_registry.py]]
- 1 edge to [[_COMMUNITY_AgentShroud Security Verification (13-check driver)]]

## Top bridge nodes
- [[AgentShroud Blue Team Security Auditor (SEC-DEFENSE)]] - degree 27, connects to 17 communities
- [[agentshroud-blueteamSKILL]] - degree 29, connects to 16 communities
- [[cve-mitigation-matrix]] - degree 14, connects to 8 communities
- [[tool_result_injection.py]] - degree 12, connects to 6 communities
- [[XMLLeakFilter]] - degree 27, connects to 3 communities
