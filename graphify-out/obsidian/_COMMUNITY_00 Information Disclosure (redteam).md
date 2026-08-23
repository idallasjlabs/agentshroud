---
type: community
cohesion: 0.50
members: 4
---

# 00 Information Disclosure (redteam)

**Cohesion:** 0.50 - moderately connected
**Members:** 4 nodes

## Members
- [[Monitor-First Design Rationale Observe → Tune → Enforce (operator must flip before production)]] - rationale - docs/planning/redteam/01-enforce-by-default.md
- [[Outbound Infrastructure Content Filter (deny-list for hostnames, tool names, user IDs)]] - concept - docs/planning/redteam/00-information-disclosure.md
- [[Red Team Finding 00 Agent Self-Disclosure of Internal Architecture]] - document - docs/planning/redteam/00-information-disclosure.md
- [[Red Team Finding 01 Security Modules Default to Monitor Mode — Zero Active Defense]] - document - docs/planning/redteam/01-enforce-by-default.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/00_Information_Disclosure_redteam
SORT file.name ASC
```
