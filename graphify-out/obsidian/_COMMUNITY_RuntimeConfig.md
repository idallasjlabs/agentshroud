---
type: community
cohesion: 0.18
members: 19
---

# RuntimeConfig

**Cohesion:** 0.18 - loosely connected
**Members:** 19 nodes

## Members
- [[.effective_rootless()]] - code - gateway/runtime/config.py
- [[.test_effective_rootless_docker()]] - code - gateway/tests/test_runtime_engines.py
- [[.test_effective_rootless_override()]] - code - gateway/tests/test_runtime_engines.py
- [[.test_effective_rootless_podman()]] - code - gateway/tests/test_runtime_engines.py
- [[.test_from_dict()]] - code - gateway/tests/test_runtime_engines.py
- [[.test_from_env_defaults()]] - code - gateway/tests/test_runtime_engines.py
- [[.test_from_env_set()]] - code - gateway/tests/test_runtime_engines.py
- [[Configuration for container runtime selection and behavior.      Loaded from env]] - rationale - gateway/runtime/config.py
- [[Resolve rootless setting based on runtime.]] - rationale - gateway/runtime/config.py
- [[RuntimeConfig]] - code - gateway/runtime/config.py
- [[TestRuntimeConfig]] - code - gateway/tests/test_runtime_engines.py
- [[apple_engine.py]] - code - gateway/runtime/apple_engine.py
- [[compose_generator.py]] - code - gateway/runtime/compose_generator.py
- [[docker_engine.py]] - code - gateway/runtime/docker_engine.py
- [[engine.py]] - code - gateway/runtime/engine.py
- [[podman_engine.py]] - code - gateway/runtime/podman_engine.py
- [[runtime__init__.py]] - code - gateway/runtime/__init__.py
- [[runtimeconfig.py]] - code - gateway/runtime/config.py
- [[security.py]] - code - gateway/runtime/security.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/RuntimeConfig
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_ContainerEngine]]
- 6 edges to [[_COMMUNITY_test_runtime_engines.py]]
- 6 edges to [[_COMMUNITY_TestSecurityFeatures]]
- 5 edges to [[_COMMUNITY_ContainerInfo]]
- 4 edges to [[_COMMUNITY_api.py]]
- 3 edges to [[_COMMUNITY_AppleContainerEngine]]
- 3 edges to [[_COMMUNITY_DockerEngine]]
- 3 edges to [[_COMMUNITY_PodmanEngine]]
- 2 edges to [[_COMMUNITY_ADR-006 Multi-Runtime Container Support]]
- 2 edges to [[_COMMUNITY_detect_runtime()]]
- 2 edges to [[_COMMUNITY_cls]]
- 1 edge to [[_COMMUNITY_get_engine()]]

## Top bridge nodes
- [[runtime__init__.py]] - degree 10, connects to 6 communities
- [[TestRuntimeConfig]] - degree 12, connects to 5 communities
- [[docker_engine.py]] - degree 9, connects to 4 communities
- [[podman_engine.py]] - degree 9, connects to 4 communities
- [[RuntimeConfig]] - degree 13, connects to 3 communities