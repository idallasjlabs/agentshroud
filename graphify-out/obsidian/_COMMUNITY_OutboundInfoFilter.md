---
type: community
members: 36
---

# OutboundInfoFilter

**Members:** 36 nodes

## Members
- [[dot-__init__()_121]] - code - gateway/security/outbound_filter.py
- [[dot-_classify_response_risk()]] - code - gateway/security/outbound_filter.py
- [[dot-_compile_patterns()]] - code - gateway/security/outbound_filter.py
- [[dot-_is_allowed_for_trust()]] - code - gateway/security/outbound_filter.py
- [[dot-filter_response()_2]] - code - gateway/security/outbound_filter.py
- [[dot-get_stats()_8]] - code - gateway/security/outbound_filter.py
- [[dot-setup_method()_22]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_outbound_filter_still_escalates_fabricated_notice()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_real_world_agent_responses()]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_with_pii_sanitizer_compatibility()]] - code - gateway/tests/test_outbound_filter.py
- [[A single match found by the outbound filter.]] - rationale - gateway/security/outbound_filter.py
- [[Any_42]] - code
- [[Categories of information that may need filtering.]] - rationale - gateway/security/outbound_filter.py
- [[Check if a disclosure category is permitted for the user's trust level. Default…]] - rationale - gateway/security/outbound_filter.py
- [[Classify the risk level of a response based on info disclosure density.]] - rationale - gateway/security/outbound_filter.py
- [[Compile all filter patterns into regex objects.]] - rationale - gateway/security/outbound_filter.py
- [[Comprehensive tests for the Outbound Information Filter Tests all filtering…]] - rationale - gateway/tests/test_outbound_filter.py
- [[Enum_31]] - code
- [[Filter agent response for sensitive information disclosure. Args…]] - rationale - gateway/security/outbound_filter.py
- [[FilterMatch]] - code - gateway/security/outbound_filter.py
- [[FilterResult_1]] - code - gateway/security/outbound_filter.py
- [[Get filter statistics.]] - rationale - gateway/security/outbound_filter.py
- [[InfoCategory]] - code - gateway/security/outbound_filter.py
- [[Initialize the outbound information filter. Args config Configuration…]] - rationale - gateway/security/outbound_filter.py
- [[Integration tests with other security components.]] - rationale - gateway/tests/test_outbound_filter.py
- [[Main outbound information filtering engine. Uses compiled regex patterns to…]] - rationale - gateway/security/outbound_filter.py
- [[Outbound Information Filter for AgentShroud Gateway Prevents disclosure of…]] - rationale - gateway/security/outbound_filter.py
- [[OutboundInfoFilter]] - code - gateway/security/outbound_filter.py
- [[Regression filter_result was possibly-unbound in process_outbound when no…]] - rationale - gateway/tests/test_pipeline_unit.py
- [[Result of filtering agent response content.]] - rationale - gateway/security/outbound_filter.py
- [[Test that outbound filter works alongside PII sanitizer.]] - rationale - gateway/tests/test_outbound_filter.py
- [[Test with realistic agent response patterns.]] - rationale - gateway/tests/test_outbound_filter.py
- [[TestIntegration]] - code - gateway/tests/test_outbound_filter.py
- [[TestOutboundFilterResultBinding]] - code - gateway/tests/test_pipeline_unit.py
- [[outbound_filter.py]] - code - gateway/security/outbound_filter.py
- [[test_outbound_filter.py]] - code - gateway/tests/test_outbound_filter.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/OutboundInfoFilter
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_SecurityPipeline]]
- 4 edges to [[_COMMUNITY_TrustManager]]
- 4 edges to [[_COMMUNITY_TestFabricatedSecurityNotice]]
- 2 edges to [[_COMMUNITY_TestOutboundInfoFilter]]
- 2 edges to [[_COMMUNITY_lifespan.py]]
- 1 edge to [[_COMMUNITY_AsyncMock]]
- 1 edge to [[_COMMUNITY_PipelineAction]]
- 1 edge to [[_COMMUNITY_dot-setup_method_1]]
- 1 edge to [[_COMMUNITY_dot-test_custom_patterns]]
- 1 edge to [[_COMMUNITY_dot-test_initialization_with_config]]
- 1 edge to [[_COMMUNITY_dot-test_monitor_mode]]
- 1 edge to [[_COMMUNITY_dot-test_trust_level_overrides]]
- 1 edge to [[_COMMUNITY_lifespan]]

## Top bridge nodes
- [[OutboundInfoFilter]] - degree 25, connects to 10 communities
- [[TestOutboundFilterResultBinding]] - degree 8, connects to 3 communities
- [[outbound_filter.py]] - degree 9, connects to 2 communities
- [[test_outbound_filter.py]] - degree 7, connects to 2 communities
- [[FilterResult_1]] - degree 5, connects to 2 communities
