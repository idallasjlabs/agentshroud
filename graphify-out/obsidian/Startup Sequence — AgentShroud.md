---
source_file: "docs/vault/01 - Architecture/Startup Sequence.md"
type: "document"
community: "docs/vault"
tags:
  - graphify/document
  - graphify/EXTRACTED
  - community/docs/vault
---

# Startup Sequence — AgentShroud

## Connections
- [[Two-Stage Startup (gateway healthy before bot starts — depends_on service_healthy)]] - `documents` [EXTRACTED]
- [[agentshroud-bot Container (Node.js 22 OpenClaw, port 18789, 4 GB, isolated network)]] - `references` [EXTRACTED]
- [[agentshroud-gateway Container (Python 3.13  FastAPI, port 8080, 1280 MB, read-only rootfs)]] - `references` [EXTRACTED]
- [[main.py — FastAPI Entrypoint (5-step POST forward pipeline, 22 lifespan steps)]] - `references` [EXTRACTED]

#graphify/document #graphify/EXTRACTED #community/docs/vault