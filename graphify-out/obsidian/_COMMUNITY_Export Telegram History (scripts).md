---
type: community
cohesion: 0.42
members: 9
---

# Export Telegram History (scripts)

**Cohesion:** 0.42 - moderately connected
**Members:** 9 nodes

## Members
- [[Parse --since into a UTC-aware datetime. Accepts 'YYYY-MM-DD' or     'YYYY-MM-DD_2]] - rationale - scripts/export-telegram-history.py
- [[Path_44]] - code - scripts/export-telegram-history.py
- [[_parse_since()_2]] - code - scripts/export-telegram-history.py
- [[_require_env()]] - code - scripts/export-telegram-history.py
- [[_serialize()]] - code - scripts/export-telegram-history.py
- [[datetime_8]] - code - scripts/export-telegram-history.py
- [[export()]] - code - scripts/export-telegram-history.py
- [[export-telegram-history.py]] - code - scripts/export-telegram-history.py
- [[main()_17]] - code - scripts/export-telegram-history.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Export_Telegram_History_scripts
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_Export Bot Conversations (scripts)]]
- 1 edge to [[_COMMUNITY_Export Email Reports (scripts)]]

## Top bridge nodes
- [[_parse_since()_2]] - degree 6, connects to 2 communities
- [[export()]] - degree 7, connects to 1 community