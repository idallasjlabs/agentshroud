---
type: community
cohesion: 0.33
members: 6
---

# 🔴 CRITICAL — Not Wired (code exists, tests pass,

**Cohesion:** 0.33 - loosely connected
**Members:** 6 nodes

## Members
- [[1. EgressTelegramNotifier — Little Snitch Inline Buttons]] - document - docs/planning/v0.8/v0.8.0-wiring-audit.md
- [[2. Approval Queue — Missing Telegram Notifications]] - document - docs/planning/v0.8/v0.8.0-wiring-audit.md
- [[3. OutputCanary — Not Passed to Pipeline]] - document - docs/planning/v0.8/v0.8.0-wiring-audit.md
- [[4. EnhancedToolResultSanitizer — Not Passed to Pipeline]] - document - docs/planning/v0.8/v0.8.0-wiring-audit.md
- [[5. LLMProxy — Never Instantiated]] - document - docs/planning/v0.8/v0.8.0-wiring-audit.md
- [[🔴 CRITICAL — Not Wired (code exists, tests pass, but NOT running in production)]] - document - docs/planning/v0.8/v0.8.0-wiring-audit.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/_CRITICAL__Not_Wired_code_exists_tests_pass
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_AgentShroud v0.8.0 Watchtower — Comprehensive]]

## Top bridge nodes
- [[🔴 CRITICAL — Not Wired (code exists, tests pass, but NOT running in production)]] - degree 6, connects to 1 community