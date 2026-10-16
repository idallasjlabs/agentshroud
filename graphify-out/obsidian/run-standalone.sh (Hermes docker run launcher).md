---
source_file: "docker/bots/hermes/run-standalone.sh"
type: "code"
community: "run-standalone.sh (Hermes docker run launcher)"
location: "L1-L386"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/run-standalonesh_Hermes_docker_run_launcher
---

# run-standalone.sh (Hermes docker run launcher)

## Connections
- [[AGENTSHROUD_VERSION fallback to dockerversions.env]] - `implements` [EXTRACTED]
- [[Dev override gateway (agentshroud-dev-gateway, 9080, dev Hermes upstreams)]] - `references` [EXTRACTED]
- [[Devprod coexistence on one host offset ports (908018790) and subnets (172.20-2224)]] - `references` [EXTRACTED]
- [[Hermes cron jobs paused by empty AGENTSHROUD_PROD_CRON_KEEP on container recreate]] - `references` [EXTRACTED]
- [[_dashboard_auth_env_args]] - `defines` [EXTRACTED]
- [[_dashboard_host_default]] - `defines` [EXTRACTED]
- [[_feedbin_env_args]] - `defines` [EXTRACTED]
- [[_secret_mount_args]] - `defines` [EXTRACTED]
- [[_wait_for_gateway_healthy]] - `defines` [EXTRACTED]
- [[cmd_down]] - `defines` [EXTRACTED]
- [[cmd_logs]] - `defines` [EXTRACTED]
- [[cmd_status_1]] - `defines` [EXTRACTED]
- [[cmd_up]] - `defines` [EXTRACTED]
- [[hermes service block (profiles hermesfull; DEAD CODE — Hermes deploys via run-standalone.sh)]] - `references` [EXTRACTED]
- [[patch_slack_session_recreate.py]] - `conceptually_related_to` [INFERRED]
- [[run-standalone.sh script]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/run-standalonesh_Hermes_docker_run_launcher
