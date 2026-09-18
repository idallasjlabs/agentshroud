---
type: community
cohesion: 0.12
members: 26
---

# test_runtime_engines.py

**Cohesion:** 0.12 - loosely connected
**Members:** 26 nodes

## Members
- [[.client()_3]] - code - gateway/tests/test_runtime_engines.py
- [[.client()_4]] - code - gateway/tests/test_runtime_engines.py
- [[.test_apple_script_custom_services()]] - code - gateway/tests/test_runtime_engines.py
- [[.test_compose_depends_on()]] - code - gateway/tests/test_runtime_engines.py
- [[.test_compose_has_security_opts()]] - code - gateway/tests/test_runtime_engines.py
- [[.test_compose_healthcheck()]] - code - gateway/tests/test_runtime_engines.py
- [[.test_dashboard_page()]] - code - gateway/tests/test_runtime_engines.py
- [[.test_generate_apple_script()]] - code - gateway/tests/test_runtime_engines.py
- [[.test_generate_custom_services()]] - code - gateway/tests/test_runtime_engines.py
- [[.test_generate_docker_compose()]] - code - gateway/tests/test_runtime_engines.py
- [[.test_generate_podman_compose()]] - code - gateway/tests/test_runtime_engines.py
- [[.test_put_then_get()]] - code - gateway/tests/test_runtime_engines.py
- [[Definition of a single service for compose generation.]] - rationale - gateway/runtime/compose_generator.py
- [[Generate a compose YAML file for Docker or Podman.      Args         services]] - rationale - gateway/runtime/compose_generator.py
- [[Generate a shell script to start services with Apple Containers.      Apple Cont]] - rationale - gateway/runtime/compose_generator.py
- [[ServiceDef]] - code - gateway/runtime/compose_generator.py
- [[TestComposeGenerator]] - code - gateway/tests/test_runtime_engines.py
- [[TestConfigRoundTrip]] - code - gateway/tests/test_runtime_engines.py
- [[TestManagementPage]] - code - gateway/tests/test_runtime_engines.py
- [[gatewayruntimeconfig.py (RuntimeConfig)]] - code - gateway/runtime/config.py
- [[gatewayruntimedocker_engine.py (DockerEngine)]] - code - gateway/runtime/docker_engine.py
- [[gatewayruntimepodman_engine.py (PodmanEngine)]] - code - gateway/runtime/podman_engine.py
- [[gatewayruntimesecurity.py (get_features_for_runtime)]] - code - gateway/runtime/security.py
- [[generate_apple_script()]] - code - gateway/runtime/compose_generator.py
- [[generate_compose()]] - code - gateway/runtime/compose_generator.py
- [[test_runtime_engines.py]] - code - gateway/tests/test_runtime_engines.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_runtime_enginespy
SORT file.name ASC
```

## Connections to other communities
- 7 edges to [[_COMMUNITY_TestSecurityFeatures]]
- 6 edges to [[_COMMUNITY_RuntimeConfig]]
- 6 edges to [[_COMMUNITY_ContainerInfo]]
- 6 edges to [[_COMMUNITY_PodmanEngine]]
- 5 edges to [[_COMMUNITY_AppleContainerEngine]]
- 4 edges to [[_COMMUNITY_DockerEngine]]
- 3 edges to [[_COMMUNITY_detect_runtime()]]
- 3 edges to [[_COMMUNITY_get_engine()]]
- 2 edges to [[_COMMUNITY_TestInstallerAPI]]
- 2 edges to [[_COMMUNITY_TestAppleContainerEngine]]
- 2 edges to [[_COMMUNITY_TestDockerEngine]]
- 2 edges to [[_COMMUNITY_TestWebAPI]]
- 1 edge to [[_COMMUNITY_api.py]]
- 1 edge to [[_COMMUNITY_ModeRequest]]

## Top bridge nodes
- [[test_runtime_engines.py]] - degree 33, connects to 14 communities
- [[ServiceDef]] - degree 20, connects to 10 communities
- [[TestComposeGenerator]] - degree 14, connects to 4 communities
- [[TestConfigRoundTrip]] - degree 8, connects to 4 communities
- [[TestManagementPage]] - degree 8, connects to 4 communities