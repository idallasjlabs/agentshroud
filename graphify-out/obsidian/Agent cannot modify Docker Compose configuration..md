---
source_file: "gateway/tests/test_privilege_separation.py"
type: "rationale"
community: "Environment Guard & Leak Detection"
location: "L147"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Environment_Guard__Leak_Detection
---

# Agent cannot modify Docker Compose configuration.

## Connections
- [[.test_docker_compose_write_blocked()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Environment_Guard__Leak_Detection