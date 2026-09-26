---
type: community
cohesion: 0.08
members: 34
---

# CI/CD Pipeline Advisor (README)

**Cohesion:** 0.08 - loosely connected
**Members:** 34 nodes

## Members
- [[Compose-specific restart-storm workaround rationale]] - rationale - docker/bots/hermes/run-standalone.sh
- [[Container runtime auto-detection contract (SCRUM-92)]] - rationale - docker/README.md
- [[_asb_banner]] - code - scripts/asb
- [[_cr_plugin_works()]] - code - scripts/lib/container-runtime.sh
- [[_ensure_sandbox_image]] - code - scripts/asb
- [[_fstrim_colima_datadisk]] - code - scripts/asb
- [[_hermes_down]] - code - scripts/asb
- [[_hermes_up]] - code - scripts/asb
- [[_prune_docker]] - code - scripts/asb
- [[_prune_superseded_images]] - code - scripts/asb
- [[_read_running_version_str]] - code - scripts/triage-cve-mitigations.py
- [[_reset_device_store]] - code - scripts/asb
- [[_secret_mount_args()]] - code - docker/bots/hermes/run-standalone.sh
- [[_wait_for_gateway_healthy()]] - code - docker/bots/hermes/run-standalone.sh
- [[aiohttp ClientSession closed-session crash-loop fix (partial)]] - rationale - docker/bots/hermes/patch_slack_session_recreate.py
- [[asb (AgentShroud Bot helper)]] - code - scripts/asb
- [[check-version-pins-parity.sh]] - code - scripts/check-version-pins-parity.sh
- [[check-version-pins-parity.sh script]] - code - scripts/check-version-pins-parity.sh
- [[cmd_down()]] - code - docker/bots/hermes/run-standalone.sh
- [[cmd_logs()]] - code - docker/bots/hermes/run-standalone.sh
- [[cmd_status()]] - code - docker/bots/hermes/run-standalone.sh
- [[cmd_up()]] - code - docker/bots/hermes/run-standalone.sh
- [[container-runtime.sh]] - code - scripts/lib/container-runtime.sh
- [[container-runtime.sh script]] - code - scripts/lib/container-runtime.sh
- [[container_runtime_engine()]] - code - scripts/lib/container-runtime.sh
- [[detect_container_runtime()]] - code - scripts/lib/container-runtime.sh
- [[missing-secret startup visibility check]] - code - docker/bots/hermes/start.sh
- [[patch_slack_session_recreate.py]] - code - docker/bots/hermes/patch_slack_session_recreate.py
- [[run-standalone.sh]] - code - docker/bots/hermes/run-standalone.sh
- [[run-standalone.sh script]] - code - docker/bots/hermes/run-standalone.sh
- [[run-standalone.sh — launches Hermes via `docker run`, bypassing compose restart-storm bug]] - rationale - docker/bots/hermes/run-standalone.sh
- [[setup-secrets.sh]] - code - docker/setup-secrets.sh
- [[setup_ephemeral_secrets]] - code - scripts/asb
- [[versions.env]] - document - docker/versions.env

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/CI/CD_Pipeline_Advisor_README
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_DraftEntry]]
- 1 edge to [[_COMMUNITY_What You Must Do When Invoked]]
- 1 edge to [[_COMMUNITY_Mode A — Single task]]
- 1 edge to [[_COMMUNITY_MCPServerConfig]]
- 1 edge to [[_COMMUNITY_AgentShroud v0.7.0 Enforcement Audit Results]]
- 1 edge to [[_COMMUNITY_Recommendations for Production Deployment]]
- 1 edge to [[_COMMUNITY_Skills by Category]]

## Top bridge nodes
- [[versions.env]] - degree 6, connects to 3 communities
- [[asb (AgentShroud Bot helper)]] - degree 11, connects to 2 communities
- [[run-standalone.sh — launches Hermes via `docker run`, bypassing compose restart-storm bug]] - degree 5, connects to 1 community
- [[detect_container_runtime()]] - degree 5, connects to 1 community
- [[_wait_for_gateway_healthy()]] - degree 3, connects to 1 community