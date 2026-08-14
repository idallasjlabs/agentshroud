---
type: community
members: 4
---

# Architecture Docs

**Members:** 4 nodes

## Members
- [[i-atlas SKILL.md (Curriculum Architect, referenced dependency)]] - document - docker/config/hermes/skills/i-atlas/SKILL.md
- [[i-socrates SKILL.md (Dialogue Architect, referenced dependency)]] - document - docker/config/hermes/skills/i-socrates/SKILL.md
- [[i-vulcan README]] - document - docker/config/hermes/skills/i-vulcan/README.md
- [[i-vulcan SKILL.md (Subject Matter Auditor, podcast QA gate)]] - document - docker/config/hermes/skills/i-vulcan/SKILL.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Architecture_Docs
SORT file.name ASC
```
