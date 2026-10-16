---
type: community
cohesion: 0.50
members: 4
---

# System Audit Documentation (SAD)

**Cohesion:** 0.50 - moderately connected
**Members:** 4 nodes

## Members
- [[Session Prompt Generator]] - document - .agents/skills/i-session-prompt/SKILL.md
- [[System Audit Documentation (SAD)]] - document - .agents/skills/i-sad/SKILL.md
- [[System Audit Vault (SAV)]] - document - .agents/skills/i-sav/SKILL.md
- [[System Audit Vault README]] - document - .agents/skills/i-sav/README.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/System_Audit_Documentation_SAD
SORT file.name ASC
```
