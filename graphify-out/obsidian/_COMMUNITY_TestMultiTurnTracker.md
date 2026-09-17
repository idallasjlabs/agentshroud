---
type: community
cohesion: 0.04
members: 48
---

# TestMultiTurnTracker

**Cohesion:** 0.04 - loosely connected
**Members:** 48 nodes

## Members
- [[.test_agent_response_analysis()]] - code - gateway/tests/test_multi_turn_tracker.py
- [[.test_alert_callbacks()]] - code - gateway/tests/test_multi_turn_tracker.py
- [[.test_basic_message_tracking()]] - code - gateway/tests/test_multi_turn_tracker.py
- [[.test_blocked_session_behavior()]] - code - gateway/tests/test_multi_turn_tracker.py
- [[.test_credential_detection()]] - code - gateway/tests/test_multi_turn_tracker.py
- [[.test_cumulative_scoring()]] - code - gateway/tests/test_multi_turn_tracker.py
- [[.test_disabled_tracker()]] - code - gateway/tests/test_multi_turn_tracker.py
- [[.test_edge_cases()_1]] - code - gateway/tests/test_multi_turn_tracker.py
- [[.test_file_reference_detection()]] - code - gateway/tests/test_multi_turn_tracker.py
- [[.test_get_stats()_2]] - code - gateway/tests/test_path_isolation.py
- [[.test_global_stats()]] - code - gateway/tests/test_multi_turn_tracker.py
- [[.test_global_stats()_1]] - code - gateway/tests/test_tool_chain_analyzer.py
- [[.test_infrastructure_detection()]] - code - gateway/tests/test_multi_turn_tracker.py
- [[.test_initialization()_1]] - code - gateway/tests/test_multi_turn_tracker.py
- [[.test_pii_fragment_detection()]] - code - gateway/tests/test_multi_turn_tracker.py
- [[.test_repeated_query_detection()]] - code - gateway/tests/test_multi_turn_tracker.py
- [[.test_sequential_extraction_detection()]] - code - gateway/tests/test_multi_turn_tracker.py
- [[.test_session_blocking()]] - code - gateway/tests/test_multi_turn_tracker.py
- [[.test_session_cleanup()]] - code - gateway/tests/test_multi_turn_tracker.py
- [[.test_session_reset()]] - code - gateway/tests/test_multi_turn_tracker.py
- [[.test_session_stats()]] - code - gateway/tests/test_multi_turn_tracker.py
- [[.test_system_info_detection()]] - code - gateway/tests/test_multi_turn_tracker.py
- [[.test_threshold_warnings()]] - code - gateway/tests/test_multi_turn_tracker.py
- [[.test_tool_name_detection()]] - code - gateway/tests/test_multi_turn_tracker.py
- [[Test alert callback functionality.]] - rationale - gateway/tests/test_multi_turn_tracker.py
- [[Test analysis of agent responses for potential leaks.]] - rationale - gateway/tests/test_multi_turn_tracker.py
- [[Test basic message tracking functionality.]] - rationale - gateway/tests/test_multi_turn_tracker.py
- [[Test behavior of blocked sessions.]] - rationale - gateway/tests/test_multi_turn_tracker.py
- [[Test cases for MultiTurnTracker class.]] - rationale - gateway/tests/test_multi_turn_tracker.py
- [[Test cleanup of old sessions.]] - rationale - gateway/tests/test_multi_turn_tracker.py
- [[Test detection of PII fragment patterns.]] - rationale - gateway/tests/test_multi_turn_tracker.py
- [[Test detection of credential-related queries.]] - rationale - gateway/tests/test_multi_turn_tracker.py
- [[Test detection of file reference patterns.]] - rationale - gateway/tests/test_multi_turn_tracker.py
- [[Test detection of infrastructure-related queries.]] - rationale - gateway/tests/test_multi_turn_tracker.py
- [[Test detection of repeated queries with different phrasing.]] - rationale - gateway/tests/test_multi_turn_tracker.py
- [[Test detection of sequential extraction patterns.]] - rationale - gateway/tests/test_multi_turn_tracker.py
- [[Test detection of system information queries.]] - rationale - gateway/tests/test_multi_turn_tracker.py
- [[Test detection of tool inventory queries.]] - rationale - gateway/tests/test_multi_turn_tracker.py
- [[Test edge cases and error conditions._1]] - rationale - gateway/tests/test_multi_turn_tracker.py
- [[Test getting session statistics.]] - rationale - gateway/tests/test_multi_turn_tracker.py
- [[Test getting statistics.]] - rationale - gateway/tests/test_path_isolation.py
- [[Test proper initialization of MultiTurnTracker.]] - rationale - gateway/tests/test_multi_turn_tracker.py
- [[Test session reset functionality.]] - rationale - gateway/tests/test_multi_turn_tracker.py
- [[Test that disabled tracker doesn't track or score.]] - rationale - gateway/tests/test_multi_turn_tracker.py
- [[Test that scores accumulate across turns.]] - rationale - gateway/tests/test_multi_turn_tracker.py
- [[Test that sessions get blocked at high scores.]] - rationale - gateway/tests/test_multi_turn_tracker.py
- [[Test threshold-based warning system.]] - rationale - gateway/tests/test_multi_turn_tracker.py
- [[TestMultiTurnTracker]] - code - gateway/tests/test_multi_turn_tracker.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestMultiTurnTracker
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_Enum]]
- 2 edges to [[_COMMUNITY_lifespan.py]]
- 1 edge to [[_COMMUNITY_TestPathIsolationManager]]

## Top bridge nodes
- [[TestMultiTurnTracker]] - degree 27, connects to 2 communities
- [[.test_disabled_tracker()]] - degree 3, connects to 1 community
- [[.test_get_stats()_2]] - degree 2, connects to 1 community
- [[.test_global_stats()_1]] - degree 2, connects to 1 community