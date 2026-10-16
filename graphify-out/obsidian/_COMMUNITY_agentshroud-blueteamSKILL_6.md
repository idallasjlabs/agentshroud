---
type: community
cohesion: 0.40
members: 5
---

# agentshroud-blueteam/SKILL.md

**Cohesion:** 0.40 - moderately connected
**Members:** 5 nodes

## Members
- [[CVE-2026-22708 — AI Agent Container Escape via Prompt Injection]] - rationale - docs/security/cve-mitigation-matrix.md
- [[CVE-2026-30741 — RCE via Request-Side Prompt Injection]] - rationale - docs/security/cve-mitigation-matrix.md
- [[Get the global context guard instance.]] - rationale - gateway/security/context_guard.py
- [[context_guard.py]] - code - gateway/security/context_guard.py
- [[get_context_guard()]] - code - gateway/security/context_guard.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/agentshroud-blueteam/SKILLmd
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_PIIConfig]]
- 2 edges to [[_COMMUNITY_agentshroud-blueteamSKILL_3]]
- 2 edges to [[_COMMUNITY_agentshroud-blueteamSKILL_4]]
- 2 edges to [[_COMMUNITY_Action]]
- 2 edges to [[_COMMUNITY_InjectionAction]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy_2]]
- 1 edge to [[_COMMUNITY_ContextSegment]]

## Top bridge nodes
- [[context_guard.py]] - degree 9, connects to 5 communities
- [[get_context_guard()]] - degree 4, connects to 2 communities
- [[CVE-2026-22708 — AI Agent Container Escape via Prompt Injection]] - degree 3, connects to 2 communities
- [[CVE-2026-30741 — RCE via Request-Side Prompt Injection]] - degree 3, connects to 2 communities
