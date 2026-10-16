---
type: community
cohesion: 0.06
members: 46
---

# start-agentshroud.sh

**Cohesion:** 0.06 - loosely connected
**Members:** 46 nodes

## Members
- [[120s freshclam timeout rationale (bounded failure over outage)]] - rationale - docker/scripts/security-entrypoint.sh
- [[AgentShroud Falco Rules]] - document - docker/falco/rules.yaml
- [[Capability Dropping Layer (cap_drop ALL, add back minimum)]] - rationale - docs/archive/SECURITY.md
- [[Docker Hardening Measures (no-new-privileges, cap_drop ALL, non-root)]] - rationale - docs/archive/SECURITY-ANALYSIS.md
- [[Env-split cron enabledisable pass (dev enables, prod disables)]] - code - docker/scripts/start-agentshroud.sh
- [[Falco Configuration]] - document - docker/falco/falco.yaml
- [[Falco Rule Unexpected Outbound Connection]] - concept - docker/falco/rules.yaml
- [[Intrusion Detection & Honeypot Files]] - concept - docs/archive/FUTURE-FEATURES.md
- [[Pending OpenClaw migration repair (openclaw doctor --fix) before gateway start]] - code - docker/scripts/start-agentshroud.sh
- [[Rule Container Shell Spawned]] - code - docker/falco/rules.yaml
- [[Rule Crypto Mining Detection]] - code - docker/falco/rules.yaml
- [[Rule File Access Outside Workspace]] - code - docker/falco/rules.yaml
- [[Rule Privilege Escalation Attempt]] - code - docker/falco/rules.yaml
- [[Rule Secret File Access]] - code - docker/falco/rules.yaml
- [[Rule Unexpected Outbound Connection from AgentShroud]] - code - docker/falco/rules.yaml
- [[_container_age_seconds()]] - code - docker/scripts/start-agentshroud.sh
- [[_dns_warmup_probe()]] - code - docker/scripts/start-agentshroud.sh
- [[_enforce_sandbox_cap()]] - code - docker/scripts/start-agentshroud.sh
- [[_model_runtime_ready()]] - code - docker/scripts/start-agentshroud.sh
- [[_poll_openclaw_ready()]] - code - docker/scripts/start-agentshroud.sh
- [[_read_hc_secret()]] - code - docker/scripts/start-agentshroud.sh
- [[_read_secret_file()]] - code - docker/scripts/start-agentshroud.sh
- [[_reap_exited_sandboxes()]] - code - docker/scripts/start-agentshroud.sh
- [[_reap_idle_sandboxes()]] - code - docker/scripts/start-agentshroud.sh
- [[_reconcile_security_critical_cron()]] - code - docker/scripts/start-agentshroud.sh
- [[_rename_to_meaningful()]] - code - docker/scripts/start-agentshroud.sh
- [[_slack_channel_id()]] - code - docker/scripts/start-agentshroud.sh
- [[_slack_send()]] - code - docker/scripts/start-agentshroud.sh
- [[_telegram_bot_token()]] - code - docker/scripts/start-agentshroud.sh
- [[_telegram_get_me_ready()]] - code - docker/scripts/start-agentshroud.sh
- [[_telegram_send()]] - code - docker/scripts/start-agentshroud.sh
- [[_telegram_send_photo()]] - code - docker/scripts/start-agentshroud.sh
- [[alert_critical()]] - code - docker/scripts/security-entrypoint.sh
- [[bot-access-audit.sh]] - code - docker/scripts/bot-access-audit.sh
- [[bot-access-audit.sh script]] - code - docker/scripts/bot-access-audit.sh
- [[container macro (always-true placeholder inside the gateway)]] - rationale - docker/falco/rules.yaml
- [[gateway-start.sh]] - code - docker/scripts/gateway-start.sh
- [[gateway-start.sh script]] - code - docker/scripts/gateway-start.sh
- [[log()_2]] - code - docker/scripts/security-entrypoint.sh
- [[macOS Bridge (localhost-only BlueBubbles webhook relay)]] - concept - docs/archive/SECURITY.md
- [[op_proxy_read_with_retry()]] - code - docker/scripts/start-agentshroud.sh
- [[run_op()]] - code - docker/scripts/bot-access-audit.sh
- [[security-entrypoint.sh]] - code - docker/scripts/security-entrypoint.sh
- [[security-entrypoint.sh script]] - code - docker/scripts/security-entrypoint.sh
- [[start-agentshroud.sh]] - code - docker/scripts/start-agentshroud.sh
- [[start-agentshroud.sh script]] - code - docker/scripts/start-agentshroud.sh

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/start-agentshroudsh
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_dockerbotshermesrun-standalone.sh (docker run launcher for Hermes)]]
- 2 edges to [[_COMMUNITY_ServiceManager]]
- 1 edge to [[_COMMUNITY_dockerscriptssecurity-scan.sh]]
- 1 edge to [[_COMMUNITY__is_op_reference_allowed]]
- 1 edge to [[_COMMUNITY_colima-health-check.sh]]
- 1 edge to [[_COMMUNITY_setup-https-proxy.js]]

## Top bridge nodes
- [[start-agentshroud.sh]] - degree 29, connects to 4 communities
- [[container macro (always-true placeholder inside the gateway)]] - degree 7, connects to 1 community
- [[security-entrypoint.sh]] - degree 7, connects to 1 community
- [[Falco Rule Unexpected Outbound Connection]] - degree 2, connects to 1 community
