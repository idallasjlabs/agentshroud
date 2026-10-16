---
type: community
cohesion: 0.08
members: 36
---

# TestFabricatedSecurityNotice

**Cohesion:** 0.08 - loosely connected
**Members:** 36 nodes

## Members
- [[dot-_has_fabricated_match()]] - code - gateway/tests/test_outbound_filter.py
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
- [[Categories of information that may need filtering.]] - rationale - gateway/security/outbound_filter.py
- [[InfoCategory]] - code - gateway/security/outbound_filter.py
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
- [[test_outbound_filter.py]] - code - gateway/tests/test_outbound_filter.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestFabricatedSecurityNotice
SORT file.name ASC
```

## Connections to other communities
- 9 edges to [[_COMMUNITY_OutboundInfoFilter]]
- 2 edges to [[_COMMUNITY_TestOutboundInfoFilter]]
- 1 edge to [[_COMMUNITY_Enum]]

## Top bridge nodes
- [[InfoCategory]] - degree 9, connects to 3 communities
- [[test_outbound_filter.py]] - degree 5, connects to 2 communities
- [[TestFabricatedSecurityNotice]] - degree 19, connects to 1 community
- [[TestIntegration]] - degree 6, connects to 1 community
- [[dot-test_real_world_agent_responses()]] - degree 3, connects to 1 community
