---
source_file: ".github/workflows/security-scan.yml"
type: "rationale"
community: "docker/bots/hermes/run-standalone.sh (docker run launcher for Hermes)"
location: "121"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/docker/bots/hermes/run-standalonesh_docker_run_launcher_for_Hermes
---

# Semgrep --baseline-commit gate (fail only on NEW findings)

## Connections
- [[Semgrep SAST job (IEC 62443 4-1 SDL)]] - `rationale_for` [EXTRACTED]
- [[The run is judged on state change, not steps completed]] - `semantically_similar_to` [INFERRED]
- [[pre-commit semgrep local hook (new findings only, system semgrep)]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/docker/bots/hermes/run-standalonesh_docker_run_launcher_for_Hermes
