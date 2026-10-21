---
type: community
members: 2
---

# LogSanitizer PII-Scrubbing Log Filter

**Members:** 2 nodes

## Members
- [[Skill observability_2]] - document - docker/config/openclaw/skills/i-observability/SKILL.md
- [[openclawskillsi-observabilitySKILL]] - document - docker/config/openclaw/skills/i-observability/SKILL.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/LogSanitizer_PII-Scrubbing_Log_Filter
SORT file.name ASC
```
