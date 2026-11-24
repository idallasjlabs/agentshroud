---
type: community
members: 22
---

# SessionContext

**Members:** 22 nodes

## Members
- [[dot-_add_disclosure_event()]] - code - gateway/security/multi_turn_tracker.py
- [[dot-_analyze_agent_response()]] - code - gateway/security/multi_turn_tracker.py
- [[dot-_analyze_user_message()]] - code - gateway/security/multi_turn_tracker.py
- [[dot-_check_thresholds()]] - code - gateway/security/multi_turn_tracker.py
- [[dot-_normalize_query()]] - code - gateway/security/multi_turn_tracker.py
- [[dot-_score_message_patterns()]] - code - gateway/security/multi_turn_tracker.py
- [[dot-_score_response_patterns()]] - code - gateway/security/multi_turn_tracker.py
- [[dot-_trigger_alert()_1]] - code - gateway/security/multi_turn_tracker.py
- [[dot-track_message()]] - code - gateway/security/multi_turn_tracker.py
- [[A single disclosure event in a session.]] - rationale - gateway/security/multi_turn_tracker.py
- [[Add a disclosure event to the session.]] - rationale - gateway/security/multi_turn_tracker.py
- [[Analyze agent response for potential information leaks.]] - rationale - gateway/security/multi_turn_tracker.py
- [[Analyze user message for disclosure patterns.]] - rationale - gateway/security/multi_turn_tracker.py
- [[Check session score against thresholds and take action.]] - rationale - gateway/security/multi_turn_tracker.py
- [[Context tracking for a single session.]] - rationale - gateway/security/multi_turn_tracker.py
- [[DisclosureEvent]] - code - gateway/security/multi_turn_tracker.py
- [[Normalize query for repeated query detection.]] - rationale - gateway/security/multi_turn_tracker.py
- [[Score agent response for potential leaks.]] - rationale - gateway/security/multi_turn_tracker.py
- [[Score message based on disclosure patterns.]] - rationale - gateway/security/multi_turn_tracker.py
- [[SessionContext]] - code - gateway/security/multi_turn_tracker.py
- [[Track a message and response pair for disclosure analysis. Args session_id…]] - rationale - gateway/security/multi_turn_tracker.py
- [[Trigger alert callbacks.]] - rationale - gateway/security/multi_turn_tracker.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/SessionContext
SORT file.name ASC
```

## Connections to other communities
- 10 edges to [[_COMMUNITY_MultiTurnTracker]]
- 4 edges to [[_COMMUNITY_multi_turn_tracker.py]]

## Top bridge nodes
- [[dot-_add_disclosure_event()]] - degree 8, connects to 2 communities
- [[dot-_trigger_alert()_1]] - degree 5, connects to 2 communities
- [[SessionContext]] - degree 10, connects to 1 community
- [[dot-_analyze_user_message()]] - degree 7, connects to 1 community
- [[dot-track_message()]] - degree 7, connects to 1 community
