---
type: community
cohesion: 0.31
members: 13
---

# Export Bot Conversations (scripts)

**Cohesion:** 0.31 - loosely connected
**Members:** 13 nodes

## Members
- [[OpenClaw message content is a list of blocks (texttool_usetool_result...);]] - rationale - scripts/export-bot-conversations.py
- [[Parse --since into a UTC-aware datetime. Accepts 'YYYY-MM-DD' or     'YYYY-MM-DD]] - rationale - scripts/export-bot-conversations.py
- [[Path_42]] - code - scripts/export-bot-conversations.py
- [[Read a file out of a container via `exec cat` rather than `docker cp` —     on t]] - rationale - scripts/export-bot-conversations.py
- [[Why exec cat replaced docker cp for reading container files]] - rationale - scripts/export-bot-conversations.py
- [[_docker_read_file()]] - code - scripts/export-bot-conversations.py
- [[_extract_text()]] - code - scripts/export-bot-conversations.py
- [[_parse_since()]] - code - scripts/export-bot-conversations.py
- [[datetime_6]] - code - scripts/export-bot-conversations.py
- [[export-bot-conversations.py]] - code - scripts/export-bot-conversations.py
- [[export_hermes()]] - code - scripts/export-bot-conversations.py
- [[export_openclaw()]] - code - scripts/export-bot-conversations.py
- [[main()_15]] - code - scripts/export-bot-conversations.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Export_Bot_Conversations_scripts
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_Export Telegram History (scripts)]]
- 1 edge to [[_COMMUNITY_Export Email Reports (scripts)]]
- 1 edge to [[_COMMUNITY_Iec 62443 Matrix (compliance)]]

## Top bridge nodes
- [[_parse_since()]] - degree 6, connects to 2 communities
- [[export_openclaw()]] - degree 7, connects to 1 community
- [[export_hermes()]] - degree 6, connects to 1 community