---
type: community
cohesion: 0.09
members: 38
---

# export-bot-conversations.py

**Cohesion:** 0.09 - loosely connected
**Members:** 38 nodes

## Members
- [[.client()_5]] - code - gateway/tests/test_runtime_engines.py
- [[.client()_4]] - code - gateway/tests/test_runtime_engines.py
- [[.ps()_2]] - code - gateway/runtime/engine.py
- [[.setup_method()_24]] - code - gateway/tests/test_runtime_engines.py
- [[.test_apple_script_custom_services()]] - code - gateway/tests/test_runtime_engines.py
- [[.test_compose_depends_on()]] - code - gateway/tests/test_runtime_engines.py
- [[.test_compose_has_security_opts()]] - code - gateway/tests/test_runtime_engines.py
- [[.test_compose_healthcheck()]] - code - gateway/tests/test_runtime_engines.py
- [[.test_dashboard_page()]] - code - gateway/tests/test_runtime_engines.py
- [[.test_defaults()_1]] - code - gateway/tests/test_runtime_engines.py
- [[.test_generate_apple_script()]] - code - gateway/tests/test_runtime_engines.py
- [[.test_generate_custom_services()]] - code - gateway/tests/test_runtime_engines.py
- [[.test_generate_docker_compose()]] - code - gateway/tests/test_runtime_engines.py
- [[.test_generate_podman_compose()]] - code - gateway/tests/test_runtime_engines.py
- [[.test_generate_systemd()]] - code - gateway/tests/test_runtime_engines.py
- [[.test_health_check()]] - code - gateway/tests/test_runtime_engines.py
- [[.test_ps_json()]] - code - gateway/tests/test_runtime_engines.py
- [[.test_put_then_get()]] - code - gateway/tests/test_runtime_engines.py
- [[.test_run_selinux_volumes()]] - code - gateway/tests/test_runtime_engines.py
- [[.test_with_data()]] - code - gateway/tests/test_runtime_engines.py
- [[ContainerInfo_2]] - code - gateway/runtime/engine.py
- [[Definition of a single service for compose generation.]] - rationale - gateway/runtime/compose_generator.py
- [[Generate a compose YAML file for Docker or Podman.      Args         services]] - rationale - gateway/runtime/compose_generator.py
- [[Generate a shell script to start services with Apple Containers.      Apple Cont]] - rationale - gateway/runtime/compose_generator.py
- [[Lightweight container metadata returned by psinspect.]] - rationale - gateway/runtime/engine.py
- [[ServiceDef]] - code - gateway/runtime/compose_generator.py
- [[TestComposeGenerator]] - code - gateway/tests/test_runtime_engines.py
- [[TestConfigRoundTrip]] - code - gateway/tests/test_runtime_engines.py
- [[TestContainerInfo]] - code - gateway/tests/test_runtime_engines.py
- [[TestManagementPage]] - code - gateway/tests/test_runtime_engines.py
- [[TestPodmanEngine]] - code - gateway/tests/test_runtime_engines.py
- [[gatewayruntimeconfig.py (RuntimeConfig)]] - code - gateway/runtime/config.py
- [[gatewayruntimedocker_engine.py (DockerEngine)]] - code - gateway/runtime/docker_engine.py
- [[gatewayruntimepodman_engine.py (PodmanEngine)]] - code - gateway/runtime/podman_engine.py
- [[gatewayruntimesecurity.py (get_features_for_runtime)]] - code - gateway/runtime/security.py
- [[generate_apple_script()]] - code - gateway/runtime/compose_generator.py
- [[generate_compose()]] - code - gateway/runtime/compose_generator.py
- [[test_runtime_engines.py]] - code - gateway/tests/test_runtime_engines.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/export-bot-conversationspy
SORT file.name ASC
```

## Connections to other communities
- 11 edges to [[_COMMUNITY_ADR-009 Enforce-by-Default Security Philosophy]]
- 10 edges to [[_COMMUNITY_iCloud Services]]
- 10 edges to [[_COMMUNITY_GatewayEmailService]]
- 9 edges to [[_COMMUNITY_DELIVERABLE 1 — Domain-by-Domain Assessment]]
- 7 edges to [[_COMMUNITY_TestObservatoryMode]]
- 4 edges to [[_COMMUNITY_get_trivy_summary()]]
- 4 edges to [[_COMMUNITY_REPORT STRUCTURE]]
- 3 edges to [[_COMMUNITY_🟠 HIGH Security & Logic Issues]]
- 3 edges to [[_COMMUNITY_setup-secrets.sh]]
- 3 edges to [[_COMMUNITY_i-icloud SKILL — iCloud Services]]
- 3 edges to [[_COMMUNITY_Skill Audit Branch (AB) — Merge Regression Dete]]
- 2 edges to [[_COMMUNITY_api.py]]
- 1 edge to [[_COMMUNITY_WebhookReceiver]]
- 1 edge to [[_COMMUNITY_test_redteam_probes.py]]

## Top bridge nodes
- [[test_runtime_engines.py]] - degree 33, connects to 13 communities
- [[ContainerInfo_2]] - degree 31, connects to 11 communities
- [[ServiceDef]] - degree 20, connects to 8 communities
- [[TestComposeGenerator]] - degree 14, connects to 3 communities
- [[TestPodmanEngine]] - degree 11, connects to 3 communities