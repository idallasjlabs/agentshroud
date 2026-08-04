---
source_file: "docs/vault/01 - Architecture/Startup Sequence.md"
type: "concept"
community: "Module Group 203"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/Module_Group_203
---

# Two-Stage Startup (gateway healthy before bot starts — depends_on: service_healthy)

## Connections
- [[Startup Sequence — AgentShroud]] - `documents` [EXTRACTED]
- [[agentshroud-bot Container (Node.js 22 OpenClaw, port 18789, 4 GB, isolated network)]] - `sequences` [EXTRACTED]
- [[agentshroud-gateway Container (Python 3.13  FastAPI, port 8080, 1280 MB, read-only rootfs)]] - `depends_on` [EXTRACTED]

#graphify/concept #graphify/EXTRACTED #community/Module_Group_203
