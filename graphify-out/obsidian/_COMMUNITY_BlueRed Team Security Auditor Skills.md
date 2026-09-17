---
type: community
cohesion: 0.03
members: 102
---

# Blue/Red Team Security Auditor Skills

**Cohesion:** 0.03 - loosely connected
**Members:** 102 nodes

## Members
- [[dot-__init__()_130]] - code - gateway/security/multi_turn_tracker.py
- [[dot-__init__()_131]] - code - gateway/security/xml_leak_filter.py
- [[dot-_add_disclosure_event()]] - code - gateway/security/multi_turn_tracker.py
- [[dot-_analyze_agent_response()]] - code - gateway/security/multi_turn_tracker.py
- [[dot-_analyze_user_message()]] - code - gateway/security/multi_turn_tracker.py
- [[dot-_check_thresholds()]] - code - gateway/security/multi_turn_tracker.py
- [[dot-_cleanup_old_sessions()]] - code - gateway/security/multi_turn_tracker.py
- [[dot-_compile_detection_patterns()]] - code - gateway/security/multi_turn_tracker.py
- [[dot-_normalize_query()]] - code - gateway/security/multi_turn_tracker.py
- [[dot-_score_message_patterns()]] - code - gateway/security/multi_turn_tracker.py
- [[dot-_score_response_patterns()]] - code - gateway/security/multi_turn_tracker.py
- [[dot-_trigger_alert()]] - code - gateway/security/multi_turn_tracker.py
- [[dot-filter_function_calls_only()]] - code - gateway/security/xml_leak_filter.py
- [[dot-filter_response()]] - code - gateway/security/xml_leak_filter.py
- [[dot-get_global_stats()]] - code - gateway/security/multi_turn_tracker.py
- [[dot-get_session_stats()]] - code - gateway/security/multi_turn_tracker.py
- [[dot-scan_command_injection()]] - code - gateway/security/xml_leak_filter.py
- [[dot-score_response_consistency()]] - code - gateway/security/multi_turn_tracker.py
- [[dot-setup_method()_29]] - code - gateway/tests/test_xml_leak_filter.py
- [[dot-test_clean_response_passes_through()]] - code - gateway/tests/test_xml_leak_filter.py
- [[dot-test_clean_text_passes()]] - code - gateway/tests/test_xml_leak_filter.py
- [[dot-test_empty_text_returns_clean()]] - code - gateway/tests/test_xml_leak_filter.py
- [[dot-test_file_path_removal()]] - code - gateway/tests/test_xml_leak_filter.py
- [[dot-test_function_calls_xml_removal()]] - code - gateway/tests/test_xml_leak_filter.py
- [[dot-test_python_eval_detected()]] - code - gateway/tests/test_xml_leak_filter.py
- [[dot-test_quick_function_calls_filter()]] - code - gateway/tests/test_xml_leak_filter.py
- [[dot-test_shell_injection_detected()]] - code - gateway/tests/test_xml_leak_filter.py
- [[dot-test_sql_injection_detected()]] - code - gateway/tests/test_xml_leak_filter.py
- [[dot-track_message()]] - code - gateway/security/multi_turn_tracker.py
- [[dot-xml_filter()]] - code - gateway/tests/test_xml_leak_filter.py
- [[A single disclosure event in a session.]] - rationale - gateway/security/multi_turn_tracker.py
- [[Add a disclosure event to the session.]] - rationale - gateway/security/multi_turn_tracker.py
- [[AgentShroud Blue Team Security Auditor (SEC-DEFENSE)]] - document - .agents/skills/i-sec-defense/SKILL.md
- [[AgentShroud Module Inventory (Blue Team)]] - document - skills/custom/agentshroud-blueteam/references/module-inventory.md
- [[AgentShroud Module Inventory (Red Team)]] - document - skills/custom/agentshroud-redteam/references/module-inventory.md
- [[AgentShroud Red Team Adversarial Tester (SEC-OFFENSE)]] - document - .agents/skills/i-sec-offense/SKILL.md
- [[AgentShroud Skills Library]] - document - skills/README.md
- [[Analyze agent response for potential information leaks.]] - rationale - gateway/security/multi_turn_tracker.py
- [[Analyze user message for disclosure patterns.]] - rationale - gateway/security/multi_turn_tracker.py
- [[Any_45]] - code - gateway/security/multi_turn_tracker.py
- [[Blue Team Security Auditor README]] - document - .agents/skills/i-sec-defense/README.md
- [[Check session score against thresholds and take action.]] - rationale - gateway/security/multi_turn_tracker.py
- [[Compile regex patterns for detecting disclosure categories.]] - rationale - gateway/security/multi_turn_tracker.py
- [[Compute a heuristic consistency score between query and response.          Retur]] - rationale - gateway/security/multi_turn_tracker.py
- [[Configuration for alert thresholds.]] - rationale - gateway/security/multi_turn_tracker.py
- [[ConsistencyScore]] - code - gateway/security/multi_turn_tracker.py
- [[Context tracking for a session.]] - rationale - gateway/security/context_guard.py
- [[Custom Skills]] - document - skills/README.md
- [[Directory Structure_1]] - document - skills/README.md
- [[DisclosureEvent]] - code - gateway/security/multi_turn_tracker.py
- [[Enterprise Security Feature Priorities (Steve Hay Assessment, Red Team copy)]] - document - skills/custom/agentshroud-redteam/references/steve-hay-assessment.md
- [[Filter outbound response content to remove sensitive information.          Args]] - rationale - gateway/security/xml_leak_filter.py
- [[Filter to remove sensitive XML and path information from outbound responses.]] - rationale - gateway/security/xml_leak_filter.py
- [[FilterResult_1]] - code - gateway/security/xml_leak_filter.py
- [[Get global tracking statistics.]] - rationale - gateway/security/multi_turn_tracker.py
- [[Get statistics for a session.]] - rationale - gateway/security/multi_turn_tracker.py
- [[Heuristic consistency score between a query and its response.]] - rationale - gateway/security/multi_turn_tracker.py
- [[Initialize the filter with predefined patterns.]] - rationale - gateway/security/xml_leak_filter.py
- [[Initialize the multi-turn tracker.          Args             config Configurat]] - rationale - gateway/security/multi_turn_tracker.py
- [[Module Coverage Heat Map Legend (EMAC—)]] - concept - skills/custom/agentshroud-blueteam/SKILL.md
- [[Normalize query for repeated query detection.]] - rationale - gateway/security/multi_turn_tracker.py
- [[OpenClaw Built-in Skills]] - document - skills/README.md
- [[Quick filter that only removes function call XML (for performance).          Arg]] - rationale - gateway/security/xml_leak_filter.py
- [[Red Team Adversarial Tester README]] - document - .agents/skills/i-sec-offense/README.md
- [[Red Team Assessment Plan (Steve Hay Plan, Red Team copy)]] - document - skills/custom/agentshroud-redteam/references/steve-hay-plan.md
- [[Remove old sessions to prevent memory bloat.]] - rationale - gateway/security/multi_turn_tracker.py
- [[Result from XML leak filtering.]] - rationale - gateway/security/xml_leak_filter.py
- [[STPA-Sec Loss Categories (L-1 Data Disclosure, L-2 Unauthorized Actions, L-3 Agent Integrity, L-4 Audit Integrity)]] - concept - skills/custom/agentshroud-blueteam/references/steve-hay-assessment.md
- [[STPA-Sec Methodology]] - concept - .agents/skills/i-sec-defense/SKILL.md
- [[STPA-Sec Methodology_1]] - concept - docker/config/openclaw/skills/i-sec-defense/SKILL.md
- [[Scan outbound text for command  code injection patterns.          Does NOT modi]] - rationale - gateway/security/xml_leak_filter.py
- [[Score agent response for potential leaks.]] - rationale - gateway/security/multi_turn_tracker.py
- [[Score message based on disclosure patterns.]] - rationale - gateway/security/multi_turn_tracker.py
- [[SessionContext_1]] - code - gateway/security/multi_turn_tracker.py
- [[Set up test fixtures._2]] - rationale - gateway/tests/test_xml_leak_filter.py
- [[Steve Hay Adversary Model]] - concept - .agents/skills/i-sec-offense/SKILL.md
- [[Test cases for XMLLeakFilter.]] - rationale - gateway/tests/test_xml_leak_filter.py
- [[Test removal of file paths from responses.]] - rationale - gateway/tests/test_xml_leak_filter.py
- [[Test removal of function call XML blocks.]] - rationale - gateway/tests/test_xml_leak_filter.py
- [[Test that clean responses pass through unchanged.]] - rationale - gateway/tests/test_xml_leak_filter.py
- [[Test the performance-optimized function calls only filter.]] - rationale - gateway/tests/test_xml_leak_filter.py
- [[TestCommandInjectionScan]] - code - gateway/tests/test_xml_leak_filter.py
- [[TestXMLLeakFilter]] - code - gateway/tests/test_xml_leak_filter.py
- [[ThresholdConfig]] - code - gateway/security/multi_turn_tracker.py
- [[ToolCheckResult]] - code - gateway/security/subagent_monitor.py
- [[Track a message and response pair for disclosure analysis.          Args]] - rationale - gateway/security/multi_turn_tracker.py
- [[Trigger alert callbacks.]] - rationale - gateway/security/multi_turn_tracker.py
- [[Unsafe Control Actions (UCA-1 through UCA-17)]] - concept - skills/custom/agentshroud-blueteam/references/steve-hay-assessment.md
- [[Usage_116]] - document - skills/README.md
- [[XMLLeakFilter]] - code - gateway/security/xml_leak_filter.py
- [[agentshroud-blueteamSKILL]] - document - skills/custom/agentshroud-blueteam/SKILL.md
- [[canary_tripwire.py]] - code - gateway/security/canary_tripwire.py
- [[docsreviewsblue-team-audit-v0.7.0]] - concept - docs/reviews/blue-team-audit-v0.7.0.md
- [[docsreviewsred-team-report-v0.7.0]] - concept - docs/reviews/red-team-report-v0.7.0.md
- [[encoding_detector.py]] - code - gateway/security/encoding_detector.py
- [[gateway.security.trust_manager]] - code - gateway/security/trust_manager.py
- [[multi_turn_tracker.py]] - code - gateway/security/multi_turn_tracker.py
- [[prompt_protection.py]] - code - gateway/security/prompt_protection.py
- [[skillsREADME]] - document - skills/README.md
- [[subagent_monitor.py]] - code - gateway/security/subagent_monitor.py
- [[test_xml_leak_filter.py]] - code - gateway/tests/test_xml_leak_filter.py
- [[xml_leak_filter.py]] - code - gateway/security/xml_leak_filter.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Blue/Red_Team_Security_Auditor_Skills
SORT file.name ASC
```

## Connections to other communities
- 36 edges to [[_COMMUNITY_Alert Dispatcher & RBAC Reliability]]
- 8 edges to [[_COMMUNITY_Canary Tripwire]]
- 6 edges to [[_COMMUNITY_Approval Routing & Event Bus]]
- 5 edges to [[_COMMUNITY_Voice Gateway STT & Browser Security]]
- 5 edges to [[_COMMUNITY_Ingest API & RBAC Core]]
- 5 edges to [[_COMMUNITY_Community 658]]
- 4 edges to [[_COMMUNITY_Cross-Bot Trust & A2A Governance]]
- 4 edges to [[_COMMUNITY_File Sandbox & Privilege Separation Tests]]
- 3 edges to [[_COMMUNITY_Community 52]]
- 2 edges to [[_COMMUNITY_Session Manager & PIIContext Guard]]
- 2 edges to [[_COMMUNITY_Community 101]]
- 2 edges to [[_COMMUNITY_Community 112]]
- 2 edges to [[_COMMUNITY_P3 Infrastructure Security Modules]]
- 2 edges to [[_COMMUNITY_Enhanced Approval Queue]]
- 2 edges to [[_COMMUNITY_PII Sanitizer & Redaction]]
- 2 edges to [[_COMMUNITY_Community 291]]
- 2 edges to [[_COMMUNITY_Community 903]]
- 2 edges to [[_COMMUNITY_Community 44]]
- 2 edges to [[_COMMUNITY_Community 42]]
- 1 edge to [[_COMMUNITY_Community 115]]
- 1 edge to [[_COMMUNITY_Proxy Sidecar & Forwarder]]
- 1 edge to [[_COMMUNITY_Community 56]]
- 1 edge to [[_COMMUNITY_Agent Isolation & Group Config Tests]]
- 1 edge to [[_COMMUNITY_Community 86]]
- 1 edge to [[_COMMUNITY_Community 565]]
- 1 edge to [[_COMMUNITY_Community 689]]
- 1 edge to [[_COMMUNITY_Memory Integrity & Lifecycle]]
- 1 edge to [[_COMMUNITY_Prompt Guard & Context Integrity]]
- 1 edge to [[_COMMUNITY_Community 731]]
- 1 edge to [[_COMMUNITY_Community 46]]
- 1 edge to [[_COMMUNITY_Community 793]]
- 1 edge to [[_COMMUNITY_Community 98]]
- 1 edge to [[_COMMUNITY_Community 535]]
- 1 edge to [[_COMMUNITY_Ingest Middleware & File Sandbox]]
- 1 edge to [[_COMMUNITY_Community 674]]
- 1 edge to [[_COMMUNITY_Community 632]]
- 1 edge to [[_COMMUNITY_Community 92]]
- 1 edge to [[_COMMUNITY_Community 673]]

## Top bridge nodes
- [[agentshroud-blueteamSKILL]] - degree 30, connects to 15 communities
- [[AgentShroud Blue Team Security Auditor (SEC-DEFENSE)]] - degree 29, connects to 15 communities
- [[gateway.security.trust_manager]] - degree 18, connects to 11 communities
- [[subagent_monitor.py]] - degree 12, connects to 7 communities
- [[XMLLeakFilter]] - degree 27, connects to 4 communities