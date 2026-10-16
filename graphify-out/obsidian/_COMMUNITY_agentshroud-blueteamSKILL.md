---
type: community
cohesion: 0.02
members: 103
---

# agentshroud-blueteam/SKILL.md

**Cohesion:** 0.02 - loosely connected
**Members:** 103 nodes

## Members
- [[dot-__init__()_114]] - code - gateway/security/canary_tripwire.py
- [[dot-__init__()_115]] - code - gateway/security/prompt_protection.py
- [[dot-_calculate_similarity()]] - code - gateway/security/prompt_protection.py
- [[dot-_compile_detection_patterns()]] - code - gateway/security/prompt_protection.py
- [[dot-_load_protected_content()]] - code - gateway/security/prompt_protection.py
- [[dot-_redact_fuzzy_match()]] - code - gateway/security/prompt_protection.py
- [[dot-_redact_match()]] - code - gateway/security/prompt_protection.py
- [[dot-add_protected_content()]] - code - gateway/security/prompt_protection.py
- [[dot-filter_response()_2]] - code - gateway/security/xml_leak_filter.py
- [[dot-get_protection_stats()]] - code - gateway/security/prompt_protection.py
- [[dot-register_bot_hostnames()]] - code - gateway/security/prompt_protection.py
- [[dot-scan_command_injection()]] - code - gateway/security/xml_leak_filter.py
- [[dot-scan_response()_2]] - code - gateway/security/prompt_protection.py
- [[dot-setup_method()_20]] - code - gateway/tests/test_canary_tripwire.py
- [[dot-setup_method()_21]] - code - gateway/tests/test_xml_leak_filter.py
- [[dot-test_api_key_canary()]] - code - gateway/tests/test_canary_tripwire.py
- [[dot-test_base64_canary()]] - code - gateway/tests/test_canary_tripwire.py
- [[dot-test_case_insensitive()_3]] - code - gateway/tests/test_canary_tripwire.py
- [[dot-test_clean_response_passes_through()]] - code - gateway/tests/test_xml_leak_filter.py
- [[dot-test_clean_text_passes()]] - code - gateway/tests/test_xml_leak_filter.py
- [[dot-test_code_word_canary()]] - code - gateway/tests/test_canary_tripwire.py
- [[dot-test_counter_increments()]] - code - gateway/tests/test_canary_tripwire.py
- [[dot-test_custom_config()_2]] - code - gateway/tests/test_canary_tripwire.py
- [[dot-test_empty_input()_2]] - code - gateway/tests/test_canary_tripwire.py
- [[dot-test_empty_text_returns_clean()]] - code - gateway/tests/test_xml_leak_filter.py
- [[dot-test_file_path_removal()]] - code - gateway/tests/test_xml_leak_filter.py
- [[dot-test_function_calls_xml_removal()]] - code - gateway/tests/test_xml_leak_filter.py
- [[dot-test_no_canaries()]] - code - gateway/tests/test_canary_tripwire.py
- [[dot-test_normal_content_passes()]] - code - gateway/tests/test_canary_tripwire.py
- [[dot-test_plain_canary_detected()]] - code - gateway/tests/test_canary_tripwire.py
- [[dot-test_python_eval_detected()]] - code - gateway/tests/test_xml_leak_filter.py
- [[dot-test_quick_function_calls_filter()]] - code - gateway/tests/test_xml_leak_filter.py
- [[dot-test_reversed_canary()]] - code - gateway/tests/test_canary_tripwire.py
- [[dot-test_rot13_canary()]] - code - gateway/tests/test_canary_tripwire.py
- [[dot-test_scan_response_blocks_on_canary()]] - code - gateway/tests/test_canary_tripwire.py
- [[dot-test_scan_response_no_block_when_block_disabled()]] - code - gateway/tests/test_canary_tripwire.py
- [[dot-test_scan_response_passes_clean_text()]] - code - gateway/tests/test_canary_tripwire.py
- [[dot-test_scan_response_records_scan_method()]] - code - gateway/tests/test_canary_tripwire.py
- [[dot-test_scan_response_returns_tripwire_response()]] - code - gateway/tests/test_canary_tripwire.py
- [[dot-test_shell_injection_detected()]] - code - gateway/tests/test_xml_leak_filter.py
- [[dot-test_spaced_canary()]] - code - gateway/tests/test_canary_tripwire.py
- [[dot-test_sql_injection_detected()]] - code - gateway/tests/test_xml_leak_filter.py
- [[dot-test_url_encoded_canary()]] - code - gateway/tests/test_canary_tripwire.py
- [[dot-test_zero_width_bypass()]] - code - gateway/tests/test_canary_tripwire.py
- [[dot-xml_filter()]] - code - gateway/tests/test_xml_leak_filter.py
- [[A piece of content that should be protected from disclosure.]] - rationale - gateway/security/prompt_protection.py
- [[Add bot container hostnames to the infrastructure detection patterns.          C]] - rationale - gateway/security/prompt_protection.py
- [[Add content to the protected registry.          Args             name Identifi]] - rationale - gateway/security/prompt_protection.py
- [[AgentShroud Blue Team Security Auditor (SEC-DEFENSE)]] - document - .agents/skills/i-sec-defense/SKILL.md
- [[AgentShroud Module Inventory (Blue Team)]] - document - skills/custom/agentshroud-blueteam/references/module-inventory.md
- [[AgentShroud Module Inventory (Red Team)]] - document - skills/custom/agentshroud-redteam/references/module-inventory.md
- [[AgentShroud Red Team Adversarial Tester (SEC-OFFENSE)]] - document - .agents/skills/i-sec-offense/SKILL.md
- [[Any_46]] - code - gateway/security/prompt_protection.py
- [[Blue Team Security Auditor README]] - document - .agents/skills/i-sec-defense/README.md
- [[Bridge result returned by scan_response() for pipeline compatibility.]] - rationale - gateway/security/canary_tripwire.py
- [[CVE-2026-34425 — Preflight Validation Bypass (Shell-Bleed)]] - rationale - docs/security/cve-mitigation-matrix.md
- [[Calculate similarity between text and protected content.]] - rationale - gateway/security/prompt_protection.py
- [[CanaryConfig_1]] - code - gateway/security/canary_tripwire.py
- [[Compile regex patterns for detecting disclosure attempts.]] - rationale - gateway/security/prompt_protection.py
- [[Enterprise Security Feature Priorities (Steve Hay Assessment, Red Team copy)]] - document - skills/custom/agentshroud-redteam/references/steve-hay-assessment.md
- [[Filter outbound response content to remove sensitive information.          Args]] - rationale - gateway/security/xml_leak_filter.py
- [[FilterResult_1]] - code - gateway/security/xml_leak_filter.py
- [[Get statistics about the protection system.]] - rationale - gateway/security/prompt_protection.py
- [[Initialize prompt protection system.          Args             config Configur]] - rationale - gateway/security/prompt_protection.py
- [[Load protected content from configured sources.]] - rationale - gateway/security/prompt_protection.py
- [[Main system prompt protection engine.      Maintains fingerprints of sensitive c]] - rationale - gateway/security/prompt_protection.py
- [[Match]] - code - gateway/security/prompt_protection.py
- [[Module Coverage Heat Map Legend (EMAC—)]] - concept - skills/custom/agentshroud-blueteam/SKILL.md
- [[PromptProtection]] - code - gateway/security/prompt_protection.py
- [[ProtectedContent]] - code - gateway/security/prompt_protection.py
- [[Red Team Adversarial Tester README]] - document - .agents/skills/i-sec-offense/README.md
- [[Red Team Assessment Plan (Steve Hay Plan, Red Team copy)]] - document - skills/custom/agentshroud-redteam/references/steve-hay-plan.md
- [[Redact text that fuzzy matches protected content.]] - rationale - gateway/security/prompt_protection.py
- [[RedactionResult_1]] - code - gateway/security/prompt_protection.py
- [[Replace a regex match with a redaction placeholder.]] - rationale - gateway/security/prompt_protection.py
- [[Result from XML leak filtering.]] - rationale - gateway/security/xml_leak_filter.py
- [[Result of scanning and redacting content.]] - rationale - gateway/security/prompt_protection.py
- [[STPA-Sec Loss Categories (L-1 Data Disclosure, L-2 Unauthorized Actions, L-3 Agent Integrity, L-4 Audit Integrity)]] - concept - skills/custom/agentshroud-blueteam/references/steve-hay-assessment.md
- [[STPA-Sec Methodology]] - concept - .agents/skills/i-sec-defense/SKILL.md
- [[STPA-Sec Methodology_1]] - concept - docker/config/openclaw/skills/i-sec-defense/SKILL.md
- [[Scan outbound text for command  code injection patterns.          Does NOT modi]] - rationale - gateway/security/xml_leak_filter.py
- [[Scan text for protected content and return redacted version.          Args]] - rationale - gateway/security/prompt_protection.py
- [[Set up test fixtures._3]] - rationale - gateway/tests/test_xml_leak_filter.py
- [[Steve Hay Adversary Model]] - concept - .agents/skills/i-sec-offense/SKILL.md
- [[System Prompt Protection Tests]] - code - gateway/tests/test_prompt_protection.py
- [[Test cases for XMLLeakFilter.]] - rationale - gateway/tests/test_xml_leak_filter.py
- [[Test removal of file paths from responses.]] - rationale - gateway/tests/test_xml_leak_filter.py
- [[Test removal of function call XML blocks.]] - rationale - gateway/tests/test_xml_leak_filter.py
- [[Test that clean responses pass through unchanged.]] - rationale - gateway/tests/test_xml_leak_filter.py
- [[Test the performance-optimized function calls only filter.]] - rationale - gateway/tests/test_xml_leak_filter.py
- [[TestCanaryTripwire]] - code - gateway/tests/test_canary_tripwire.py
- [[TestCommandInjectionScan]] - code - gateway/tests/test_xml_leak_filter.py
- [[TestXMLLeakFilter]] - code - gateway/tests/test_xml_leak_filter.py
- [[TripwireResponse]] - code - gateway/security/canary_tripwire.py
- [[Unsafe Control Actions (UCA-1 through UCA-17)]] - concept - skills/custom/agentshroud-blueteam/references/steve-hay-assessment.md
- [[agentshroud-blueteamSKILL]] - document - skills/custom/agentshroud-blueteam/SKILL.md
- [[canary_tripwire.py]] - code - gateway/security/canary_tripwire.py
- [[docsreviewsblue-team-audit-v0.7.0]] - concept - docs/reviews/blue-team-audit-v0.7.0.md
- [[docsreviewsred-team-report-v0.7.0]] - concept - docs/reviews/red-team-report-v0.7.0.md
- [[prompt_protection.py]] - code - gateway/security/prompt_protection.py
- [[test_canary_tripwire.py]] - code - gateway/tests/test_canary_tripwire.py
- [[test_xml_leak_filter.py]] - code - gateway/tests/test_xml_leak_filter.py
- [[xml_leak_filter.py]] - code - gateway/security/xml_leak_filter.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/agentshroud-blueteam/SKILLmd
SORT file.name ASC
```

## Connections to other communities
- 18 edges to [[_COMMUNITY_MiddlewareManager]]
- 12 edges to [[_COMMUNITY_PIIConfig]]
- 5 edges to [[_COMMUNITY_TestPromptProtection]]
- 3 edges to [[_COMMUNITY_OutboundInfoFilter]]
- 3 edges to [[_COMMUNITY_lifespan.py]]
- 3 edges to [[_COMMUNITY_Action]]
- 2 edges to [[_COMMUNITY_gatewayingest_apimain.py (hermes-dashboard HTTP + WebSocket reverse proxy)]]
- 2 edges to [[_COMMUNITY_dot-analyze_message]]
- 2 edges to [[_COMMUNITY_Enum]]
- 2 edges to [[_COMMUNITY_load_config]]
- 2 edges to [[_COMMUNITY_KillSwitchMonitor]]
- 2 edges to [[_COMMUNITY_KeyRotationConfig]]
- 2 edges to [[_COMMUNITY_tool_chain_analyzer.py]]
- 2 edges to [[_COMMUNITY_ApprovalHardening]]
- 2 edges to [[_COMMUNITY_ApprovalQueueConfig]]
- 2 edges to [[_COMMUNITY_AuditStore]]
- 2 edges to [[_COMMUNITY_ToolResultSanitizer]]
- 1 edge to [[_COMMUNITY_test_redteam_probes.py]]
- 1 edge to [[_COMMUNITY_AgentShroud Skills Library]]
- 1 edge to [[_COMMUNITY_AgentShroud Blue Team Security Auditor_3]]
- 1 edge to [[_COMMUNITY_FR3 System Integrity]]
- 1 edge to [[_COMMUNITY_dockerscriptssecurity-scan.sh]]
- 1 edge to [[_COMMUNITY_AgentShroud Security Verification (13-check driver)]]

## Top bridge nodes
- [[agentshroud-blueteamSKILL]] - degree 29, connects to 18 communities
- [[AgentShroud Blue Team Security Auditor (SEC-DEFENSE)]] - degree 27, connects to 17 communities
- [[PromptProtection]] - degree 23, connects to 4 communities
- [[AgentShroud Red Team Adversarial Tester (SEC-OFFENSE)]] - degree 7, connects to 2 communities
- [[TestCanaryTripwire]] - degree 25, connects to 1 community
