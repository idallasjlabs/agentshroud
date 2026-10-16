---
type: community
cohesion: 0.08
members: 31
---

# .analyze_message

**Cohesion:** 0.08 - loosely connected
**Members:** 31 nodes

## Members
- [[dot-__init__()_29]] - code - gateway/security/tool_result_injection.py
- [[dot-_detect_hidden_instructions()]] - code - gateway/security/context_guard.py
- [[dot-_detect_instruction_injection()]] - code - gateway/security/context_guard.py
- [[dot-_detect_rapid_context_growth()]] - code - gateway/security/context_guard.py
- [[dot-_detect_repetition_attacks()]] - code - gateway/security/context_guard.py
- [[dot-analyze_message()]] - code - gateway/security/context_guard.py
- [[dot-scan_tool_result()_1]] - code - gateway/security/tool_result_injection.py
- [[dot-should_block_message()]] - code - gateway/security/context_guard.py
- [[Analyze a message for context poisoning attempts.          Args             ses]] - rationale - gateway/security/context_guard.py
- [[CVE-2026-22708 — AI Agent Container Escape via Prompt Injection]] - rationale - docs/security/cve-mitigation-matrix.md
- [[CVE-2026-30741 — RCE via Request-Side Prompt Injection]] - rationale - docs/security/cve-mitigation-matrix.md
- [[Context tracking for a session.]] - rationale - gateway/security/context_guard.py
- [[ContextAttack]] - code - gateway/security/context_guard.py
- [[Detect hidden instructions buried in large text blocks.]] - rationale - gateway/security/context_guard.py
- [[Detect instruction injection attempts.]] - rationale - gateway/security/context_guard.py
- [[Detect rapid context window filling.]] - rationale - gateway/security/context_guard.py
- [[Detect repetition-based context stuffing attacks.]] - rationale - gateway/security/context_guard.py
- [[Detected context window attack attempt.]] - rationale - gateway/security/context_guard.py
- [[Determine if a message should be blocked.          Returns             Tuple of]] - rationale - gateway/security/context_guard.py
- [[Initialize the scanner with optional custom rules.          Args             cu]] - rationale - gateway/security/tool_result_injection.py
- [[InjectionResult]] - code - gateway/security/tool_result_injection.py
- [[InjectionRule]] - code - gateway/security/tool_result_injection.py
- [[Result from tool result injection scan.]] - rationale - gateway/security/tool_result_injection.py
- [[Rule for detecting injection patterns in tool results.]] - rationale - gateway/security/tool_result_injection.py
- [[Scan tool result content for injection attempts.          Args             tool]] - rationale - gateway/security/tool_result_injection.py
- [[SessionContext]] - code - gateway/security/context_guard.py
- [[Strip potentially malicious markdown from tool results.      Removes     - Mark]] - rationale - gateway/security/input_normalizer.py
- [[context_guard.py]] - code - gateway/security/context_guard.py
- [[input_normalizer.py]] - code - gateway/security/input_normalizer.py
- [[strip_markdown_exfil()]] - code - gateway/security/input_normalizer.py
- [[tool_result_injection.py]] - code - gateway/security/tool_result_injection.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/analyze_message
SORT file.name ASC
```

## Connections to other communities
- 10 edges to [[_COMMUNITY_MiddlewareManager]]
- 5 edges to [[_COMMUNITY_TelegramAPIProxy_1]]
- 4 edges to [[_COMMUNITY_InjectionAction]]
- 3 edges to [[_COMMUNITY_check_message]]
- 2 edges to [[_COMMUNITY_dot-_filter_outbound]]
- 2 edges to [[_COMMUNITY_agentshroud-blueteamSKILL]]
- 2 edges to [[_COMMUNITY_Action]]
- 1 edge to [[_COMMUNITY_OutboundInfoFilter]]
- 1 edge to [[_COMMUNITY_ContextSegment]]
- 1 edge to [[_COMMUNITY_KillSwitchMonitor]]
- 1 edge to [[_COMMUNITY_EgressFilterConfig]]
- 1 edge to [[_COMMUNITY_telegram_proxy.py]]
- 1 edge to [[_COMMUNITY_Enum]]
- 1 edge to [[_COMMUNITY_MultiTurnTracker]]

## Top bridge nodes
- [[tool_result_injection.py]] - degree 12, connects to 5 communities
- [[dot-analyze_message()]] - degree 12, connects to 4 communities
- [[context_guard.py]] - degree 9, connects to 4 communities
- [[dot-scan_tool_result()_1]] - degree 7, connects to 3 communities
- [[input_normalizer.py]] - degree 4, connects to 3 communities
