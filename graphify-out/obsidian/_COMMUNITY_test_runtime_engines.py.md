---
type: community
cohesion: 0.09
members: 38
---

# test_runtime_engines.py

**Cohesion:** 0.09 - loosely connected
**Members:** 38 nodes

## Members
- [[dot-client()_3]] - code - gateway/tests/test_runtime_engines.py
- [[dot-client()_4]] - code - gateway/tests/test_runtime_engines.py
- [[dot-ps()]] - code - gateway/runtime/engine.py
- [[dot-setup_method()_5]] - code - gateway/tests/test_runtime_engines.py
- [[dot-test_apple_script_custom_services()]] - code - gateway/tests/test_runtime_engines.py
- [[dot-test_compose_depends_on()]] - code - gateway/tests/test_runtime_engines.py
- [[dot-test_compose_has_security_opts()]] - code - gateway/tests/test_runtime_engines.py
- [[dot-test_compose_healthcheck()]] - code - gateway/tests/test_runtime_engines.py
- [[dot-test_dashboard_page()]] - code - gateway/tests/test_runtime_engines.py
- [[dot-test_defaults()]] - code - gateway/tests/test_runtime_engines.py
- [[dot-test_generate_apple_script()]] - code - gateway/tests/test_runtime_engines.py
- [[dot-test_generate_custom_services()]] - code - gateway/tests/test_runtime_engines.py
- [[dot-test_generate_docker_compose()]] - code - gateway/tests/test_runtime_engines.py
- [[dot-test_generate_podman_compose()]] - code - gateway/tests/test_runtime_engines.py
- [[dot-test_generate_systemd()]] - code - gateway/tests/test_runtime_engines.py
- [[dot-test_health_check()]] - code - gateway/tests/test_runtime_engines.py
- [[dot-test_ps_json()]] - code - gateway/tests/test_runtime_engines.py
- [[dot-test_put_then_get()]] - code - gateway/tests/test_runtime_engines.py
- [[dot-test_run_selinux_volumes()]] - code - gateway/tests/test_runtime_engines.py
- [[dot-test_with_data()]] - code - gateway/tests/test_runtime_engines.py
- [[ContainerInfo]] - code - gateway/runtime/engine.py
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
TABLE source_file, type FROM #community/test_runtime_enginespy
SORT file.name ASC
```

## Connections to other communities
- 11 edges to [[_COMMUNITY_RuntimeConfig]]
- 10 edges to [[_COMMUNITY_AppleContainerEngine]]
- 10 edges to [[_COMMUNITY_PodmanEngine]]
- 9 edges to [[_COMMUNITY_get_engine]]
- 9 edges to [[_COMMUNITY_DockerEngine]]
- 8 edges to [[_COMMUNITY_TestSecurityFeatures]]
- 3 edges to [[_COMMUNITY_TestInstallerAPI]]
- 3 edges to [[_COMMUNITY_TestAppleContainerEngine]]
- 3 edges to [[_COMMUNITY_TestDockerEngine]]
- 3 edges to [[_COMMUNITY_TestWebAPI]]
- 1 edge to [[_COMMUNITY_ContainerEngine]]
- 1 edge to [[_COMMUNITY_ModeRequest]]

## Top bridge nodes
- [[test_runtime_engines.py]] - degree 33, connects to 11 communities
- [[ContainerInfo]] - degree 31, connects to 10 communities
- [[ServiceDef]] - degree 20, connects to 7 communities
- [[TestComposeGenerator]] - degree 14, connects to 3 communities
- [[TestPodmanEngine]] - degree 11, connects to 3 communities
