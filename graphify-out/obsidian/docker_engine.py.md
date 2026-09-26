---
source_file: "gateway/runtime/docker_engine.py"
type: "code"
community: "ADR-009: Enforce-by-Default Security Philosophy"
location: "L1"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/ADR-009_Enforce-by-Default_Security_Philosophy
---

# docker_engine.py

## Connections
- [[ADR-006 Multi-Runtime Container Support]] - `implements` [EXTRACTED]
- [[ContainerEngine_2]] - `imports` [EXTRACTED]
- [[ContainerInfo_2]] - `imports` [EXTRACTED]
- [[DockerEngine]] - `contains` [EXTRACTED]
- [[RuntimeConfig]] - `references` [EXTRACTED]
- [[__init__.py_8]] - `re_exports` [EXTRACTED]
- [[compose_generator.py]] - `references` [EXTRACTED]
- [[engine.py]] - `imports_from` [EXTRACTED]
- [[security.py]] - `references` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/ADR-009_Enforce-by-Default_Security_Philosophy