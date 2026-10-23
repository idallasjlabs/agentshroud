---
type: community
cohesion: 0.05
members: 54
---

# agentshroud-blueteam/SKILL.md (2)

**Cohesion:** 0.05 - loosely connected
**Members:** 54 nodes

## Members
- [[dot-__init__()_38]] - code - gateway/security/outbound_filter.py
- [[dot-_classify_response_risk()]] - code - gateway/security/outbound_filter.py
- [[dot-_compile_patterns()_1]] - code - gateway/security/outbound_filter.py
- [[dot-_has_fabricated_match()]] - code - gateway/tests/test_outbound_filter.py
- [[dot-_is_allowed_for_trust()]] - code - gateway/security/outbound_filter.py
- [[dot-filter_response()]] - code - gateway/security/outbound_filter.py
- [[dot-get_stats()_2]] - code - gateway/security/outbound_filter.py
- [[dot-setup_method()_3]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_blocked_unauthorized_command()]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_blocking_suspicious_code_execution()]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_case_insensitive()_1]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_category_is_operational()]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_continues_blocking()]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_exact_past_tense()]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_flagging_form()]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_legitimate_responses_not_matched()]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_possessive_flagging()]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_present_tense()]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_prevents_form()]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_progressive_tense()]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_real_world_agent_responses()]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_redaction_applied()]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_with_pii_sanitizer_compatibility()]] - code - gateway/tests/test_outbound_filter.py
- [[A single match found by the outbound filter.]] - rationale - gateway/security/outbound_filter.py
- [[Any_11]] - code - gateway/security/outbound_filter.py
- [[Categories of information that may need filtering.]] - rationale - gateway/security/outbound_filter.py
- [[Check if a disclosure category is permitted for the user's trust level.]] - rationale - gateway/security/outbound_filter.py
- [[Classify the risk level of a response based on info disclosure density.]] - rationale - gateway/security/outbound_filter.py
- [[Compile all filter patterns into regex objects.]] - rationale - gateway/security/outbound_filter.py
- [[FR4 Data Confidentiality]] - concept - docs/compliance/iec-62443-matrix.md
- [[Filter agent response for sensitive information disclosure.          Args]] - rationale - gateway/security/outbound_filter.py
- [[FilterMatch]] - code - gateway/security/outbound_filter.py
- [[Get filter statistics.]] - rationale - gateway/security/outbound_filter.py
- [[InfoCategory]] - code - gateway/security/outbound_filter.py
- [[Initialize the outbound information filter.          Args             config C]] - rationale - gateway/security/outbound_filter.py
- [[Integration tests with other security components.]] - rationale - gateway/tests/test_outbound_filter.py
- [[Matched text is replaced with RESPONSE_FILTERED.]] - rationale - gateway/tests/test_outbound_filter.py
- [[Normal helpful responses must NOT trigger the pattern.]] - rationale - gateway/tests/test_outbound_filter.py
- [[Original pattern exact past-tense form.]] - rationale - gateway/tests/test_outbound_filter.py
- [[Pattern is case-insensitive.]] - rationale - gateway/tests/test_outbound_filter.py
- [[Pattern is in the OPERATIONAL category.]] - rationale - gateway/tests/test_outbound_filter.py
- [[Possessive form AGENTSHROUD's behavioral analysis flagging.]] - rationale - gateway/tests/test_outbound_filter.py
- [[Standalone 'blocked unauthorized command execution' without AGENTSHROUD prefix.]] - rationale - gateway/tests/test_outbound_filter.py
- [[Test cases for the widened fabricated_security_notice pattern.]] - rationale - gateway/tests/test_outbound_filter.py
- [[Test that outbound filter works alongside PII sanitizer.]] - rationale - gateway/tests/test_outbound_filter.py
- [[Test with realistic agent response patterns.]] - rationale - gateway/tests/test_outbound_filter.py
- [[TestFabricatedSecurityNotice]] - code - gateway/tests/test_outbound_filter.py
- [[TestIntegration]] - code - gateway/tests/test_outbound_filter.py
- [[blocking suspicious code execution' variant.]] - rationale - gateway/tests/test_outbound_filter.py
- [[blocking' continuous form.]] - rationale - gateway/tests/test_outbound_filter.py
- [[continues blocking' — adverb + gerund form.]] - rationale - gateway/tests/test_outbound_filter.py
- [[flagging' gerund form.]] - rationale - gateway/tests/test_outbound_filter.py
- [[outbound_filter.py]] - code - gateway/security/outbound_filter.py
- [[test_outbound_filter.py]] - code - gateway/tests/test_outbound_filter.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/agentshroud-blueteam/SKILLmd_2
SORT file.name ASC
```

## Connections to other communities
- 13 edges to [[_COMMUNITY_KeyVaultConfig]]
- 2 edges to [[_COMMUNITY_Enum]]
- 2 edges to [[_COMMUNITY_SecurityPipeline (2)]]
- 2 edges to [[_COMMUNITY_FetchOutcome]]
- 2 edges to [[_COMMUNITY_IEC 62443 Compliance Matrix — AgentShroud]]
- 1 edge to [[_COMMUNITY_KeyVault]]
- 1 edge to [[_COMMUNITY_AgentTarget (2)]]
- 1 edge to [[_COMMUNITY_FileSandbox]]
- 1 edge to [[_COMMUNITY_openclawskillsi-crSKILL]]
- 1 edge to [[_COMMUNITY_Distributed OpenClaw Node Architecture — Raspberry Pi 4]]
- 1 edge to [[_COMMUNITY_PHASE_3A_3B_IMPLEMENTATION]]

## Top bridge nodes
- [[FR4 Data Confidentiality]] - degree 8, connects to 6 communities
- [[outbound_filter.py]] - degree 7, connects to 4 communities
- [[InfoCategory]] - degree 9, connects to 2 communities
- [[dot-filter_response()]] - degree 6, connects to 2 communities
- [[test_outbound_filter.py]] - degree 5, connects to 2 communities
