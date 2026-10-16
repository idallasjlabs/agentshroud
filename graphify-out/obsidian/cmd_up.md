---
source_file: "docker/bots/hermes/run-standalone.sh"
type: "code"
community: "run-standalone.sh (Hermes docker run launcher)"
location: "L255-L359"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/run-standalonesh_Hermes_docker_run_launcher
---

# cmd_up

## Connections
- [[Env-split cron reconciliation (AGENTSHROUD_PROD_CRON_KEEP)]] - `shares_data_with` [EXTRACTED]
- [[_dashboard_auth_env_args]] - `calls` [EXTRACTED]
- [[_dashboard_host_default]] - `calls` [EXTRACTED]
- [[_feedbin_env_args]] - `calls` [EXTRACTED]
- [[_secret_mount_args]] - `calls` [EXTRACTED]
- [[_wait_for_gateway_healthy]] - `calls` [EXTRACTED]
- [[llm_api_proxy (v1{path} LLM reverse proxy route)]] - `references` [INFERRED]
- [[run-standalone.sh (Hermes docker run launcher)]] - `defines` [EXTRACTED]
- [[run-standalone.sh script]] - `calls` [EXTRACTED]
- [[start.sh (Hermes s6 main program  startup wrapper)]] - `shares_data_with` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/run-standalonesh_Hermes_docker_run_launcher
