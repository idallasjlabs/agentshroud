---
type: community
cohesion: 0.17
members: 16
---

# agentshroud-blueteam/SKILL.md

**Cohesion:** 0.17 - loosely connected
**Members:** 16 nodes

## Members
- [[dot-_detect_hidden_instructions()]] - code - gateway/security/context_guard.py
- [[dot-_detect_instruction_injection()]] - code - gateway/security/context_guard.py
- [[dot-_detect_rapid_context_growth()]] - code - gateway/security/context_guard.py
- [[dot-_detect_repetition_attacks()]] - code - gateway/security/context_guard.py
- [[dot-analyze_message()]] - code - gateway/security/context_guard.py
- [[dot-should_block_message()]] - code - gateway/security/context_guard.py
- [[Analyze a message for context poisoning attempts.          Args             ses]] - rationale - gateway/security/context_guard.py
- [[Context tracking for a session.]] - rationale - gateway/security/context_guard.py
- [[ContextAttack]] - code - gateway/security/context_guard.py
- [[Detect hidden instructions buried in large text blocks.]] - rationale - gateway/security/context_guard.py
- [[Detect instruction injection attempts.]] - rationale - gateway/security/context_guard.py
- [[Detect rapid context window filling.]] - rationale - gateway/security/context_guard.py
- [[Detect repetition-based context stuffing attacks.]] - rationale - gateway/security/context_guard.py
- [[Detected context window attack attempt.]] - rationale - gateway/security/context_guard.py
- [[Determine if a message should be blocked.          Returns             Tuple of]] - rationale - gateway/security/context_guard.py
- [[SessionContext_1]] - code - gateway/security/context_guard.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/agentshroud-blueteam/SKILLmd
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_PIIConfig]]
- 2 edges to [[_COMMUNITY_agentshroud-blueteamSKILL_6]]
- 1 edge to [[_COMMUNITY_KillSwitchMonitor]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy_2]]
- 1 edge to [[_COMMUNITY_MultiTurnTracker]]
- 1 edge to [[_COMMUNITY_agentshroud-blueteamSKILL_4]]

## Top bridge nodes
- [[dot-analyze_message()]] - degree 12, connects to 4 communities
- [[ContextAttack]] - degree 7, connects to 1 community
- [[dot-_detect_rapid_context_growth()]] - degree 5, connects to 1 community
- [[dot-_detect_hidden_instructions()]] - degree 4, connects to 1 community
- [[dot-_detect_instruction_injection()]] - degree 4, connects to 1 community
