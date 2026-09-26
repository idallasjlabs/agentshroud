---
source_file: "gateway/runtime/__init__.py"
type: "code"
community: "ADR-009: Enforce-by-Default Security Philosophy"
location: "L1"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/ADR-009_Enforce-by-Default_Security_Philosophy
---

# __init__.py

## Connections
- [[AppleContainerEngine]] - `imports` [EXTRACTED]
- [[ContainerEngine_2]] - `imports` [EXTRACTED]
- [[DockerEngine]] - `imports` [EXTRACTED]
- [[PodmanEngine]] - `imports` [EXTRACTED]
- [[apple_engine.py]] - `re_exports` [EXTRACTED]
- [[detect_runtime()]] - `contains` [EXTRACTED]
- [[docker_engine.py]] - `re_exports` [EXTRACTED]
- [[engine.py]] - `re_exports` [EXTRACTED]
- [[get_engine()]] - `contains` [EXTRACTED]
- [[podman_engine.py]] - `re_exports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/ADR-009_Enforce-by-Default_Security_Philosophy