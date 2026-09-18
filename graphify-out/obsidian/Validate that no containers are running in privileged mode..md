---
source_file: "gateway/security/network_validator.py"
type: "rationale"
community: ".validate_docker_compose_config()"
location: "L415"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/validate_docker_compose_config
---

# Validate that no containers are running in privileged mode.

## Connections
- [[._validate_privileged_containers()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/validate_docker_compose_config