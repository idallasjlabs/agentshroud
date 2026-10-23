---
source_file: "docker/docker-compose.yml"
type: "code"
community: "run-standalone.sh"
location: "L839"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/run-standalonesh
---

# voice-gateway service

## Connections
- [[AgentShroud production compose stack]] - `references` [EXTRACTED]
- [[Marvin dev compose override (agentshroud-bot)]] - `references` [EXTRACTED]
- [[VT_AGENTS table (directhermesopenclaw)]] - `shares_data_with` [INFERRED]
- [[Voice Interface (STTTTS, wake word)]] - `semantically_similar_to` [INFERRED]
- [[gateway service (sole egress, FalcoClamAV in-process)]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/run-standalonesh
