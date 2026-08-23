---
type: community
cohesion: 0.20
members: 12
---

# Diagram 09 Data Lineage (images)

**Cohesion:** 0.20 - loosely connected
**Members:** 12 nodes

## Members
- [[Audit query GET ledger (hashes only)]] - concept - docs/diagrams/images/diagram-09-data-lineage.svg
- [[Auto-delete at expires_at]] - concept - docs/diagrams/images/diagram-09-data-lineage.svg
- [[Cron trigger (no user content)]] - concept - docs/diagrams/images/diagram-09-data-lineage.svg
- [[LLM API call (sanitized text only)]] - concept - docs/diagrams/images/diagram-09-data-lineage.svg
- [[PII Redaction (PHONE_NUMBER, EMAIL_ADDRESS, SSN)]] - concept - docs/diagrams/images/diagram-09-data-lineage.svg
- [[Response to user (Telegram  iMessage)]] - concept - docs/diagrams/images/diagram-09-data-lineage.svg
- [[Telegram message (raw user text)]] - concept - docs/diagrams/images/diagram-09-data-lineage.svg
- [[Tool call (MCP-inspected)]] - concept - docs/diagrams/images/diagram-09-data-lineage.svg
- [[content_hash = SHA-256(sanitized)]] - concept - docs/diagrams/images/diagram-09-data-lineage.svg
- [[iMessage (raw user text)]] - concept - docs/diagrams/images/diagram-09-data-lineage.svg
- [[ledger row (id, timestamp, source, hashes, sanitized flag, expires_at)]] - concept - docs/diagrams/images/diagram-09-data-lineage.svg
- [[original_content_hash = SHA-256(raw)]] - concept - docs/diagrams/images/diagram-09-data-lineage.svg

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Diagram_09_Data_Lineage_images
SORT file.name ASC
```
