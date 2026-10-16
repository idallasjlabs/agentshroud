---
type: community
cohesion: 0.10
members: 24
---

# asb (AgentShroud Bot helper)

**Cohesion:** 0.10 - loosely connected
**Members:** 24 nodes

## Members
- [[Container runtime auto-detection contract (SCRUM-92)]] - rationale - docker/README.md
- [[_asb_banner]] - code - scripts/asb
- [[_cr_plugin_works()]] - code - scripts/lib/container-runtime.sh
- [[_ensure_sandbox_image]] - code - scripts/asb
- [[_fstrim_colima_datadisk]] - code - scripts/asb
- [[_hermes_down]] - code - scripts/asb
- [[_hermes_up]] - code - scripts/asb
- [[_prune_docker]] - code - scripts/asb
- [[_prune_superseded_images]] - code - scripts/asb
- [[_reset_device_store]] - code - scripts/asb
- [[_rollback()]] - code - scripts/update-agentshroud.sh
- [[asb (AgentShroud Bot helper)]] - code - scripts/asb
- [[check()_8]] - code - scripts/post-deploy-check.sh
- [[container-runtime.sh]] - code - scripts/lib/container-runtime.sh
- [[container-runtime.sh script]] - code - scripts/lib/container-runtime.sh
- [[container_runtime_engine()]] - code - scripts/lib/container-runtime.sh
- [[detect_container_runtime()]] - code - scripts/lib/container-runtime.sh
- [[post-deploy-check.sh]] - code - scripts/post-deploy-check.sh
- [[post-deploy-check.sh script]] - code - scripts/post-deploy-check.sh
- [[restore-backup.sh]] - code - scripts/restore-backup.sh
- [[restore-backup.sh script]] - code - scripts/restore-backup.sh
- [[restore_tar_to_volume()]] - code - scripts/restore-backup.sh
- [[update-agentshroud.sh]] - code - scripts/update-agentshroud.sh
- [[update-agentshroud.sh script]] - code - scripts/update-agentshroud.sh

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/asb_AgentShroud_Bot_helper
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_dockerbotshermesrun-standalone.sh (docker run launcher for Hermes)]]
- 2 edges to [[_COMMUNITY_sunday-upgrade-apply.sh]]
- 2 edges to [[_COMMUNITY_colima-health-check.sh]]
- 1 edge to [[_COMMUNITY_Upgrade Report 2026-09-27 (dev, PARTIAL, Hermes creds)]]
- 1 edge to [[_COMMUNITY_validate_network_security]]
- 1 edge to [[_COMMUNITY_test_openclaw_photo.sh]]
- 1 edge to [[_COMMUNITY_check-vendor-compat.sh]]
- 1 edge to [[_COMMUNITY__is_op_reference_allowed]]

## Top bridge nodes
- [[asb (AgentShroud Bot helper)]] - degree 11, connects to 3 communities
- [[post-deploy-check.sh]] - degree 7, connects to 3 communities
- [[update-agentshroud.sh]] - degree 5, connects to 2 communities
- [[detect_container_runtime()]] - degree 5, connects to 1 community
- [[_hermes_down]] - degree 2, connects to 1 community
