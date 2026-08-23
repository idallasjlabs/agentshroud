---
type: community
cohesion: 0.11
members: 24
---

# Start Agentshroud (scripts)

**Cohesion:** 0.11 - loosely connected
**Members:** 24 nodes

## Members
- [[BRAND_1]] - document - docker/config/openclaw/workspace/BRAND.md
- [[Jira Dev-Ticket Helper Module]] - code - docker/config/hermes/workspace/jira_dev_ticket.py
- [[_dns_warmup_probe()]] - code - docker/scripts/start-agentshroud.sh
- [[_model_runtime_ready()]] - code - docker/scripts/start-agentshroud.sh
- [[_read_secret_file()]] - code - docker/scripts/start-agentshroud.sh
- [[_reconcile_security_critical_cron()]] - code - docker/scripts/start-agentshroud.sh
- [[_sha256()]] - code - docker/scripts/init-openclaw-config.sh
- [[_slack_channel_id()]] - code - docker/scripts/start-agentshroud.sh
- [[_slack_send()]] - code - docker/scripts/start-agentshroud.sh
- [[_telegram_bot_token()_1]] - code - docker/scripts/start-agentshroud.sh
- [[_telegram_get_me_ready()_1]] - code - docker/scripts/start-agentshroud.sh
- [[_telegram_send()_1]] - code - docker/scripts/start-agentshroud.sh
- [[_telegram_send_photo()_1]] - code - docker/scripts/start-agentshroud.sh
- [[entrypoint-agentshroud.sh]] - code - docker/scripts/entrypoint-agentshroud.sh
- [[entrypoint-agentshroud.sh script]] - code - docker/scripts/entrypoint-agentshroud.sh
- [[init-openclaw-config.sh]] - code - docker/scripts/init-openclaw-config.sh
- [[init-openclaw-config.sh script]] - code - docker/scripts/init-openclaw-config.sh
- [[op_proxy_read_with_retry()]] - code - docker/scripts/start-agentshroud.sh
- [[patch-slack-sdk.sh]] - code - docker/scripts/patch-slack-sdk.sh
- [[patch-slack-sdk.sh script]] - code - docker/scripts/patch-slack-sdk.sh
- [[patch-ws-proxy.sh]] - code - docker/scripts/patch-ws-proxy.sh
- [[patch-ws-proxy.sh script]] - code - docker/scripts/patch-ws-proxy.sh
- [[start-agentshroud.sh]] - code - docker/scripts/start-agentshroud.sh
- [[start-agentshroud.sh script]] - code - docker/scripts/start-agentshroud.sh

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Start_Agentshroud_scripts
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_Developer (workspace)]]
- 3 edges to [[_COMMUNITY_Apply Patches (openclaw)]]
- 1 edge to [[_COMMUNITY_Start (hermes)]]
- 1 edge to [[_COMMUNITY_Jira Weekly Review (workspace)]]
- 1 edge to [[_COMMUNITY_Anthropic Base Url (04 - Environment Variables)]]
- 1 edge to [[_COMMUNITY_Readme (dashboard)]]
- 1 edge to [[_COMMUNITY_Readme (scripts)]]
- 1 edge to [[_COMMUNITY_Container Runtime (smoke.d)]]
- 1 edge to [[_COMMUNITY_Readme (branding)]]

## Top bridge nodes
- [[init-openclaw-config.sh]] - degree 17, connects to 5 communities
- [[start-agentshroud.sh]] - degree 17, connects to 3 communities
- [[BRAND_1]] - degree 2, connects to 1 community
- [[Jira Dev-Ticket Helper Module]] - degree 2, connects to 1 community