---
type: community
cohesion: 1.00
members: 2
---

# hermes/skills/i-incident-response/SKILL.md

**Cohesion:** 1.00 - tightly connected
**Members:** 2 nodes

## Members
- [[AGENTSHROUD_ENV auto-detected from invoking account]] - rationale - docker/bots/hermes/run-standalone.sh
- [[Hermes resource caps by environment]] - rationale - docker/bots/hermes/run-standalone.sh

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/hermes/skills/i-incident-response/SKILLmd
SORT file.name ASC
```
