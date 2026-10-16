---
source_file: "prompts/sunday-upgrade.md"
type: "rationale"
community: "docker/bots/hermes/run-standalone.sh (docker run launcher for Hermes)"
location: "9"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/docker/bots/hermes/run-standalonesh_docker_run_launcher_for_Hermes
---

# The run is judged on state change, not steps completed

## Connections
- [[Image signing & provenance job (cosign keyless + syft SBOM attest)]] - `semantically_similar_to` [INFERRED]
- [[Inventory EVERYTHING MEANS EVERYTHING — a component missing from the table is a failed run]] - `conceptually_related_to` [EXTRACTED]
- [[Semgrep --baseline-commit gate (fail only on NEW findings)]] - `semantically_similar_to` [INFERRED]
- [[Soak, not just boot check-soak-status.sh must report SOAKED on dev OpenClaw]] - `semantically_similar_to` [INFERRED]
- [[Sunday upgrade mission every component in dev and prod to latest stable, resolve every finding, dev first]] - `rationale_for` [EXTRACTED]
- [[sunday-upgrade-apply.sh]] - `references` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/docker/bots/hermes/run-standalonesh_docker_run_launcher_for_Hermes
