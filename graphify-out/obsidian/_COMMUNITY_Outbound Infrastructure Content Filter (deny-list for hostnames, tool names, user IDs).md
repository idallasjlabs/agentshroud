---
type: community
members: 4
---

# Outbound Infrastructure Content Filter (deny-list for hostnames, tool names, user IDs)

**Members:** 4 nodes

## Members
- [[Monitor-First Design Rationale Observe → Tune → Enforce (operator must flip before production)]] - rationale - docs/planning/redteam/01-enforce-by-default.md
- [[Outbound Infrastructure Content Filter (deny-list for hostnames, tool names, user IDs)]] - concept - docs/planning/redteam/00-information-disclosure.md
- [[Red Team Finding 00 Agent Self-Disclosure of Internal Architecture]] - document - docs/planning/redteam/00-information-disclosure.md
- [[Red Team Finding 01 Security Modules Default to Monitor Mode — Zero Active Defense]] - document - docs/planning/redteam/01-enforce-by-default.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Outbound_Infrastructure_Content_Filter_deny-list_for_hostnames_tool_names_user_IDs
SORT file.name ASC
```
