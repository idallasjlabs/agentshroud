---
type: community
cohesion: 0.09
members: 24
---

# Module Group 198

**Cohesion:** 0.09 - loosely connected
**Members:** 24 nodes

## Members
- [[.__init__()_81]] - code - gateway/security/outbound_filter.py
- [[._compile_patterns()_1]] - code - gateway/security/outbound_filter.py
- [[.get_stats()_16]] - code - gateway/security/outbound_filter.py
- [[.setup_method()_15]] - code - gateway/tests/test_outbound_filter.py
- [[.setup_method()_14]] - code - gateway/tests/test_outbound_filter.py
- [[.test_custom_patterns()]] - code - gateway/tests/test_outbound_filter.py
- [[.test_initialization_with_config()]] - code - gateway/tests/test_outbound_filter.py
- [[.test_monitor_mode()]] - code - gateway/tests/test_outbound_filter.py
- [[.test_real_world_agent_responses()]] - code - gateway/tests/test_outbound_filter.py
- [[.test_trust_level_overrides()]] - code - gateway/tests/test_outbound_filter.py
- [[.test_with_pii_sanitizer_compatibility()]] - code - gateway/tests/test_outbound_filter.py
- [[Any_46]] - code - gateway/security/outbound_filter.py
- [[Compile all filter patterns into regex objects.]] - rationale - gateway/security/outbound_filter.py
- [[Get filter statistics.]] - rationale - gateway/security/outbound_filter.py
- [[Initialize the outbound information filter.          Args             config C]] - rationale - gateway/security/outbound_filter.py
- [[Main outbound information filtering engine.      Uses compiled regex patterns to]] - rationale - gateway/security/outbound_filter.py
- [[OutboundInfoFilter]] - code - gateway/security/outbound_filter.py
- [[Set up test fixtures.]] - rationale - gateway/tests/test_outbound_filter.py
- [[Test adding custom filter patterns.]] - rationale - gateway/tests/test_outbound_filter.py
- [[Test filter initializes with custom configuration.]] - rationale - gateway/tests/test_outbound_filter.py
- [[Test that monitor mode logs but doesn't redact.]] - rationale - gateway/tests/test_outbound_filter.py
- [[Test that outbound filter works alongside PII sanitizer.]] - rationale - gateway/tests/test_outbound_filter.py
- [[Test that trust level overrides work correctly.]] - rationale - gateway/tests/test_outbound_filter.py
- [[Test with realistic agent response patterns.]] - rationale - gateway/tests/test_outbound_filter.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_198
SORT file.name ASC
```

## Connections to other communities
- 9 edges to [[_COMMUNITY_Module Group 282]]
- 6 edges to [[_COMMUNITY_Module Group 81]]
- 2 edges to [[_COMMUNITY_Gateway Config & Lifespan]]
- 2 edges to [[_COMMUNITY_Module Group 181]]
- 1 edge to [[_COMMUNITY_CLI & Core Gateway Routes]]

## Top bridge nodes
- [[OutboundInfoFilter]] - degree 23, connects to 5 communities
- [[.__init__()_81]] - degree 5, connects to 1 community
- [[.test_real_world_agent_responses()]] - degree 3, connects to 1 community
- [[.test_with_pii_sanitizer_compatibility()]] - degree 3, connects to 1 community
- [[.setup_method()_14]] - degree 3, connects to 1 community