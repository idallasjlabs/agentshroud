---
source_file: "docs/diagrams/images/diagram-12-credential-flow.svg"
type: "concept"
community: "Bot Skill Config"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/Bot_Skill_Config
---

# Gateway Container (has service account)

## Connections
- [[POST credentialsop-proxy endpoint]] - `calls` [EXTRACTED]
- [[op_proxy_read_with_retry() (cascading retries 5s,10s,15s,30s,60s)]] - `calls` [EXTRACTED]

#graphify/concept #graphify/EXTRACTED #community/Bot_Skill_Config