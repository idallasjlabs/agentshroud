---
type: community
cohesion: 0.40
members: 10
---

# Export Email Reports (scripts)

**Cohesion:** 0.40 - moderately connected
**Members:** 10 nodes

## Members
- [[Parse --since into a UTC-aware datetime. Accepts 'YYYY-MM-DD' or     'YYYY-MM-DD_1]] - rationale - scripts/export-email-reports.py
- [[Path_43]] - code - scripts/export-email-reports.py
- [[Why report .md source files stand in for a missing sent-mail ledger]] - rationale - scripts/export-email-reports.py
- [[_list_report_files()]] - code - scripts/export-email-reports.py
- [[_parse_since()_1]] - code - scripts/export-email-reports.py
- [[_report_date()]] - code - scripts/export-email-reports.py
- [[datetime_7]] - code - scripts/export-email-reports.py
- [[export-email-reports.py]] - code - scripts/export-email-reports.py
- [[export_bot()]] - code - scripts/export-email-reports.py
- [[main()_16]] - code - scripts/export-email-reports.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Export_Email_Reports_scripts
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_Export Bot Conversations (scripts)]]
- 1 edge to [[_COMMUNITY_Export Telegram History (scripts)]]

## Top bridge nodes
- [[_parse_since()_1]] - degree 6, connects to 2 communities