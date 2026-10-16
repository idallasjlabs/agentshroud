---
source_file: "docker/bots/hermes/start.sh"
type: "rationale"
community: "setup-secrets.sh"
location: "L365-L445"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/setup-secretssh
---

# Post-migration model lock + sandboxed terminal + cron fleet default

## Connections
- [[OpenClaw sandbox mode set to off (isolation reduction)]] - `semantically_similar_to` [INFERRED]
- [[start.sh (Hermes s6 main program  startup wrapper)]] - `implements` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/setup-secretssh
