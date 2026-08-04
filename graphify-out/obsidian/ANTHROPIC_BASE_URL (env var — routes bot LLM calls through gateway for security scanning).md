---
source_file: "/Users/ijefferson.admin/Development/agentshroud/docs/vault/04 - Environment Variables/ANTHROPIC_BASE_URL.md"
type: "document"
community: "Module Group 326"
tags:
  - graphify/document
  - graphify/EXTRACTED
  - community/Module_Group_326
---

# ANTHROPIC_BASE_URL (env var — routes bot LLM calls through gateway for security scanning)

## Connections
- [[agentshroud-bot service (docker-compose port 18789, 4GB memory, isolated network)]] - `sets` [EXTRACTED]
- [[gateway service (docker-compose port 8080, read-only rootfs, 1280MB memory)]] - `routes_traffic_to` [EXTRACTED]

#graphify/document #graphify/EXTRACTED #community/Module_Group_326
