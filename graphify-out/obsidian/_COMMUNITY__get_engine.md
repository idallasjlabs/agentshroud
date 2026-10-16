---
type: community
cohesion: 0.06
members: 37
---

# _get_engine

**Cohesion:** 0.06 - loosely connected
**Members:** 37 nodes

## Members
- [[dot-test_resolves_hermes_to_the_real_renamed_container()]] - code - gateway/tests/test_web_api_coverage.py
- [[dot-test_resolves_openclaw_to_the_convention_default()]] - code - gateway/tests/test_web_api_coverage.py
- [[dot-test_unknown_bot_id_falls_back_to_the_naive_guess()]] - code - gateway/tests/test_web_api_coverage.py
- [[Check for OpenClaw updates (backward-compat alias for updatesbotopenclaw).]] - rationale - gateway/web/api.py
- [[Check for updates for the named bot container.]] - rationale - gateway/web/api.py
- [[Compute valid service names from config + sidecars at call-time. Uses     each b]] - rationale - gateway/web/api.py
- [[Emergency kill switch freeze, shutdown, or disconnect.]] - rationale - gateway/web/api.py
- [[Get the active container engine.]] - rationale - gateway/web/api.py
- [[Pull latest AgentShroud, test, rebuild, restart. Auto-rollback on failure.]] - rationale - gateway/web/api.py
- [[Rebuild containers with latest images.]] - rationale - gateway/web/api.py
- [[Resolve the real Docker container name for a given bot_id — from     BotConfig.r]] - rationale - gateway/web/api.py
- [[Restart a specific service container.]] - rationale - gateway/web/api.py
- [[Retrieve container logs with optional filtering.]] - rationale - gateway/web/api.py
- [[Revert to previous git commit and rebuild.]] - rationale - gateway/web/api.py
- [[Start a specific service container.]] - rationale - gateway/web/api.py
- [[Stop a specific service container.]] - rationale - gateway/web/api.py
- [[TestResolveBotContainer]] - code - gateway/tests/test_web_api_coverage.py
- [[Upgrade OpenClaw (backward-compat alias for updatesbotopenclawupgrade).]] - rationale - gateway/web/api.py
- [[Upgrade a named bot container.]] - rationale - gateway/web/api.py
- [[Validate service name against allowlist to prevent injection.]] - rationale - gateway/web/api.py
- [[_get_engine()]] - code - gateway/web/api.py
- [[_resolve_bot_container must use BotConfig.resolved_container_name, not     a har]] - rationale - gateway/tests/test_web_api_coverage.py
- [[_resolve_bot_container()]] - code - gateway/web/api.py
- [[_valid_services()]] - code - gateway/web/api.py
- [[_validate_service_name()]] - code - gateway/web/api.py
- [[check_bot_updates()]] - code - gateway/web/api.py
- [[check_openclaw_updates()]] - code - gateway/web/api.py
- [[get_logs()]] - code - gateway/web/api.py
- [[killswitch()]] - code - gateway/web/api.py
- [[rebuild()]] - code - gateway/web/api.py
- [[restart_service()]] - code - gateway/web/api.py
- [[rollback_agentshroud()]] - code - gateway/web/api.py
- [[start_service()]] - code - gateway/web/api.py
- [[stop_service()]] - code - gateway/web/api.py
- [[upgrade_agentshroud()]] - code - gateway/web/api.py
- [[upgrade_bot()]] - code - gateway/web/api.py
- [[upgrade_openclaw()]] - code - gateway/web/api.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/_get_engine
SORT file.name ASC
```

## Connections to other communities
- 17 edges to [[_COMMUNITY_api.py]]
- 9 edges to [[_COMMUNITY_ModeRequest]]
- 4 edges to [[_COMMUNITY_load_config]]
- 3 edges to [[_COMMUNITY_get_engine]]
- 2 edges to [[_COMMUNITY_test_config.py]]
- 1 edge to [[_COMMUNITY_upgrade]]

## Top bridge nodes
- [[_resolve_bot_container()]] - degree 9, connects to 3 communities
- [[upgrade_bot()]] - degree 7, connects to 3 communities
- [[killswitch()]] - degree 5, connects to 3 communities
- [[upgrade_agentshroud()]] - degree 5, connects to 3 communities
- [[_valid_services()]] - degree 5, connects to 3 communities
