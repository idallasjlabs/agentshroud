---
source_file: "docker/docker-compose.yml"
type: "code"
community: "docker/bots/hermes/run-standalone.sh (docker run launcher for Hermes)"
location: "482"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/docker/bots/hermes/run-standalonesh_docker_run_launcher_for_Hermes
---

# openclaw service (isolated network only, egress via gateway:8181, DOCKER_HOST=socket-proxy)

## Connections
- [[Compose secrets block (file fallbacks; asb extracts from credential backend at runtime)]] - `shares_data_with` [EXTRACTED]
- [[OpenClaw sandbox mode set off (named volume vs bind-mount mismatch)]] - `references` [EXTRACTED]
- [[Stdin-Pipe Deploy Pattern (never docker cp)]] - `conceptually_related_to` [INFERRED]
- [[Three-tier network segmentation (internal edge  isolated DMZ  dmz) — IEC 62443 FR5]] - `rationale_for` [EXTRACTED]
- [[docker-socket-proxy service (digest-pinned tecnativa, narrow allowlist)]] - `references` [EXTRACTED]
- [[dockerscriptsinit-openclaw-config.sh (baked into OpenClaw image; seeds sandbox mode, runs doctor --fix)]] - `references` [EXTRACTED]
- [[gateway service (security proxy, sole egress point, read-only rootfs, cap_drop ALL)]] - `references` [EXTRACTED]
- [[start-agentshroud.sh (OpenClaw entrypoint)]] - `shares_data_with` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/docker/bots/hermes/run-standalonesh_docker_run_launcher_for_Hermes
