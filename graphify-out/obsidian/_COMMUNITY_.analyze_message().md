---
type: community
cohesion: 0.18
members: 15
---

# .analyze_message()

**Cohesion:** 0.18 - loosely connected
**Members:** 15 nodes

## Members
- [[._detect_hidden_instructions()]] - code - gateway/security/context_guard.py
- [[._detect_instruction_injection()]] - code - gateway/security/context_guard.py
- [[._detect_rapid_context_growth()]] - code - gateway/security/context_guard.py
- [[._detect_repetition_attacks()]] - code - gateway/security/context_guard.py
- [[.analyze_message()]] - code - gateway/security/context_guard.py
- [[.should_block_message()]] - code - gateway/security/context_guard.py
- [[Analyze a message for context poisoning attempts.          Args             ses]] - rationale - gateway/security/context_guard.py
- [[ContextAttack]] - code - gateway/security/context_guard.py
- [[Detect hidden instructions buried in large text blocks.]] - rationale - gateway/security/context_guard.py
- [[Detect instruction injection attempts.]] - rationale - gateway/security/context_guard.py
- [[Detect rapid context window filling.]] - rationale - gateway/security/context_guard.py
- [[Detect repetition-based context stuffing attacks.]] - rationale - gateway/security/context_guard.py
- [[Detected context window attack attempt.]] - rationale - gateway/security/context_guard.py
- [[Determine if a message should be blocked.          Returns             Tuple of]] - rationale - gateway/security/context_guard.py
- [[SessionContext]] - code - gateway/security/context_guard.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/analyze_message
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_lifespan.py]]
- 2 edges to [[_COMMUNITY_tool_result_injection.py]]
- 1 edge to [[_COMMUNITY_check_message()]]
- 1 edge to [[_COMMUNITY_KillSwitchMonitor]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy]]
- 1 edge to [[_COMMUNITY_SessionContext]]

## Top bridge nodes
- [[.analyze_message()]] - degree 12, connects to 4 communities
- [[SessionContext]] - degree 4, connects to 2 communities
- [[ContextAttack]] - degree 7, connects to 1 community
- [[._detect_rapid_context_growth()]] - degree 5, connects to 1 community
- [[._detect_hidden_instructions()]] - degree 4, connects to 1 community