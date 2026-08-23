---
type: community
cohesion: 0.20
members: 12
---

# Engine (runtime)

**Cohesion:** 0.20 - loosely connected
**Members:** 12 nodes

## Members
- [[.ps()]] - code - gateway/runtime/apple_engine.py
- [[.ps()_1]] - code - gateway/runtime/docker_engine.py
- [[.ps()_2]] - code - gateway/runtime/engine.py
- [[.ps()_3]] - code - gateway/runtime/podman_engine.py
- [[.test_defaults()_1]] - code - gateway/tests/test_runtime_engines.py
- [[.test_with_data()]] - code - gateway/tests/test_runtime_engines.py
- [[ContainerInfo]] - code - gateway/runtime/apple_engine.py
- [[ContainerInfo_1]] - code - gateway/runtime/docker_engine.py
- [[ContainerInfo_3]] - code - gateway/runtime/podman_engine.py
- [[ContainerInfo_2]] - code - gateway/runtime/engine.py
- [[Lightweight container metadata returned by psinspect.]] - rationale - gateway/runtime/engine.py
- [[TestContainerInfo]] - code - gateway/tests/test_runtime_engines.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Engine_runtime
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_Runtime Engines]]
- 5 edges to [[_COMMUNITY_Runtime Engines]]
- 5 edges to [[_COMMUNITY_Podman Engine (runtime)]]
- 4 edges to [[_COMMUNITY_Apple Engine (runtime)]]
- 4 edges to [[_COMMUNITY_Engine (runtime)]]
- 4 edges to [[_COMMUNITY_Docker Engine (runtime)]]
- 1 edge to [[_COMMUNITY_Runtime Engines]]
- 1 edge to [[_COMMUNITY_Installer (web)]]
- 1 edge to [[_COMMUNITY_Runtime Engines]]
- 1 edge to [[_COMMUNITY_Runtime Engines]]
- 1 edge to [[_COMMUNITY_Runtime Engines]]
- 1 edge to [[_COMMUNITY_Runtime Engines]]
- 1 edge to [[_COMMUNITY_Runtime Engines]]

## Top bridge nodes
- [[ContainerInfo_2]] - degree 31, connects to 12 communities
- [[TestContainerInfo]] - degree 8, connects to 4 communities
- [[ContainerInfo]] - degree 3, connects to 1 community
- [[ContainerInfo_1]] - degree 3, connects to 1 community
- [[ContainerInfo_3]] - degree 3, connects to 1 community