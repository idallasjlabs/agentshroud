---
source_file: "gateway/security/scanner_integration.py"
type: "code"
community: "gateway/cli"
location: "L1631"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/gateway/cli
---

# _score_docker_daemon_config()

## Connections
- [[Score domain 20 Docker Daemon Configuration (0-5). CIS Sections 2 & 3.      0=d]] - `rationale_for` [EXTRACTED]
- [[_is_containerized()]] - `calls` [EXTRACTED]
- [[_read_compose_text()]] - `calls` [EXTRACTED]
- [[_read_docker_daemon_config()]] - `calls` [EXTRACTED]
- [[compute_scorecard()]] - `calls` [EXTRACTED]
- [[scanner_integration.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/gateway/cli