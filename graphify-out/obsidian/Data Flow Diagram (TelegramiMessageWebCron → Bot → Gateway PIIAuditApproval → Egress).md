---
source_file: "docs/diagrams/03-data.md"
type: "document"
community: "Module Group 238"
location: "line 7"
tags:
  - graphify/document
  - graphify/INFERRED
  - community/Module_Group_238
---

# Data Flow Diagram (Telegram/iMessage/Web/Cron → Bot → Gateway PII/Audit/Approval → Egress)

## Connections
- [[Approval Queue (SQLite-based, human-in-the-loop, risk-based queuing)]] - `visualizes` [INFERRED]
- [[Audit Ledger (SHA-256 Hash Chain, blockchain-inspired, tamper-evident)]] - `visualizes` [INFERRED]
- [[PII Sanitizer (Microsoft Presidio + custom regex, spaCy models)]] - `visualizes` [INFERRED]

#graphify/document #graphify/INFERRED #community/Module_Group_238