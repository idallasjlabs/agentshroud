---
source_file: "gateway/tests/test_privilege_separation.py"
type: "rationale"
community: "Enum"
location: "L146"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Enum
---

# Agent cannot modify Docker Compose configuration.

## Connections
- [[.test_docker_compose_write_blocked()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Enum