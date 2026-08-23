---
type: community
cohesion: 0.29
members: 7
---

# Diagram 15 Sequence Telegram (images)

**Cohesion:** 0.29 - loosely connected
**Members:** 7 nodes

## Members
- [[Bot Container (agent decides reply + tool call)]] - concept - docs/diagrams/images/diagram-15-sequence-telegram.svg
- [[Gateway (HMAC auth check, PII redaction via Presidio, route to agent)]] - concept - docs/diagrams/images/diagram-15-sequence-telegram.svg
- [[Isaiah (Telegram)]] - concept - docs/diagrams/images/diagram-15-sequence-telegram.svg
- [[MCP inspection (injection scan NONE, PII scan NONE, sensitive op NONE)]] - concept - docs/diagrams/images/diagram-15-sequence-telegram.svg
- [[OpenAI API (POST v1chatcompletions)]] - concept - docs/diagrams/images/diagram-15-sequence-telegram.svg
- [[Telegram API_1]] - concept - docs/diagrams/images/diagram-15-sequence-telegram.svg
- [[ledger.db (INSERT INTO ledger)]] - concept - docs/diagrams/images/diagram-15-sequence-telegram.svg

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Diagram_15_Sequence_Telegram_images
SORT file.name ASC
```
