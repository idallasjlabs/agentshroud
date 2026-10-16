---
type: community
cohesion: 0.03
members: 102
---

# agentshroud-blueteam/SKILL.md

**Cohesion:** 0.03 - loosely connected
**Members:** 102 nodes

## Members
- [[dot-__init__()_140]] - code - gateway/security/prompt_protection.py
- [[dot-__init__()_141]] - code - gateway/security/tool_result_injection.py
- [[dot-_calculate_similarity()]] - code - gateway/security/prompt_protection.py
- [[dot-_compile_detection_patterns()_1]] - code - gateway/security/prompt_protection.py
- [[dot-_detect_hidden_instructions()]] - code - gateway/security/context_guard.py
- [[dot-_detect_instruction_injection()]] - code - gateway/security/context_guard.py
- [[dot-_detect_rapid_context_growth()]] - code - gateway/security/context_guard.py
- [[dot-_detect_repetition_attacks()]] - code - gateway/security/context_guard.py
- [[dot-_load_protected_content()]] - code - gateway/security/prompt_protection.py
- [[dot-_redact_fuzzy_match()]] - code - gateway/security/prompt_protection.py
- [[dot-_redact_match()]] - code - gateway/security/prompt_protection.py
- [[dot-add_protected_content()]] - code - gateway/security/prompt_protection.py
- [[dot-analyze_message()]] - code - gateway/security/context_guard.py
- [[dot-get_protection_stats()]] - code - gateway/security/prompt_protection.py
- [[dot-guard()_5]] - code - gateway/tests/test_context_guard.py
- [[dot-register_bot_hostnames()]] - code - gateway/security/prompt_protection.py
- [[dot-scan_response()_2]] - code - gateway/security/prompt_protection.py
- [[dot-should_block_message()]] - code - gateway/security/context_guard.py
- [[dot-test_empty_provenance_for_unknown_session()]] - code - gateway/tests/test_context_guard.py
- [[dot-test_few_repetitions_allowed()]] - code - gateway/tests/test_context_guard.py
- [[dot-test_normal_message_allowed()]] - code - gateway/tests/test_context_guard.py
- [[dot-test_normal_sized_message_allowed()]] - code - gateway/tests/test_context_guard.py
- [[dot-test_oversized_message_blocked()]] - code - gateway/tests/test_context_guard.py
- [[dot-test_repeated_pattern_flagged()]] - code - gateway/tests/test_context_guard.py
- [[dot-test_segment_hash_integrity()]] - code - gateway/tests/test_context_guard.py
- [[dot-test_segment_provenance_ordering()]] - code - gateway/tests/test_context_guard.py
- [[dot-test_segment_tagging_basic()]] - code - gateway/tests/test_context_guard.py
- [[dot-test_separate_sessions_isolated()]] - code - gateway/tests/test_context_guard.py
- [[dot-test_short_repetitions_allowed()]] - code - gateway/tests/test_context_guard.py
- [[A piece of content that should be protected from disclosure.]] - rationale - gateway/security/prompt_protection.py
- [[Add bot container hostnames to the infrastructure detection patterns.          C]] - rationale - gateway/security/prompt_protection.py
- [[Add content to the protected registry.          Args             name Identifi]] - rationale - gateway/security/prompt_protection.py
- [[AgentShroud Blue Team Security Auditor (SEC-DEFENSE)]] - document - .agents/skills/i-sec-defense/SKILL.md
- [[AgentShroud Module Inventory (Blue Team)]] - document - skills/custom/agentshroud-blueteam/references/module-inventory.md
- [[AgentShroud Module Inventory (Red Team)]] - document - skills/custom/agentshroud-redteam/references/module-inventory.md
- [[AgentShroud Red Team Adversarial Tester (SEC-OFFENSE)]] - document - .agents/skills/i-sec-offense/SKILL.md
- [[AgentShroud Skills Library]] - document - skills/README.md
- [[Analyze a message for context poisoning attempts.          Args             ses]] - rationale - gateway/security/context_guard.py
- [[Any_53]] - code - gateway/security/prompt_protection.py
- [[Blue Team Security Auditor README]] - document - .agents/skills/i-sec-defense/README.md
- [[CVE-2026-22172 — WebSocket Scope Self-Declaration]] - rationale - docs/security/cve-mitigation-matrix.md
- [[CVE-2026-22708 — AI Agent Container Escape via Prompt Injection]] - rationale - docs/security/cve-mitigation-matrix.md
- [[CVE-2026-30741 — RCE via Request-Side Prompt Injection]] - rationale - docs/security/cve-mitigation-matrix.md
- [[CVE-2026-32922 — Token Scope Expansion via device.token.rotate]] - rationale - docs/security/cve-mitigation-matrix.md
- [[CVE-2026-34425 — Preflight Validation Bypass (Shell-Bleed)]] - rationale - docs/security/cve-mitigation-matrix.md
- [[CVE-2026-3690 — Canvas Authentication Bypass]] - rationale - docs/security/cve-mitigation-matrix.md
- [[Calculate similarity between text and protected content.]] - rationale - gateway/security/prompt_protection.py
- [[Check if message should be allowed, with detailed findings.      Args         t]] - rationale - gateway/security/context_guard.py
- [[Compile regex patterns for detecting disclosure attempts.]] - rationale - gateway/security/prompt_protection.py
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
- [[Get statistics about the protection system.]] - rationale - gateway/security/prompt_protection.py
- [[Get the global context guard instance.]] - rationale - gateway/security/context_guard.py
- [[Initialize prompt protection system.          Args             config Configur]] - rationale - gateway/security/prompt_protection.py
- [[Initialize the scanner with optional custom rules.          Args             cu]] - rationale - gateway/security/tool_result_injection.py
- [[InjectionRule]] - code - gateway/security/tool_result_injection.py
- [[Load protected content from configured sources.]] - rationale - gateway/security/prompt_protection.py
- [[Main system prompt protection engine.      Maintains fingerprints of sensitive c]] - rationale - gateway/security/prompt_protection.py
- [[Match]] - code - gateway/security/prompt_protection.py
- [[Module Coverage Heat Map Legend (EMAC—)]] - concept - skills/custom/agentshroud-blueteam/SKILL.md
- [[OpenClaw Built-in Skills]] - document - skills/README.md
- [[PromptProtection]] - code - gateway/security/prompt_protection.py
- [[ProtectedContent]] - code - gateway/security/prompt_protection.py
- [[Red Team Adversarial Tester README]] - document - .agents/skills/i-sec-offense/README.md
- [[Red Team Assessment Plan (Steve Hay Plan, Red Team copy)]] - document - skills/custom/agentshroud-redteam/references/steve-hay-plan.md
- [[Redact text that fuzzy matches protected content.]] - rationale - gateway/security/prompt_protection.py
- [[RedactionResult_1]] - code - gateway/security/prompt_protection.py
- [[Replace a regex match with a redaction placeholder.]] - rationale - gateway/security/prompt_protection.py
- [[Result of scanning and redacting content.]] - rationale - gateway/security/prompt_protection.py
- [[Rule for detecting injection patterns in tool results.]] - rationale - gateway/security/tool_result_injection.py
- [[STPA-Sec Loss Categories (L-1 Data Disclosure, L-2 Unauthorized Actions, L-3 Agent Integrity, L-4 Audit Integrity)]] - concept - skills/custom/agentshroud-blueteam/references/steve-hay-assessment.md
- [[STPA-Sec Methodology]] - concept - .agents/skills/i-sec-defense/SKILL.md
- [[STPA-Sec Methodology_1]] - concept - docker/config/openclaw/skills/i-sec-defense/SKILL.md
- [[Scan text for protected content and return redacted version.          Args]] - rationale - gateway/security/prompt_protection.py
- [[SessionContext_1]] - code - gateway/security/context_guard.py
- [[Steve Hay Adversary Model]] - concept - .agents/skills/i-sec-offense/SKILL.md
- [[System Prompt Protection Tests]] - code - gateway/tests/test_prompt_protection.py
- [[TestCheckMessage]] - code - gateway/tests/test_context_guard.py
- [[TestSourceTagging]] - code - gateway/tests/test_context_guard.py
- [[Unsafe Control Actions (UCA-1 through UCA-17)]] - concept - skills/custom/agentshroud-blueteam/references/steve-hay-assessment.md
- [[Usage_72]] - document - skills/README.md
- [[agentshroud-blueteamSKILL]] - document - skills/custom/agentshroud-blueteam/SKILL.md
- [[check_message()]] - code - gateway/security/context_guard.py
- [[context_guard.py]] - code - gateway/security/context_guard.py
- [[cve-mitigation-matrix]] - document - docs/security/cve-mitigation-matrix.md
- [[docsreviewsblue-team-audit-v0.7.0]] - concept - docs/reviews/blue-team-audit-v0.7.0.md
- [[docsreviewsred-team-report-v0.7.0]] - concept - docs/reviews/red-team-report-v0.7.0.md
- [[get_context_guard()]] - code - gateway/security/context_guard.py
- [[prompt_protection.py]] - code - gateway/security/prompt_protection.py
- [[skillsREADME]] - document - skills/README.md
- [[test_context_guard.py]] - code - gateway/tests/test_context_guard.py
- [[tool_result_injection.py]] - code - gateway/security/tool_result_injection.py
- [[xml_leak_filter.py]] - code - gateway/security/xml_leak_filter.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/agentshroud-blueteam/SKILLmd
SORT file.name ASC
```

## Connections to other communities
- 13 edges to [[_COMMUNITY_MiddlewareManager]]
- 12 edges to [[_COMMUNITY_AlertDispatcher]]
- 6 edges to [[_COMMUNITY_PIIConfig]]
- 5 edges to [[_COMMUNITY_TestPromptProtection]]
- 5 edges to [[_COMMUNITY_Action]]
- 4 edges to [[_COMMUNITY_ContextSegment]]
- 4 edges to [[_COMMUNITY_AuditChain]]
- 3 edges to [[_COMMUNITY_HeuristicClassifier]]
- 3 edges to [[_COMMUNITY_KillSwitchMonitor]]
- 3 edges to [[_COMMUNITY_MultiTurnTracker]]
- 2 edges to [[_COMMUNITY_KeyRotationManager]]
- 2 edges to [[_COMMUNITY_agentshroud-blueteamSKILL_1]]
- 2 edges to [[_COMMUNITY_gatewayingest_apimain.py (hermes-dashboard HTTP + WebSocket reverse proxy)]]
- 2 edges to [[_COMMUNITY_AuditStore]]
- 2 edges to [[_COMMUNITY_TestToolChainAnalyzer]]
- 2 edges to [[_COMMUNITY_dot-_filter_outbound]]
- 2 edges to [[_COMMUNITY_ApprovalHardening]]
- 2 edges to [[_COMMUNITY_ApprovalQueueConfig]]
- 2 edges to [[_COMMUNITY_ApprovalQueueConfig_1]]
- 2 edges to [[_COMMUNITY_MiddlewareManager_2]]
- 1 edge to [[_COMMUNITY_dockerscriptssecurity-scan.sh]]
- 1 edge to [[_COMMUNITY_InjectionAction]]
- 1 edge to [[_COMMUNITY_AgentShroud™ CVE Mitigation Matrix]]
- 1 edge to [[_COMMUNITY_system-requirements]]
- 1 edge to [[_COMMUNITY_agentshroud-blueteamSKILL_2]]
- 1 edge to [[_COMMUNITY_AgentShroud Blue Team Security Auditor_3]]
- 1 edge to [[_COMMUNITY_FR3 System Integrity]]
- 1 edge to [[_COMMUNITY_colima-health-check.sh]]
- 1 edge to [[_COMMUNITY_DNSFilterConfig]]
- 1 edge to [[_COMMUNITY_egress_filter.py]]
- 1 edge to [[_COMMUNITY_RBACConfig]]
- 1 edge to [[_COMMUNITY_test_agent_cve_registry.py]]
- 1 edge to [[_COMMUNITY_AgentShroud Security Verification (13-check driver)]]

## Top bridge nodes
- [[agentshroud-blueteamSKILL]] - degree 29, connects to 17 communities
- [[AgentShroud Blue Team Security Auditor (SEC-DEFENSE)]] - degree 27, connects to 16 communities
- [[cve-mitigation-matrix]] - degree 14, connects to 8 communities
- [[tool_result_injection.py]] - degree 12, connects to 6 communities
- [[PromptProtection]] - degree 23, connects to 3 communities
