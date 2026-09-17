---
type: community
cohesion: 0.50
members: 4
---

# GSDL-715 (silent regression incident)

**Cohesion:** 0.50 - moderately connected
**Members:** 4 nodes

## Members
- [[Discrete confidence-score rubric]] - rationale - docker/config/hermes/skills/graphify/references/extraction-spec.md
- [[Finding Triage Classes (CONFIRMEDPROBABLESELF_HEALEDFALSE_POSITIVEGOOD_DIRECTION)]] - concept - docker/config/openclaw/skills/i-ab/SKILL.md
- [[GSDL-715 (silent regression incident)]] - concept - docker/config/hermes/skills/i-ab/SKILL.md
- [[scriptsaudit_merge_regression.py]] - concept - docker/config/hermes/skills/i-ab/SKILL.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/GSDL-715_silent_regression_incident
SORT file.name ASC
```
