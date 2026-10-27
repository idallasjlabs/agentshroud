---
type: community
members: 40
---

# Community 115

**Members:** 40 nodes

## Members
- [[._add_disclosure_event()]] - code - gateway/security/multi_turn_tracker.py
- [[._analyze_agent_response()]] - code - gateway/security/multi_turn_tracker.py
- [[._analyze_user_message()]] - code - gateway/security/multi_turn_tracker.py
- [[._check_thresholds()]] - code - gateway/security/multi_turn_tracker.py
- [[._cleanup_old_sessions()]] - code - gateway/security/multi_turn_tracker.py
- [[._detect_hidden_instructions()]] - code - gateway/security/context_guard.py
- [[._detect_instruction_injection()]] - code - gateway/security/context_guard.py
- [[._detect_rapid_context_growth()]] - code - gateway/security/context_guard.py
- [[._detect_repetition_attacks()]] - code - gateway/security/context_guard.py
- [[._normalize_query()]] - code - gateway/security/multi_turn_tracker.py
- [[._score_message_patterns()]] - code - gateway/security/multi_turn_tracker.py
- [[._score_response_patterns()]] - code - gateway/security/multi_turn_tracker.py
- [[._trigger_alert()]] - code - gateway/security/multi_turn_tracker.py
- [[.analyze_message()]] - code - gateway/security/context_guard.py
- [[.should_block_message()]] - code - gateway/security/context_guard.py
- [[.track_message()]] - code - gateway/security/multi_turn_tracker.py
- [[A single disclosure event in a session.]] - rationale - gateway/security/multi_turn_tracker.py
- [[Add a disclosure event to the session.]] - rationale - gateway/security/multi_turn_tracker.py
- [[Analyze a message for context poisoning attempts.          Args             ses]] - rationale - gateway/security/context_guard.py
- [[Analyze agent response for potential information leaks.]] - rationale - gateway/security/multi_turn_tracker.py
- [[Analyze user message for disclosure patterns.]] - rationale - gateway/security/multi_turn_tracker.py
- [[Check session score against thresholds and take action.]] - rationale - gateway/security/multi_turn_tracker.py
- [[Context tracking for a session.]] - rationale - gateway/security/context_guard.py
- [[Context tracking for a single session.]] - rationale - gateway/security/multi_turn_tracker.py
- [[ContextAttack]] - code - gateway/security/context_guard.py
- [[Detect hidden instructions buried in large text blocks.]] - rationale - gateway/security/context_guard.py
- [[Detect instruction injection attempts.]] - rationale - gateway/security/context_guard.py
- [[Detect rapid context window filling.]] - rationale - gateway/security/context_guard.py
- [[Detect repetition-based context stuffing attacks.]] - rationale - gateway/security/context_guard.py
- [[Detected context window attack attempt.]] - rationale - gateway/security/context_guard.py
- [[Determine if a message should be blocked.          Returns             Tuple of]] - rationale - gateway/security/context_guard.py
- [[DisclosureEvent]] - code - gateway/security/multi_turn_tracker.py
- [[Normalize query for repeated query detection.]] - rationale - gateway/security/multi_turn_tracker.py
- [[Remove old sessions to prevent memory bloat.]] - rationale - gateway/security/multi_turn_tracker.py
- [[Score agent response for potential leaks.]] - rationale - gateway/security/multi_turn_tracker.py
- [[Score message based on disclosure patterns.]] - rationale - gateway/security/multi_turn_tracker.py
- [[SessionContext]] - code - gateway/security/context_guard.py
- [[SessionContext_1]] - code - gateway/security/multi_turn_tracker.py
- [[Track a message and response pair for disclosure analysis.          Args]] - rationale - gateway/security/multi_turn_tracker.py
- [[Trigger alert callbacks.]] - rationale - gateway/security/multi_turn_tracker.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_115
SORT file.name ASC
```

## Connections to other communities
- 16 edges to [[_COMMUNITY_Community 72]]
- 4 edges to [[_COMMUNITY_Community 8]]
- 3 edges to [[_COMMUNITY_Community 344]]
- 1 edge to [[_COMMUNITY_Community 919]]
- 1 edge to [[_COMMUNITY_Community 9]]

## Top bridge nodes
- [[.analyze_message()]] - degree 12, connects to 4 communities
- [[._add_disclosure_event()]] - degree 8, connects to 2 communities
- [[._trigger_alert()]] - degree 5, connects to 2 communities
- [[SessionContext_1]] - degree 11, connects to 1 community
- [[ContextAttack]] - degree 7, connects to 1 community