---
type: community
cohesion: 0.18
members: 12
---

# tool_result_injection.py

**Cohesion:** 0.18 - loosely connected
**Members:** 12 nodes

## Members
- [[.__init__()_23]] - code - gateway/security/tool_result_injection.py
- [[CVE-2026-22708 — AI Agent Container Escape via Prompt Injection]] - rationale - docs/security/cve-mitigation-matrix.md
- [[CVE-2026-30741 — RCE via Request-Side Prompt Injection]] - rationale - docs/security/cve-mitigation-matrix.md
- [[Get the global context guard instance.]] - rationale - gateway/security/context_guard.py
- [[Initialize the scanner with optional custom rules.          Args             cu]] - rationale - gateway/security/tool_result_injection.py
- [[InjectionResult]] - code - gateway/security/tool_result_injection.py
- [[InjectionRule]] - code - gateway/security/tool_result_injection.py
- [[Result from tool result injection scan.]] - rationale - gateway/security/tool_result_injection.py
- [[Rule for detecting injection patterns in tool results.]] - rationale - gateway/security/tool_result_injection.py
- [[context_guard.py]] - code - gateway/security/context_guard.py
- [[get_context_guard()]] - code - gateway/security/context_guard.py
- [[tool_result_injection.py]] - code - gateway/security/tool_result_injection.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/tool_result_injectionpy
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_lifespan.py]]
- 3 edges to [[_COMMUNITY_test_redteam_probes.py]]
- 2 edges to [[_COMMUNITY_check_message()]]
- 2 edges to [[_COMMUNITY_.analyze_message()]]
- 2 edges to [[_COMMUNITY_TelegramAPIProxy]]
- 2 edges to [[_COMMUNITY_.scan()]]
- 1 edge to [[_COMMUNITY_ContextSegment]]
- 1 edge to [[_COMMUNITY_agentshroud-blueteamSKILL]]
- 1 edge to [[_COMMUNITY_Enum]]
- 1 edge to [[_COMMUNITY_KeyVaultConfig]]
- 1 edge to [[_COMMUNITY_InjectionSeverity]]

## Top bridge nodes
- [[tool_result_injection.py]] - degree 12, connects to 8 communities
- [[context_guard.py]] - degree 9, connects to 5 communities
- [[get_context_guard()]] - degree 4, connects to 2 communities
- [[CVE-2026-22708 — AI Agent Container Escape via Prompt Injection]] - degree 3, connects to 1 community
- [[CVE-2026-30741 — RCE via Request-Side Prompt Injection]] - degree 3, connects to 1 community