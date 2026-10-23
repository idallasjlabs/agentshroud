---
type: community
cohesion: 0.15
members: 29
---

# telegram_api_proxy (/telegram-api/{path})

**Cohesion:** 0.15 - loosely connected
**Members:** 29 nodes

## Members
- [[COMPOSE (asb compose command string)]] - code - scripts/asb
- [[Compose profile gating (voicehermesfull)]] - rationale - scripts/asb
- [[Container runtime auto-detection contract (SCRUM-92)]] - rationale - docker/README.md
- [[DOCKER_API_VERSION]] - code - scripts/asb
- [[PROJECT (compose project name)]] - code - scripts/asb
- [[S16 asb rebuildclean-rebuild build with $_PROFILE_FLAG]] - concept - tests/startup_smoke/test_bot_boot_static.sh
- [[_PROFILE_FLAG]] - code - scripts/asb
- [[_asb_banner()]] - code - scripts/asb
- [[_cr_plugin_works()]] - code - scripts/lib/container-runtime.sh
- [[_ensure_sandbox_image()]] - code - scripts/asb
- [[_fstrim_colima_datadisk()]] - code - scripts/asb
- [[_hermes_down()]] - code - scripts/asb
- [[_hermes_up()]] - code - scripts/asb
- [[_preserve_nonempty_secrets()]] - code - scripts/asb
- [[_prune_docker()]] - code - scripts/asb
- [[_prune_superseded_images()]] - code - scripts/asb
- [[_reset_device_store()]] - code - scripts/asb
- [[asb]] - code - scripts/asb
- [[asb build]] - code - scripts/asb
- [[asb clean-rebuild fullhermes]] - code - scripts/asb
- [[asb down]] - code - scripts/asb
- [[asb rebuild fullhermes]] - code - scripts/asb
- [[asb script]] - code - scripts/asb
- [[asb up fullhermes]] - code - scripts/asb
- [[container-runtime.sh]] - code - scripts/lib/container-runtime.sh
- [[container-runtime.sh script]] - code - scripts/lib/container-runtime.sh
- [[container_runtime_engine()]] - code - scripts/lib/container-runtime.sh
- [[detect_container_runtime()]] - code - scripts/lib/container-runtime.sh
- [[setup_ephemeral_secrets()]] - code - scripts/asb

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/telegram_api_proxy_/telegram-api/path
SORT file.name ASC
```

## Connections to other communities
- 13 edges to [[_COMMUNITY_PIIConfig]]
- 1 edge to [[_COMMUNITY_run-standalone.sh]]
- 1 edge to [[_COMMUNITY_export-bot-conversations.py]]
- 1 edge to [[_COMMUNITY_setup-secrets.sh]]

## Top bridge nodes
- [[setup_ephemeral_secrets()]] - degree 10, connects to 3 communities
- [[_hermes_up()]] - degree 8, connects to 2 communities
- [[_prune_docker()]] - degree 9, connects to 1 community
- [[asb up fullhermes]] - degree 7, connects to 1 community
- [[COMPOSE (asb compose command string)]] - degree 6, connects to 1 community
