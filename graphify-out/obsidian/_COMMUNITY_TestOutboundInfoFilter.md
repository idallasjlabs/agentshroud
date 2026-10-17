---
type: community
members: 57
---

# TestOutboundInfoFilter

**Members:** 57 nodes

## Members
- [[dot-__init__()_197]] - code - gateway/security/outbound_filter.py
- [[dot-_classify_response_risk()]] - code - gateway/security/outbound_filter.py
- [[dot-_compile_patterns()_1]] - code - gateway/security/outbound_filter.py
- [[dot-_has_fabricated_match()]] - code - gateway/tests/test_outbound_filter.py
- [[dot-_is_allowed_for_trust()]] - code - gateway/security/outbound_filter.py
- [[dot-filter_response()_2]] - code - gateway/security/outbound_filter.py
- [[dot-get_stats()_19]] - code - gateway/security/outbound_filter.py
- [[dot-setup_method()_38]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_blocked_unauthorized_command()]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_blocking_suspicious_code_execution()]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_case_insensitive()_3]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_category_is_operational()]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_continues_blocking()]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_exact_past_tense()]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_flagging_form()]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_legitimate_responses_not_matched()]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_outbound_filter_still_escalates_fabricated_notice()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_possessive_flagging()]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_present_tense()]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_prevents_form()]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_progressive_tense()]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_real_world_agent_responses()]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_redaction_applied()]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_with_pii_sanitizer_compatibility()]] - code - gateway/tests/test_outbound_filter.py
- [[A single match found by the outbound filter.]] - rationale - gateway/security/outbound_filter.py
- [[Any_82]] - code - gateway/security/outbound_filter.py
- [[Categories of information that may need filtering.]] - rationale - gateway/security/outbound_filter.py
- [[Check if a disclosure category is permitted for the user's trust level.]] - rationale - gateway/security/outbound_filter.py
- [[Classify the risk level of a response based on info disclosure density.]] - rationale - gateway/security/outbound_filter.py
- [[Compile all filter patterns into regex objects.]] - rationale - gateway/security/outbound_filter.py
- [[Filter agent response for sensitive information disclosure.          Args]] - rationale - gateway/security/outbound_filter.py
- [[FilterMatch]] - code - gateway/security/outbound_filter.py
- [[Get filter statistics.]] - rationale - gateway/security/outbound_filter.py
- [[InfoCategory]] - code - gateway/security/outbound_filter.py
- [[Initialize the outbound information filter.          Args             config C]] - rationale - gateway/security/outbound_filter.py
- [[Integration tests with other security components.]] - rationale - gateway/tests/test_outbound_filter.py
- [[Main outbound information filtering engine.      Uses compiled regex patterns to]] - rationale - gateway/security/outbound_filter.py
- [[Matched text is replaced with RESPONSE_FILTERED.]] - rationale - gateway/tests/test_outbound_filter.py
- [[Normal helpful responses must NOT trigger the pattern.]] - rationale - gateway/tests/test_outbound_filter.py
- [[Original pattern exact past-tense form.]] - rationale - gateway/tests/test_outbound_filter.py
- [[Outbound Information Filter Tests]] - code - gateway/tests/test_outbound_filter.py
- [[OutboundInfoFilter]] - code - gateway/security/outbound_filter.py
- [[Pattern is case-insensitive.]] - rationale - gateway/tests/test_outbound_filter.py
- [[Pattern is in the OPERATIONAL category.]] - rationale - gateway/tests/test_outbound_filter.py
- [[Possessive form AGENTSHROUD's behavioral analysis flagging.]] - rationale - gateway/tests/test_outbound_filter.py
- [[Standalone 'blocked unauthorized command execution' without AGENTSHROUD prefix.]] - rationale - gateway/tests/test_outbound_filter.py
- [[Test cases for the widened fabricated_security_notice pattern.]] - rationale - gateway/tests/test_outbound_filter.py
- [[Test that outbound filter works alongside PII sanitizer.]] - rationale - gateway/tests/test_outbound_filter.py
- [[Test with realistic agent response patterns.]] - rationale - gateway/tests/test_outbound_filter.py
- [[TestFabricatedSecurityNotice]] - code - gateway/tests/test_outbound_filter.py
- [[TestIntegration_1]] - code - gateway/tests/test_outbound_filter.py
- [[blocking suspicious code execution' variant.]] - rationale - gateway/tests/test_outbound_filter.py
- [[blocking' continuous form.]] - rationale - gateway/tests/test_outbound_filter.py
- [[continues blocking' — adverb + gerund form.]] - rationale - gateway/tests/test_outbound_filter.py
- [[flagging' gerund form.]] - rationale - gateway/tests/test_outbound_filter.py
- [[outbound_filter.py]] - code - gateway/security/outbound_filter.py
- [[test_outbound_filter.py]] - code - gateway/tests/test_outbound_filter.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestOutboundInfoFilter
SORT file.name ASC
```

## Connections to other communities
- 14 edges to [[_COMMUNITY_AuditChain]]
- 3 edges to [[_COMMUNITY_TestOutboundInfoFilter (2)]]
- 3 edges to [[_COMMUNITY_PipelineAction]]
- 2 edges to [[_COMMUNITY_AlertDispatcher]]
- 2 edges to [[_COMMUNITY_TestToolChainAnalyzer]]
- 2 edges to [[_COMMUNITY_AgentRegistry]]
- 2 edges to [[_COMMUNITY_MiddlewareManager (2)]]
- 1 edge to [[_COMMUNITY_TestOutboundInfoFilter (26)]]
- 1 edge to [[_COMMUNITY_TestOutboundInfoFilter (31)]]
- 1 edge to [[_COMMUNITY_TestOutboundInfoFilter (32)]]
- 1 edge to [[_COMMUNITY_TestOutboundInfoFilter (34)]]
- 1 edge to [[_COMMUNITY_TestOutboundInfoFilter (39)]]
- 1 edge to [[_COMMUNITY_AsyncMock]]
- 1 edge to [[_COMMUNITY_agentshroud-blueteamSKILL.md (3)]]
- 1 edge to [[_COMMUNITY_AlertDispatcher (3)]]

## Top bridge nodes
- [[OutboundInfoFilter]] - degree 38, connects to 9 communities
- [[outbound_filter.py]] - degree 9, connects to 5 communities
- [[dot-test_outbound_filter_still_escalates_fabricated_notice()]] - degree 4, connects to 3 communities
- [[InfoCategory]] - degree 9, connects to 2 communities
- [[dot-filter_response()_2]] - degree 6, connects to 1 community
