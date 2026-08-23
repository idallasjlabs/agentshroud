---
type: community
cohesion: 0.20
members: 10
---

# Diagram 14 Logic Flow (images)

**Cohesion:** 0.20 - loosely connected
**Members:** 10 nodes

## Members
- [[Approval queue (notify Isaiah via Telegram, wait up to 1 hour)]] - concept - docs/diagrams/images/diagram-14-logic-flow.svg
- [[Execute action via HTTP CONNECT proxy]] - concept - docs/diagrams/images/diagram-14-logic-flow.svg
- [[Isaiah decides (approved  rejected  timeout)]] - concept - docs/diagrams/images/diagram-14-logic-flow.svg
- [[LLM inference (OpenAI GPT-4o or Anthropic Claude)]] - concept - docs/diagrams/images/diagram-14-logic-flow.svg
- [[MCP Inspector (injection scan, PII scan, sensitive op scan)]] - concept - docs/diagrams/images/diagram-14-logic-flow.svg
- [[Main agent (agentshroud_bot)]] - concept - docs/diagrams/images/diagram-14-logic-flow.svg
- [[Response delivered to user]] - concept - docs/diagrams/images/diagram-14-logic-flow.svg
- [[Threat level (NONELOW, MEDIUM, HIGH)]] - concept - docs/diagrams/images/diagram-14-logic-flow.svg
- [[User sends message or cron fires]] - concept - docs/diagrams/images/diagram-14-logic-flow.svg
- [[Write audit entry to ledger.db (SHA-256 hash only)]] - concept - docs/diagrams/images/diagram-14-logic-flow.svg

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Diagram_14_Logic_Flow_images
SORT file.name ASC
```
