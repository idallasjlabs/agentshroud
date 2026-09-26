---
source_file: "docker/scripts/start-agentshroud.sh"
type: "code"
community: "What You Must Do When Invoked"
location: "L1"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/What_You_Must_Do_When_Invoked
---

# start-agentshroud.sh

## Connections
- [[Env-split cron enabledisable pass (dev enables, prod disables)]] - `references` [EXTRACTED]
- [[OpenClawHermesMCP sandbox container reaper]] - `references` [EXTRACTED]
- [[Pending OpenClaw migration repair (openclaw doctor --fix) before gateway start]] - `references` [EXTRACTED]
- [[Rule Container Shell Spawned]] - `references` [EXTRACTED]
- [[TestIsOpReferenceAllowed]] - `references` [EXTRACTED]
- [[_check_clamd()]] - `shares_data_with` [INFERRED]
- [[_check_wazuh_agent()]] - `shares_data_with` [INFERRED]
- [[_container_age_seconds()]] - `defines` [EXTRACTED]
- [[_dns_warmup_probe()]] - `defines` [EXTRACTED]
- [[_enforce_sandbox_cap()]] - `defines` [EXTRACTED]
- [[_model_runtime_ready()]] - `defines` [EXTRACTED]
- [[_poll_openclaw_ready()]] - `references` [EXTRACTED]
- [[_read_hc_secret()]] - `defines` [EXTRACTED]
- [[_read_secret_file()]] - `defines` [EXTRACTED]
- [[_reap_exited_sandboxes()]] - `defines` [EXTRACTED]
- [[_reap_idle_sandboxes()]] - `defines` [EXTRACTED]
- [[_reconcile_security_critical_cron()]] - `references` [EXTRACTED]
- [[_rename_to_meaningful()]] - `defines` [EXTRACTED]
- [[_slack_channel_id()]] - `defines` [EXTRACTED]
- [[_slack_send()]] - `defines` [EXTRACTED]
- [[_telegram_bot_token()_1]] - `defines` [EXTRACTED]
- [[_telegram_get_me_ready()_1]] - `defines` [EXTRACTED]
- [[_telegram_send()_1]] - `defines` [EXTRACTED]
- [[_telegram_send_photo()_1]] - `defines` [EXTRACTED]
- [[colima-health-check.sh]] - `conceptually_related_to` [INFERRED]
- [[gateway-start.sh]] - `semantically_similar_to` [INFERRED]
- [[init-openclaw-config.sh]] - `calls` [EXTRACTED]
- [[op_proxy_read_with_retry()]] - `defines` [EXTRACTED]
- [[patch-anthropic-sdk.sh]] - `calls` [EXTRACTED]
- [[patch-telegram-sdk.sh]] - `calls` [EXTRACTED]
- [[start-agentshroud.sh script]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/What_You_Must_Do_When_Invoked