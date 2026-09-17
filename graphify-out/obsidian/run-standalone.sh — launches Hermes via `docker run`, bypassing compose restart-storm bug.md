---
source_file: "docker/bots/hermes/run-standalone.sh"
type: "rationale"
community: "run-standalone.sh"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/run-standalonesh
---

# run-standalone.sh — launches Hermes via `docker run`, bypassing compose restart-storm bug

## Connections
- [[cmd_down]] - `calls` [EXTRACTED]
- [[cmd_logs]] - `calls` [EXTRACTED]
- [[cmd_status]] - `calls` [EXTRACTED]
- [[cmd_up]] - `calls` [EXTRACTED]
- [[hermes service (prod, profiles hermesfull — service block is dead code, see run-standalone.sh)]] - `semantically_similar_to` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/run-standalonesh