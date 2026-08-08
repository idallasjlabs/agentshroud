---
source_file: "docs/vault/06 - Containers & Services/agentshroud-bot.md"
type: "document"
community: "docs/vault"
tags:
  - graphify/document
  - graphify/EXTRACTED
  - community/docs/vault
---

# agentshroud-bot Container

## Connections
- [[Docker Networks]] - `references` [EXTRACTED]
- [[OpenClaw]] - `runs_in` [EXTRACTED]
- [[Playwright]] - `runs_in` [EXTRACTED]
- [[agentshroud-browsers volume (Playwright binaries)]] - `mounts` [EXTRACTED]
- [[agentshroud-config volume (OpenClaw config)]] - `mounts` [EXTRACTED]
- [[agentshroud-gateway Container]] - `depends_on` [EXTRACTED]
- [[agentshroud-isolated network (172.21.0.016)]] - `member_of` [EXTRACTED]
- [[agentshroud-ssh volume (SSH keypair)]] - `mounts` [EXTRACTED]
- [[agentshroud-workspace volume (agent files)]] - `mounts` [EXTRACTED]

#graphify/document #graphify/EXTRACTED #community/docs/vault