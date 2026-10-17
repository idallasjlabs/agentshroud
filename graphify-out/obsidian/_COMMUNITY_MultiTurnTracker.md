---
type: community
members: 49
---

# MultiTurnTracker

**Members:** 49 nodes

## Members
- [[dot-test_agent_response_analysis()]] - code - gateway/tests/test_multi_turn_tracker.py
- [[dot-test_alert_callbacks()_1]] - code - gateway/tests/test_multi_turn_tracker.py
- [[dot-test_basic_message_tracking()]] - code - gateway/tests/test_multi_turn_tracker.py
- [[dot-test_blocked_session_behavior()]] - code - gateway/tests/test_multi_turn_tracker.py
- [[dot-test_credential_detection()]] - code - gateway/tests/test_multi_turn_tracker.py
- [[dot-test_cumulative_scoring()]] - code - gateway/tests/test_multi_turn_tracker.py
- [[dot-test_disabled_tracker()]] - code - gateway/tests/test_multi_turn_tracker.py
- [[dot-test_edge_cases()_1]] - code - gateway/tests/test_multi_turn_tracker.py
- [[dot-test_file_reference_detection()]] - code - gateway/tests/test_multi_turn_tracker.py
- [[dot-test_get_stats()]] - code - gateway/tests/test_path_isolation.py
- [[dot-test_global_stats()]] - code - gateway/tests/test_multi_turn_tracker.py
- [[dot-test_global_stats()_1]] - code - gateway/tests/test_tool_chain_analyzer.py
- [[dot-test_infrastructure_detection()]] - code - gateway/tests/test_multi_turn_tracker.py
- [[dot-test_initialization()_2]] - code - gateway/tests/test_multi_turn_tracker.py
- [[dot-test_pii_fragment_detection()]] - code - gateway/tests/test_multi_turn_tracker.py
- [[dot-test_repeated_query_detection()]] - code - gateway/tests/test_multi_turn_tracker.py
- [[dot-test_sequential_extraction_detection()]] - code - gateway/tests/test_multi_turn_tracker.py
- [[dot-test_session_blocking()]] - code - gateway/tests/test_multi_turn_tracker.py
- [[dot-test_session_cleanup()_1]] - code - gateway/tests/test_multi_turn_tracker.py
- [[dot-test_session_reset()]] - code - gateway/tests/test_multi_turn_tracker.py
- [[dot-test_session_stats()_1]] - code - gateway/tests/test_multi_turn_tracker.py
- [[dot-test_system_info_detection()]] - code - gateway/tests/test_multi_turn_tracker.py
- [[dot-test_threshold_warnings()]] - code - gateway/tests/test_multi_turn_tracker.py
- [[dot-test_tool_name_detection()]] - code - gateway/tests/test_multi_turn_tracker.py
- [[Test alert callback functionality._1]] - rationale - gateway/tests/test_multi_turn_tracker.py
- [[Test analysis of agent responses for potential leaks.]] - rationale - gateway/tests/test_multi_turn_tracker.py
- [[Test basic message tracking functionality.]] - rationale - gateway/tests/test_multi_turn_tracker.py
- [[Test behavior of blocked sessions.]] - rationale - gateway/tests/test_multi_turn_tracker.py
- [[Test cases for MultiTurnTracker class.]] - rationale - gateway/tests/test_multi_turn_tracker.py
- [[Test cleanup of old sessions._1]] - rationale - gateway/tests/test_multi_turn_tracker.py
- [[Test detection of PII fragment patterns.]] - rationale - gateway/tests/test_multi_turn_tracker.py
- [[Test detection of credential-related queries.]] - rationale - gateway/tests/test_multi_turn_tracker.py
- [[Test detection of file reference patterns.]] - rationale - gateway/tests/test_multi_turn_tracker.py
- [[Test detection of infrastructure-related queries.]] - rationale - gateway/tests/test_multi_turn_tracker.py
- [[Test detection of repeated queries with different phrasing.]] - rationale - gateway/tests/test_multi_turn_tracker.py
- [[Test detection of sequential extraction patterns.]] - rationale - gateway/tests/test_multi_turn_tracker.py
- [[Test detection of system information queries.]] - rationale - gateway/tests/test_multi_turn_tracker.py
- [[Test detection of tool inventory queries.]] - rationale - gateway/tests/test_multi_turn_tracker.py
- [[Test edge cases and error conditions._1]] - rationale - gateway/tests/test_multi_turn_tracker.py
- [[Test getting global statistics.]] - rationale - gateway/tests/test_tool_chain_analyzer.py
- [[Test getting session statistics._1]] - rationale - gateway/tests/test_multi_turn_tracker.py
- [[Test getting statistics.]] - rationale - gateway/tests/test_path_isolation.py
- [[Test proper initialization of MultiTurnTracker.]] - rationale - gateway/tests/test_multi_turn_tracker.py
- [[Test session reset functionality.]] - rationale - gateway/tests/test_multi_turn_tracker.py
- [[Test that disabled tracker doesn't track or score.]] - rationale - gateway/tests/test_multi_turn_tracker.py
- [[Test that scores accumulate across turns.]] - rationale - gateway/tests/test_multi_turn_tracker.py
- [[Test that sessions get blocked at high scores.]] - rationale - gateway/tests/test_multi_turn_tracker.py
- [[Test threshold-based warning system.]] - rationale - gateway/tests/test_multi_turn_tracker.py
- [[TestMultiTurnTracker_1]] - code - gateway/tests/test_multi_turn_tracker.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/MultiTurnTracker
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_TestToolChainAnalyzer]]
- 3 edges to [[_COMMUNITY_AlertDispatcher]]

## Top bridge nodes
- [[TestMultiTurnTracker_1]] - degree 27, connects to 2 communities
- [[dot-test_disabled_tracker()]] - degree 3, connects to 1 community
- [[dot-test_global_stats()_1]] - degree 3, connects to 1 community
- [[dot-test_get_stats()]] - degree 2, connects to 1 community
