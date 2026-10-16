---
type: community
cohesion: 0.20
members: 19
---

# export_bot

**Cohesion:** 0.20 - loosely connected
**Members:** 19 nodes

## Members
- [[Parse --since into a UTC-aware datetime. Accepts 'YYYY-MM-DD' or     'YYYY-MM-DD_1]] - rationale - scripts/export-email-reports.py
- [[Parse --since into a UTC-aware datetime. Accepts 'YYYY-MM-DD' or     'YYYY-MM-DD_2]] - rationale - scripts/export-telegram-history.py
- [[Path_52]] - code - scripts/export-email-reports.py
- [[Path_53]] - code - scripts/export-telegram-history.py
- [[Why report .md source files stand in for a missing sent-mail ledger]] - rationale - scripts/export-email-reports.py
- [[_list_report_files()]] - code - scripts/export-email-reports.py
- [[_parse_since()_1]] - code - scripts/export-email-reports.py
- [[_parse_since()_2]] - code - scripts/export-telegram-history.py
- [[_report_date()]] - code - scripts/export-email-reports.py
- [[_require_env()]] - code - scripts/export-telegram-history.py
- [[_serialize()]] - code - scripts/export-telegram-history.py
- [[datetime_6]] - code - scripts/export-email-reports.py
- [[datetime_7]] - code - scripts/export-telegram-history.py
- [[export()]] - code - scripts/export-telegram-history.py
- [[export-email-reports.py]] - code - scripts/export-email-reports.py
- [[export-telegram-history.py]] - code - scripts/export-telegram-history.py
- [[export_bot()]] - code - scripts/export-email-reports.py
- [[main()_25]] - code - scripts/export-email-reports.py
- [[main()_26]] - code - scripts/export-telegram-history.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/export_bot
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_export-bot-conversations.py]]

## Top bridge nodes
- [[export()]] - degree 7, connects to 1 community
- [[_parse_since()_1]] - degree 6, connects to 1 community
- [[_parse_since()_2]] - degree 6, connects to 1 community
