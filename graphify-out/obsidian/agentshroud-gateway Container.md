---
source_file: "docs/vault/06 - Containers & Services/agentshroud-gateway.md"
type: "document"
community: "Bot Skill Config"
tags:
  - graphify/document
  - graphify/EXTRACTED
  - community/Bot_Skill_Config
---

# agentshroud-gateway Container

## Connections
- [[Container Errors_1]] - `troubleshoots` [INFERRED]
- [[Docker Networks]] - `references` [EXTRACTED]
- [[FastAPI_4]] - `uses` [INFERRED]
- [[OpenClaw]] - `proxied_by` [EXTRACTED]
- [[OpenSCAP]] - `runs_in` [EXTRACTED]
- [[agentshroud-bot Container]] - `depends_on` [EXTRACTED]
- [[agentshroud-internal network (172.20.0.016)]] - `member_of` [EXTRACTED]
- [[agentshroud-isolated network (172.21.0.016)]] - `member_of` [EXTRACTED]
- [[agentshroud-ssh volume (SSH keypair)]] - `mounts` [EXTRACTED]
- [[agentshroud.yaml (master config)]] - `configured_by` [EXTRACTED]
- [[gateway-data volume (SQLite ledger)]] - `mounts` [EXTRACTED]

#graphify/document #graphify/EXTRACTED #community/Bot_Skill_Config