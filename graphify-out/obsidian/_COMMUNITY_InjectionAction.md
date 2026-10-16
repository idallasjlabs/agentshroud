---
type: community
cohesion: 0.03
members: 84
---

# InjectionAction

**Cohesion:** 0.03 - loosely connected
**Members:** 84 nodes

## Members
- [[dot-__init__()_153]] - code - gateway/security/tool_result_injection.py
- [[dot-_detect_encoded_injection()]] - code - gateway/security/tool_result_injection.py
- [[dot-_detect_unicode_obfuscation()]] - code - gateway/security/tool_result_injection.py
- [[dot-scan_tool_result()_1]] - code - gateway/security/tool_result_injection.py
- [[dot-setup_method()_33]] - code - gateway/tests/test_tool_injection_scan.py
- [[dot-test_base64_clean_content_not_flagged()]] - code - gateway/tests/test_tool_result_injection.py
- [[dot-test_base64_encoded_injection()_1]] - code - gateway/tests/test_tool_injection_scan.py
- [[dot-test_base64_encoded_injection()_2]] - code - gateway/tests/test_tool_result_injection.py
- [[dot-test_clean_content_passes_through()]] - code - gateway/tests/test_tool_injection_scan.py
- [[dot-test_clean_tool_output_passes()]] - code - gateway/tests/test_tool_result_injection.py
- [[dot-test_empty_content()]] - code - gateway/tests/test_tool_result_injection.py
- [[dot-test_high_severity_strips_content()]] - code - gateway/tests/test_tool_result_injection.py
- [[dot-test_ignore_instructions_injection_high_severity()]] - code - gateway/tests/test_tool_injection_scan.py
- [[dot-test_ignore_previous_instructions()_1]] - code - gateway/tests/test_tool_result_injection.py
- [[dot-test_jailbreak_attempt()]] - code - gateway/tests/test_tool_result_injection.py
- [[dot-test_medium_severity_warns()]] - code - gateway/tests/test_tool_result_injection.py
- [[dot-test_new_instructions_override()_1]] - code - gateway/tests/test_tool_result_injection.py
- [[dot-test_none_content()]] - code - gateway/tests/test_tool_result_injection.py
- [[dot-test_prompt_extraction()_1]] - code - gateway/tests/test_tool_result_injection.py
- [[dot-test_role_reassignment()_2]] - code - gateway/tests/test_tool_result_injection.py
- [[dot-test_rtl_override_detected()]] - code - gateway/tests/test_tool_result_injection.py
- [[dot-test_social_engineering_admin()]] - code - gateway/tests/test_tool_result_injection.py
- [[dot-test_system_delimiter_injection()]] - code - gateway/tests/test_tool_result_injection.py
- [[dot-test_xml_function_injection()]] - code - gateway/tests/test_tool_result_injection.py
- [[dot-test_xml_function_injection_detection()]] - code - gateway/tests/test_tool_injection_scan.py
- [[dot-test_zero_width_chars_dont_bypass_detection()]] - code - gateway/tests/test_tool_result_injection.py
- [[AgentShroud Blue Team Security Auditor (SEC-DEFENSE)]] - document - .agents/skills/i-sec-defense/SKILL.md
- [[AgentShroud Module Inventory (Blue Team)]] - document - skills/custom/agentshroud-blueteam/references/module-inventory.md
- [[AgentShroud Module Inventory (Red Team)]] - document - skills/custom/agentshroud-redteam/references/module-inventory.md
- [[AgentShroud Red Team Adversarial Tester (SEC-OFFENSE)]] - document - .agents/skills/i-sec-offense/SKILL.md
- [[AgentShroud Skills Library]] - document - skills/README.md
- [[Benign base64 content should not trigger encoded injection.]] - rationale - gateway/tests/test_tool_result_injection.py
- [[Blue Team Security Auditor README]] - document - .agents/skills/i-sec-defense/README.md
- [[CVE-2026-34425 — Preflight Validation Bypass (Shell-Bleed)]] - rationale - docs/security/cve-mitigation-matrix.md
- [[Check for base64 or hex encoded injection attempts.]] - rationale - gateway/security/tool_result_injection.py
- [[Custom Skills]] - document - skills/README.md
- [[Detect unicode-based obfuscation techniques.]] - rationale - gateway/security/tool_result_injection.py
- [[Directory Structure_2]] - document - skills/README.md
- [[Enterprise Security Feature Priorities (Steve Hay Assessment, Red Team copy)]] - document - skills/custom/agentshroud-redteam/references/steve-hay-assessment.md
- [[Initialize the scanner with optional custom rules.          Args             cu]] - rationale - gateway/security/tool_result_injection.py
- [[InjectionResult]] - code - gateway/security/tool_result_injection.py
- [[InjectionRule]] - code - gateway/security/tool_result_injection.py
- [[InjectionSeverity]] - code - gateway/security/tool_result_injection.py
- [[Module Coverage Heat Map Legend (EMAC—)]] - concept - skills/custom/agentshroud-blueteam/SKILL.md
- [[OpenClaw Built-in Skills]] - document - skills/README.md
- [[Red Team Adversarial Tester README]] - document - .agents/skills/i-sec-offense/README.md
- [[Red Team Assessment Plan (Steve Hay Plan, Red Team copy)]] - document - skills/custom/agentshroud-redteam/references/steve-hay-plan.md
- [[Result from tool result injection scan.]] - rationale - gateway/security/tool_result_injection.py
- [[Rule for detecting injection patterns in tool results.]] - rationale - gateway/security/tool_result_injection.py
- [[STPA-Sec Loss Categories (L-1 Data Disclosure, L-2 Unauthorized Actions, L-3 Agent Integrity, L-4 Audit Integrity)]] - concept - skills/custom/agentshroud-blueteam/references/steve-hay-assessment.md
- [[STPA-Sec Methodology_1]] - concept - .agents/skills/i-sec-defense/SKILL.md
- [[STPA-Sec Methodology_2]] - concept - docker/config/openclaw/skills/i-sec-defense/SKILL.md
- [[Scan tool result content for injection attempts.          Args             tool]] - rationale - gateway/security/tool_result_injection.py
- [[Set up test fixtures._4]] - rationale - gateway/tests/test_tool_injection_scan.py
- [[Steve Hay Adversary Model]] - concept - .agents/skills/i-sec-offense/SKILL.md
- [[Strip potentially malicious markdown from tool results.      Removes     - Mark]] - rationale - gateway/security/input_normalizer.py
- [[Test cases for ToolResultInjectionScanner.]] - rationale - gateway/tests/test_tool_injection_scan.py
- [[Test detection of 'ignore previous instructions' injection.]] - rationale - gateway/tests/test_tool_injection_scan.py
- [[Test detection of XML function call injection.]] - rationale - gateway/tests/test_tool_injection_scan.py
- [[Test detection of base64 encoded injections.]] - rationale - gateway/tests/test_tool_injection_scan.py
- [[Test that clean content passes through unchanged.]] - rationale - gateway/tests/test_tool_injection_scan.py
- [[TestCleanContent]] - code - gateway/tests/test_tool_result_injection.py
- [[TestEncodedInjection]] - code - gateway/tests/test_tool_result_injection.py
- [[TestHighSeverity]] - code - gateway/tests/test_tool_result_injection.py
- [[TestMediumSeverity]] - code - gateway/tests/test_tool_result_injection.py
- [[TestSanitization]] - code - gateway/tests/test_tool_result_injection.py
- [[TestToolResultInjectionScanner]] - code - gateway/tests/test_tool_injection_scan.py
- [[TestUnicodeObfuscation]] - code - gateway/tests/test_tool_result_injection.py
- [[Unsafe Control Actions (UCA-1 through UCA-17)]] - concept - skills/custom/agentshroud-blueteam/references/steve-hay-assessment.md
- [[Usage_92]] - document - skills/README.md
- [[Zero-width chars are stripped by normalize_input, so injection is still caught.]] - rationale - gateway/tests/test_tool_result_injection.py
- [[agentshroud-blueteamSKILL]] - document - skills/custom/agentshroud-blueteam/SKILL.md
- [[canary_tripwire.py]] - code - gateway/security/canary_tripwire.py
- [[docsreviewsblue-team-audit-v0.7.0]] - concept - docs/reviews/blue-team-audit-v0.7.0.md
- [[docsreviewsred-team-report-v0.7.0]] - concept - docs/reviews/red-team-report-v0.7.0.md
- [[encoding_detector.py]] - code - gateway/security/encoding_detector.py
- [[prompt_protection.py]] - code - gateway/security/prompt_protection.py
- [[scanner()]] - code - gateway/tests/test_tool_result_injection.py
- [[skillsREADME]] - document - skills/README.md
- [[strip_markdown_exfil()]] - code - gateway/security/input_normalizer.py
- [[test_tool_injection_scan.py]] - code - gateway/tests/test_tool_injection_scan.py
- [[test_tool_result_injection.py]] - code - gateway/tests/test_tool_result_injection.py
- [[tool_result_injection.py]] - code - gateway/security/tool_result_injection.py
- [[xml_leak_filter.py]] - code - gateway/security/xml_leak_filter.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/InjectionAction
SORT file.name ASC
```

## Connections to other communities
- 21 edges to [[_COMMUNITY_MiddlewareManager]]
- 13 edges to [[_COMMUNITY_AuditChain]]
- 7 edges to [[_COMMUNITY_PIIConfig]]
- 5 edges to [[_COMMUNITY_TestToolChainAnalyzer]]
- 3 edges to [[_COMMUNITY_Action]]
- 3 edges to [[_COMMUNITY_agentshroud-blueteamSKILL]]
- 3 edges to [[_COMMUNITY_FR3 System Integrity]]
- 2 edges to [[_COMMUNITY_KillSwitchMonitor]]
- 2 edges to [[_COMMUNITY_gatewayingest_apimain.py (hermes-dashboard HTTP + WebSocket reverse proxy)]]
- 2 edges to [[_COMMUNITY_TelegramAPIProxy_2]]
- 2 edges to [[_COMMUNITY_AuditStore]]
- 2 edges to [[_COMMUNITY_ApprovalQueueConfig_2]]
- 2 edges to [[_COMMUNITY_KeyRotationManager_2]]
- 2 edges to [[_COMMUNITY_MultiTurnTracker]]
- 2 edges to [[_COMMUNITY_agentshroud-blueteamSKILL_1]]
- 2 edges to [[_COMMUNITY_ToolResultSanitizer]]
- 2 edges to [[_COMMUNITY_ApprovalHardening]]
- 2 edges to [[_COMMUNITY_dot-_filter_outbound]]
- 2 edges to [[_COMMUNITY_agentshroud-blueteamSKILL_6]]
- 2 edges to [[_COMMUNITY_ApprovalQueueConfig]]
- 2 edges to [[_COMMUNITY_MiddlewareManager_2]]
- 1 edge to [[_COMMUNITY_MiddlewareManager_4]]
- 1 edge to [[_COMMUNITY_agentshroud-blueteamSKILL_2]]
- 1 edge to [[_COMMUNITY_DifferentialPIIDetector]]
- 1 edge to [[_COMMUNITY_telegram_proxy.py_1]]
- 1 edge to [[_COMMUNITY_AgentShroud Blue Team Security Auditor_3]]
- 1 edge to [[_COMMUNITY_AgentShroud Security Verification (13-check driver)]]

## Top bridge nodes
- [[AgentShroud Blue Team Security Auditor (SEC-DEFENSE)]] - degree 27, connects to 16 communities
- [[agentshroud-blueteamSKILL]] - degree 29, connects to 15 communities
- [[tool_result_injection.py]] - degree 12, connects to 5 communities
- [[encoding_detector.py]] - degree 8, connects to 3 communities
- [[strip_markdown_exfil()]] - degree 7, connects to 3 communities
