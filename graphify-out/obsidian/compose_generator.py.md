---
source_file: "gateway/runtime/compose_generator.py"
type: "code"
community: "ADR-009: Enforce-by-Default Security Philosophy"
location: "L1"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/ADR-009_Enforce-by-Default_Security_Philosophy
---

# compose_generator.py

## Connections
- [[ServiceDef]] - `contains` [EXTRACTED]
- [[docker_engine.py]] - `references` [EXTRACTED]
- [[engine.py]] - `references` [EXTRACTED]
- [[generate_apple_script()]] - `contains` [EXTRACTED]
- [[generate_compose()]] - `contains` [EXTRACTED]
- [[podman_engine.py]] - `references` [EXTRACTED]
- [[security.py]] - `references` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/ADR-009_Enforce-by-Default_Security_Philosophy