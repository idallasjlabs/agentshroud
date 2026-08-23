---
source_file: "docker/scripts/start-agentshroud.sh"
type: "code"
community: "Start Agentshroud (scripts)"
location: "L1"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Start_Agentshroud_scripts
---

# start-agentshroud.sh

## Connections
- [[_dns_warmup_probe()]] - `defines` [EXTRACTED]
- [[_model_runtime_ready()]] - `defines` [EXTRACTED]
- [[_read_secret_file()]] - `defines` [EXTRACTED]
- [[_reconcile_security_critical_cron()]] - `defines` [EXTRACTED]
- [[_slack_channel_id()]] - `defines` [EXTRACTED]
- [[_slack_send()]] - `defines` [EXTRACTED]
- [[_telegram_bot_token()_1]] - `defines` [EXTRACTED]
- [[_telegram_get_me_ready()_1]] - `defines` [EXTRACTED]
- [[_telegram_send()_1]] - `defines` [EXTRACTED]
- [[_telegram_send_photo()_1]] - `defines` [EXTRACTED]
- [[agentshroud-ssh-exec.sh]] - `shares_data_with` [INFERRED]
- [[dockerscripts README]] - `semantically_similar_to` [AMBIGUOUS]
- [[entrypoint-agentshroud.sh]] - `calls` [AMBIGUOUS]
- [[init-openclaw-config.sh]] - `calls` [EXTRACTED]
- [[op_proxy_read_with_retry()]] - `defines` [EXTRACTED]
- [[start-agentshroud.sh script]] - `contains` [EXTRACTED]
- [[test_openclaw_photo.sh]] - `references` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Start_Agentshroud_scripts