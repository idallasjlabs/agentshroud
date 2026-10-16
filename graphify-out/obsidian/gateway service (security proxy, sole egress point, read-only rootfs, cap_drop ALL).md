---
source_file: "docker/docker-compose.yml"
type: "code"
community: "docker/bots/hermes/run-standalone.sh (docker run launcher for Hermes)"
location: "19"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/docker/bots/hermes/run-standalonesh_docker_run_launcher_for_Hermes
---

# gateway service (security proxy, sole egress point, read-only rootfs, cap_drop ALL)

## Connections
- [[CI DAST scan (Nuclei, workflow_dispatch, self-hosted)]] - `references` [EXTRACTED]
- [[Compose secrets block (file fallbacks; asb extracts from credential backend at runtime)]] - `shares_data_with` [EXTRACTED]
- [[Dev override gateway (agentshroud-dev-gateway, 9080, dev Hermes upstreams)]] - `references` [EXTRACTED]
- [[Hermes dashboard bridge port 9120 (dashboard_bridge.py re-exposes loopback-bound 9119)]] - `rationale_for` [EXTRACTED]
- [[Image signing & provenance job (cosign keyless + syft SBOM attest)]] - `references` [INFERRED]
- [[Local model defaults nemotron-3.5-lightning-rapid anchor, qwen3-coder coding, deepseek-r1 reasoning]] - `rationale_for` [EXTRACTED]
- [[Three-tier network segmentation (internal edge  isolated DMZ  dmz) — IEC 62443 FR5]] - `rationale_for` [EXTRACTED]
- [[container macro (always-true placeholder inside the gateway)]] - `references` [EXTRACTED]
- [[gateway-start.sh entrypoint]] - `shares_data_with` [EXTRACTED]
- [[hermes service block (profiles hermesfull; DEAD CODE — Hermes deploys via run-standalone.sh)]] - `references` [EXTRACTED]
- [[openclaw service (isolated network only, egress via gateway8181, DOCKER_HOST=socket-proxy)]] - `references` [EXTRACTED]
- [[sync-version.sh]] - `references` [EXTRACTED]
- [[voice-gateway service (ESP32-S3-BOX-3 STTTTS bridge, cpu_shares 4096, cpuset 0-3)]] - `references` [EXTRACTED]
- [[wazuh-agent sidecar (root moment for privilege drop, then uid 1000)]] - `shares_data_with` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/docker/bots/hermes/run-standalonesh_docker_run_launcher_for_Hermes
