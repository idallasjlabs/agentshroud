---
type: community
members: 11
---

# docker/bots/hermes/run-standalone.sh (docker run launcher for Hermes) (2)

**Members:** 11 nodes

## Members
- [[OpenClaw Cron Jobs Configuration]] - document - docker/config/openclaw/cron/jobs.json
- [[S10 start-agentshroud.sh force-reconciles security-critical live cron jobs]] - concept - tests/startup_smoke/test_bot_boot_static.sh
- [[S11 init-openclaw-config.sh seeds jira_dev_ticket.py into live OpenClaw workspace]] - concept - tests/startup_smoke/test_bot_boot_static.sh
- [[S12 Hermes init-config.sh seeds jira_dev_ticket.py into live Hermes workspace]] - concept - tests/startup_smoke/test_bot_boot_static.sh
- [[S8 no raw sshagentshroud-bot@real Tailscale FQDN in baked bot config]] - concept - tests/startup_smoke/test_bot_boot_static.sh
- [[S9 init-openclaw-config.sh seeds agentshroud-ssh-exec.sh rules into live AGENTS]] - concept - tests/startup_smoke/test_bot_boot_static.sh
- [[_oc_config_set()]] - code - docker/scripts/init-openclaw-config.sh
- [[_sha256()_2]] - code - docker/scripts/init-openclaw-config.sh
- [[dockerscriptsinit-openclaw-config.sh (baked into OpenClaw image; seeds sandbox mode, runs doctor --fix)]] - code - docker/scripts/init-openclaw-config.sh
- [[init-openclaw-config.sh runs doctor --fix before version seed (schema v23-v24 trap)]] - concept - INCIDENT-2026-10-16-conduit-and-stability.md
- [[init-openclaw-config.sh script]] - code - docker/scripts/init-openclaw-config.sh

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/docker/bots/hermes/run-standalonesh_docker_run_launcher_for_Hermes_2
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_dockerbotshermesrun-standalone.sh (docker run launcher for Hermes)]]
- 1 edge to [[_COMMUNITY_start-agentshroud.sh]]
- 1 edge to [[_COMMUNITY_apply-patches.js]]
- 1 edge to [[_COMMUNITY_test_hermes_cron_seed.py]]

## Top bridge nodes
- [[dockerscriptsinit-openclaw-config.sh (baked into OpenClaw image; seeds sandbox mode, runs doctor --fix)]] - degree 10, connects to 2 communities
- [[S12 Hermes init-config.sh seeds jira_dev_ticket.py into live Hermes workspace]] - degree 2, connects to 1 community
- [[OpenClaw Cron Jobs Configuration]] - degree 2, connects to 1 community
