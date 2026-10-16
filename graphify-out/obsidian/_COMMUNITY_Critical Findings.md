---
type: community
cohesion: 0.15
members: 13
---

# Critical Findings

**Cohesion:** 0.15 - loosely connected
**Members:** 13 nodes

## Members
- [[1. ContextGuard NEVER BLOCKS (Severity HIGH)]] - document - docs/planning/reviews/prompt-injection-assessment-2026-02-25.md
- [[2. Regex-Only Detection (Severity MEDIUM-HIGH)]] - document - docs/planning/reviews/prompt-injection-assessment-2026-02-25.md
- [[3. No Cross-Turn Analysis (Severity HIGH)]] - document - docs/planning/reviews/prompt-injection-assessment-2026-02-25.md
- [[4. No Semantic Understanding (Severity MEDIUM)]] - document - docs/planning/reviews/prompt-injection-assessment-2026-02-25.md
- [[Critical Findings_2]] - document - docs/planning/reviews/prompt-injection-assessment-2026-02-25.md
- [[Current Defenses (3 Layers)]] - document - docs/planning/reviews/prompt-injection-assessment-2026-02-25.md
- [[Layer 1 PromptGuard (11 regex patterns) — P0, ACTIVE]] - document - docs/planning/reviews/prompt-injection-assessment-2026-02-25.md
- [[Layer 2 ContextGuard (23 patterns + session tracking) — P1, ACTIVE]] - document - docs/planning/reviews/prompt-injection-assessment-2026-02-25.md
- [[Layer 3 ToolResultInjectionScanner (12 patterns) — P1, ACTIVE]] - document - docs/planning/reviews/prompt-injection-assessment-2026-02-25.md
- [[Layer 4 PromptProtection (outbound) — P2, ACTIVE]] - document - docs/planning/reviews/prompt-injection-assessment-2026-02-25.md
- [[Prompt Injection Assessment — AgentShroud v0.7.0]] - document - docs/planning/reviews/prompt-injection-assessment-2026-02-25.md
- [[Threat Matrix What Gets Through]] - document - docs/planning/reviews/prompt-injection-assessment-2026-02-25.md
- [[prompt-injection-assessment-2026-02-25]] - document - docs/planning/reviews/prompt-injection-assessment-2026-02-25.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Critical_Findings
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_Core Security Principles]]

## Top bridge nodes
- [[Prompt Injection Assessment — AgentShroud v0.7.0]] - degree 5, connects to 1 community
