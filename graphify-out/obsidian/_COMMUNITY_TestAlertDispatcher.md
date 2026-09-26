---
type: community
cohesion: 0.10
members: 21
---

# TestAlertDispatcher

**Cohesion:** 0.10 - loosely connected
**Members:** 21 nodes

## Members
- [[.do_request()]] - code - docker/bots/hermes/patch_telegram_do_request.py
- [[.from_dict()_1]] - code - gateway/runtime/config.py
- [[.from_env()]] - code - gateway/runtime/config.py
- [[.from_env()_1]] - code - gateway/security/killswitch_config.py
- [[.from_env()_2]] - code - gateway/security/memory_config.py
- [[.from_environment()]] - code - gateway/security/egress_config.py
- [[.from_file()]] - code - gateway/skills/manifest.py
- [[.from_source()]] - code - gateway/skills/manifest.py
- [[Build a ManifestEntry by reading path from disk.]] - rationale - gateway/skills/manifest.py
- [[Build a manifest by walking source (``~.llm_settings``).          Raises]] - rationale - gateway/skills/manifest.py
- [[Create config from environment variables and AGENTSHROUD_MODE.]] - rationale - gateway/security/egress_config.py
- [[Create configuration from environment variables.]] - rationale - gateway/security/memory_config.py
- [[Load configuration from environment variables.]] - rationale - gateway/runtime/config.py
- [[Load configuration from environment variables._1]] - rationale - gateway/security/killswitch_config.py
- [[Load from a config dictionary (e.g. from YAML).]] - rationale - gateway/runtime/config.py
- [[PTB HTTPXRequest __slots__ Crash-Loop Fix Rationale]] - rationale - docker/bots/hermes/patch_telegram_do_request.py
- [[Path_21]] - code - gateway/skills/manifest.py
- [[_Instr]] - code - docker/bots/hermes/patch_telegram_do_request.py
- [[_wrapped()]] - code - docker/bots/hermes/patch_telegram_do_request.py
- [[cls]] - code
- [[patch_telegram_do_request.py]] - code - docker/bots/hermes/patch_telegram_do_request.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestAlertDispatcher
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_Incident → Test Backfill Rule (R3 extension) ev]]
- 2 edges to [[_COMMUNITY_What You Must Do When Invoked]]
- 2 edges to [[_COMMUNITY_ADR-009 Enforce-by-Default Security Philosophy]]
- 1 edge to [[_COMMUNITY_GitGuard]]
- 1 edge to [[_COMMUNITY_AgentTarget]]
- 1 edge to [[_COMMUNITY_test_mfa_guard.py]]
- 1 edge to [[_COMMUNITY_RBACConfig]]
- 1 edge to [[_COMMUNITY_make_event()]]
- 1 edge to [[_COMMUNITY_lifespan.py]]
- 1 edge to [[_COMMUNITY_ReportStore]]
- 1 edge to [[_COMMUNITY_test_e2e_proxy.py]]
- 1 edge to [[_COMMUNITY_ContainerEngine]]
- 1 edge to [[_COMMUNITY_TestAuth]]
- 1 edge to [[_COMMUNITY_KeyVaultConfig]]
- 1 edge to [[_COMMUNITY_ConsentFramework]]
- 1 edge to [[_COMMUNITY_TeamsConfig]]
- 1 edge to [[_COMMUNITY_TrustManager]]
- 1 edge to [[_COMMUNITY_AWS Cloud Management & FinOps Agent]]
- 1 edge to [[_COMMUNITY_Skill Branding Specialist (BS)]]

## Top bridge nodes
- [[cls]] - degree 21, connects to 12 communities
- [[Path_21]] - degree 5, connects to 3 communities
- [[.from_file()]] - degree 5, connects to 1 community
- [[.from_source()]] - degree 5, connects to 1 community
- [[.from_dict()_1]] - degree 3, connects to 1 community