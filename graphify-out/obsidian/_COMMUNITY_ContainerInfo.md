---
type: community
cohesion: 0.20
members: 12
---

# ContainerInfo

**Cohesion:** 0.20 - loosely connected
**Members:** 12 nodes

## Members
- [[.ps()]] - code - gateway/runtime/apple_engine.py
- [[.ps()_1]] - code - gateway/runtime/docker_engine.py
- [[.ps()_2]] - code - gateway/runtime/engine.py
- [[.ps()_3]] - code - gateway/runtime/podman_engine.py
- [[.test_defaults()]] - code - gateway/tests/test_runtime_engines.py
- [[.test_with_data()]] - code - gateway/tests/test_runtime_engines.py
- [[ContainerInfo]] - code - gateway/runtime/apple_engine.py
- [[ContainerInfo_1]] - code - gateway/runtime/docker_engine.py
- [[ContainerInfo_2]] - code - gateway/runtime/podman_engine.py
- [[ContainerInfo_3]] - code - gateway/runtime/engine.py
- [[Lightweight container metadata returned by psinspect.]] - rationale - gateway/runtime/engine.py
- [[TestContainerInfo]] - code - gateway/tests/test_runtime_engines.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/ContainerInfo
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_test_runtime_engines.py]]
- 5 edges to [[_COMMUNITY_RuntimeConfig]]
- 5 edges to [[_COMMUNITY_PodmanEngine]]
- 4 edges to [[_COMMUNITY_ContainerEngine]]
- 4 edges to [[_COMMUNITY_AppleContainerEngine]]
- 4 edges to [[_COMMUNITY_DockerEngine]]
- 1 edge to [[_COMMUNITY_TestAppleContainerEngine]]
- 1 edge to [[_COMMUNITY_detect_runtime()]]
- 1 edge to [[_COMMUNITY_TestDockerEngine]]
- 1 edge to [[_COMMUNITY_get_engine()]]
- 1 edge to [[_COMMUNITY_TestInstallerAPI]]
- 1 edge to [[_COMMUNITY_TestSecurityFeatures]]
- 1 edge to [[_COMMUNITY_TestWebAPI]]

## Top bridge nodes
- [[ContainerInfo_3]] - degree 31, connects to 12 communities
- [[TestContainerInfo]] - degree 8, connects to 4 communities
- [[ContainerInfo]] - degree 3, connects to 1 community
- [[ContainerInfo_1]] - degree 3, connects to 1 community
- [[ContainerInfo_2]] - degree 3, connects to 1 community