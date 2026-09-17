---
type: community
cohesion: 0.31
members: 10
---

# get_engine()

**Cohesion:** 0.31 - loosely connected
**Members:** 10 nodes

## Members
- [[.test_auto_detect_priority()]] - code - gateway/tests/test_runtime_engines.py
- [[.test_explicit_apple()]] - code - gateway/tests/test_runtime_engines.py
- [[.test_explicit_docker()]] - code - gateway/tests/test_runtime_engines.py
- [[.test_explicit_podman()]] - code - gateway/tests/test_runtime_engines.py
- [[.test_invalid_runtime()]] - code - gateway/tests/test_runtime_engines.py
- [[.test_no_runtime_available()]] - code - gateway/tests/test_runtime_engines.py
- [[ContainerEngine_2]] - code - gateway/runtime/__init__.py
- [[Return an appropriate container engine instance.      Args         preference]] - rationale - gateway/runtime/__init__.py
- [[TestGetEngine_1]] - code - gateway/tests/test_runtime_engines.py
- [[get_engine()]] - code - gateway/runtime/__init__.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/get_engine
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_api.py]]
- 3 edges to [[_COMMUNITY_test_runtime_engines.py]]
- 2 edges to [[_COMMUNITY_PodmanEngine]]
- 2 edges to [[_COMMUNITY_DockerEngine]]
- 2 edges to [[_COMMUNITY_AppleContainerEngine]]
- 1 edge to [[_COMMUNITY_ContainerEngine]]
- 1 edge to [[_COMMUNITY_ContainerInfo]]
- 1 edge to [[_COMMUNITY_RuntimeConfig]]
- 1 edge to [[_COMMUNITY_ingest_apimain.py]]
- 1 edge to [[_COMMUNITY_ServiceManager]]
- 1 edge to [[_COMMUNITY_detect_runtime()]]

## Top bridge nodes
- [[get_engine()]] - degree 16, connects to 6 communities
- [[TestGetEngine_1]] - degree 12, connects to 5 communities
- [[ContainerEngine_2]] - degree 5, connects to 4 communities