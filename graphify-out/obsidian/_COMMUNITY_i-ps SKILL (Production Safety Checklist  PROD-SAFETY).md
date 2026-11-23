---
type: community
members: 6
---

# i-ps SKILL (Production Safety Checklist / PROD-SAFETY)

**Members:** 6 nodes

## Members
- [[i-production README (Incident Response)]] - document - docker/config/hermes/skills/i-production/README.md
- [[i-production SKILL (Incident Response  INCIDENT)]] - document - docker/config/hermes/skills/i-production/SKILL.md
- [[i-ps README (Production Safety Checklist)]] - document - docker/config/hermes/skills/i-ps/README.md
- [[i-ps SKILL (Production Safety Checklist  PROD-SAFETY)]] - document - docker/config/hermes/skills/i-ps/SKILL.md
- [[i-qa README (Quality Assurance)]] - document - docker/config/hermes/skills/i-qa/README.md
- [[i-qa SKILL (Quality Assurance  QA)]] - document - docker/config/hermes/skills/i-qa/SKILL.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/i-ps_SKILL_Production_Safety_Checklist_/_PROD-SAFETY
SORT file.name ASC
```
