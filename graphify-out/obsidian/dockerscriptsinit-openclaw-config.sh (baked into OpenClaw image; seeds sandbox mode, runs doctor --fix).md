---
source_file: "docker/scripts/init-openclaw-config.sh"
type: "code"
community: "docker/bots/hermes/run-standalone.sh (docker run launcher for Hermes)"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/docker/bots/hermes/run-standalonesh_docker_run_launcher_for_Hermes
---

# docker/scripts/init-openclaw-config.sh (baked into OpenClaw image; seeds sandbox mode, runs doctor --fix)

## Connections
- [[OpenClaw sandbox mode set off (named volume vs bind-mount mismatch)]] - `references` [EXTRACTED]
- [[S10 start-agentshroud.sh force-reconciles security-critical live cron jobs]] - `references` [EXTRACTED]
- [[S11 init-openclaw-config.sh seeds jira_dev_ticket.py into live OpenClaw workspace]] - `references` [EXTRACTED]
- [[S9 init-openclaw-config.sh seeds agentshroud-ssh-exec.sh rules into live AGENTS]] - `references` [EXTRACTED]
- [[_oc_config_set()]] - `defines` [EXTRACTED]
- [[_sha256()_3]] - `defines` [EXTRACTED]
- [[init-openclaw-config.sh runs doctor --fix before version seed (schema v23-v24 trap)]] - `references` [EXTRACTED]
- [[init-openclaw-config.sh script]] - `contains` [EXTRACTED]
- [[openclaw service (isolated network only, egress via gateway8181, DOCKER_HOST=socket-proxy)]] - `references` [EXTRACTED]
- [[start-agentshroud.sh]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/docker/bots/hermes/run-standalonesh_docker_run_launcher_for_Hermes
