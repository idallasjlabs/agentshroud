---
source_file: "skills/openclaw/healthcheck/SKILL.md"
type: "document"
community: "Gateway Ingest API"
location: "L23"
tags:
  - graphify/document
  - graphify/EXTRACTED
  - community/Gateway_Ingest_API
---

# Workflow (follow in order)

## Connections
- [[0) Model self-check (non-blocking)]] - `contains` [EXTRACTED]
- [[1) Establish context (read-only)]] - `contains` [EXTRACTED]
- [[2) Run OpenClaw security audits (read-only)]] - `contains` [EXTRACTED]
- [[3) Check OpenClaw versionupdate status (read-only)]] - `contains` [EXTRACTED]
- [[4) Determine risk tolerance (after system context)]] - `contains` [EXTRACTED]
- [[5) Produce a remediation plan]] - `contains` [EXTRACTED]
- [[6) Offer execution options]] - `contains` [EXTRACTED]
- [[7) Execute with confirmations]] - `contains` [EXTRACTED]
- [[8) Verify and report]] - `contains` [EXTRACTED]
- [[OpenClaw Host Hardening]] - `contains` [EXTRACTED]

#graphify/document #graphify/EXTRACTED #community/Gateway_Ingest_API