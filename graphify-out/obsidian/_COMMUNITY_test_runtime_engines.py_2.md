---
type: community
cohesion: 0.39
members: 8
---

# test_runtime_engines.py

**Cohesion:** 0.39 - loosely connected
**Members:** 8 nodes

## Members
- [[dot-test_detect_apple()]] - code - gateway/tests/test_runtime_engines.py
- [[dot-test_detect_docker()]] - code - gateway/tests/test_runtime_engines.py
- [[dot-test_detect_multiple()]] - code - gateway/tests/test_runtime_engines.py
- [[dot-test_detect_none()]] - code - gateway/tests/test_runtime_engines.py
- [[dot-test_detect_podman()]] - code - gateway/tests/test_runtime_engines.py
- [[Auto-detect which container runtimes are available on this system.]] - rationale - gateway/runtime/__init__.py
- [[TestDetectRuntime]] - code - gateway/tests/test_runtime_engines.py
- [[detect_runtime()]] - code - gateway/runtime/__init__.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_runtime_enginespy
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_test_runtime_engines.py]]
- 2 edges to [[_COMMUNITY_api.py]]
- 1 edge to [[_COMMUNITY_get_engine]]
- 1 edge to [[_COMMUNITY_RuntimeConfig]]
- 1 edge to [[_COMMUNITY_DockerEngine]]
- 1 edge to [[_COMMUNITY_PodmanEngine]]
- 1 edge to [[_COMMUNITY_AppleContainerEngine]]
- 1 edge to [[_COMMUNITY_test_runtime_engines.py_1]]

## Top bridge nodes
- [[TestDetectRuntime]] - degree 11, connects to 5 communities
- [[detect_runtime()]] - degree 11, connects to 4 communities
