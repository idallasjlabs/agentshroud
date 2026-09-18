---
type: community
cohesion: 0.12
members: 24
---

# SessionContext

**Cohesion:** 0.12 - loosely connected
**Members:** 24 nodes

## Members
- [[._add_disclosure_event()]] - code - gateway/security/multi_turn_tracker.py
- [[._analyze_agent_response()]] - code - gateway/security/multi_turn_tracker.py
- [[._analyze_user_message()]] - code - gateway/security/multi_turn_tracker.py
- [[._check_thresholds()]] - code - gateway/security/multi_turn_tracker.py
- [[._cleanup_old_sessions()]] - code - gateway/security/multi_turn_tracker.py
- [[._normalize_query()]] - code - gateway/security/multi_turn_tracker.py
- [[._score_message_patterns()]] - code - gateway/security/multi_turn_tracker.py
- [[._score_response_patterns()]] - code - gateway/security/multi_turn_tracker.py
- [[._trigger_alert()]] - code - gateway/security/multi_turn_tracker.py
- [[.track_message()]] - code - gateway/security/multi_turn_tracker.py
- [[A single disclosure event in a session.]] - rationale - gateway/security/multi_turn_tracker.py
- [[Add a disclosure event to the session.]] - rationale - gateway/security/multi_turn_tracker.py
- [[Analyze agent response for potential information leaks.]] - rationale - gateway/security/multi_turn_tracker.py
- [[Analyze user message for disclosure patterns.]] - rationale - gateway/security/multi_turn_tracker.py
- [[Check session score against thresholds and take action.]] - rationale - gateway/security/multi_turn_tracker.py
- [[Context tracking for a session.]] - rationale - gateway/security/context_guard.py
- [[DisclosureEvent]] - code - gateway/security/multi_turn_tracker.py
- [[Normalize query for repeated query detection.]] - rationale - gateway/security/multi_turn_tracker.py
- [[Remove old sessions to prevent memory bloat.]] - rationale - gateway/security/multi_turn_tracker.py
- [[Score agent response for potential leaks.]] - rationale - gateway/security/multi_turn_tracker.py
- [[Score message based on disclosure patterns.]] - rationale - gateway/security/multi_turn_tracker.py
- [[SessionContext_1]] - code - gateway/security/multi_turn_tracker.py
- [[Track a message and response pair for disclosure analysis.          Args]] - rationale - gateway/security/multi_turn_tracker.py
- [[Trigger alert callbacks.]] - rationale - gateway/security/multi_turn_tracker.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/SessionContext
SORT file.name ASC
```

## Connections to other communities
- 10 edges to [[_COMMUNITY_lifespan.py]]
- 4 edges to [[_COMMUNITY_Enum]]
- 1 edge to [[_COMMUNITY_.analyze_message()]]

## Top bridge nodes
- [[._add_disclosure_event()]] - degree 8, connects to 2 communities
- [[._trigger_alert()]] - degree 5, connects to 2 communities
- [[SessionContext_1]] - degree 10, connects to 1 community
- [[._analyze_user_message()]] - degree 7, connects to 1 community
- [[.track_message()]] - degree 7, connects to 1 community