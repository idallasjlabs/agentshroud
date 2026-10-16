---
type: community
cohesion: 0.11
members: 25
---

# get_engine

**Cohesion:** 0.11 - loosely connected
**Members:** 25 nodes

## Members
- [[dot-test_auto_detect_priority()]] - code - gateway/tests/test_runtime_engines.py
- [[dot-test_detect_apple()]] - code - gateway/tests/test_runtime_engines.py
- [[dot-test_detect_docker()]] - code - gateway/tests/test_runtime_engines.py
- [[dot-test_detect_multiple()]] - code - gateway/tests/test_runtime_engines.py
- [[dot-test_detect_none()]] - code - gateway/tests/test_runtime_engines.py
- [[dot-test_detect_podman()]] - code - gateway/tests/test_runtime_engines.py
- [[dot-test_explicit_apple()]] - code - gateway/tests/test_runtime_engines.py
- [[dot-test_explicit_docker()]] - code - gateway/tests/test_runtime_engines.py
- [[dot-test_explicit_podman()]] - code - gateway/tests/test_runtime_engines.py
- [[dot-test_invalid_runtime()]] - code - gateway/tests/test_runtime_engines.py
- [[dot-test_no_runtime_available()]] - code - gateway/tests/test_runtime_engines.py
- [[dot-test_security_comparison()]] - code - gateway/tests/test_runtime_engines.py
- [[Aggregate security report.]] - rationale - gateway/web/api.py
- [[Auto-detect which container runtimes are available on this system.]] - rationale - gateway/runtime/__init__.py
- [[ContainerEngine_2]] - code - gateway/runtime/__init__.py
- [[Full system status including all services and runtime info.]] - rationale - gateway/web/api.py
- [[Return a comparison dict {feature_name {runtime supported}}.]] - rationale - gateway/runtime/security.py
- [[Return an appropriate container engine instance.      Args         preference]] - rationale - gateway/runtime/__init__.py
- [[TestDetectRuntime]] - code - gateway/tests/test_runtime_engines.py
- [[TestGetEngine_1]] - code - gateway/tests/test_runtime_engines.py
- [[detect_runtime()]] - code - gateway/runtime/__init__.py
- [[get_engine()]] - code - gateway/runtime/__init__.py
- [[get_security_comparison()]] - code - gateway/runtime/security.py
- [[get_status()]] - code - gateway/web/api.py
- [[security_report()]] - code - gateway/web/api.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/get_engine
SORT file.name ASC
```

## Connections to other communities
- 9 edges to [[_COMMUNITY_test_runtime_engines.py]]
- 5 edges to [[_COMMUNITY_api.py]]
- 3 edges to [[_COMMUNITY__get_engine]]
- 3 edges to [[_COMMUNITY_PodmanEngine]]
- 3 edges to [[_COMMUNITY_DockerEngine]]
- 3 edges to [[_COMMUNITY_AppleContainerEngine]]
- 3 edges to [[_COMMUNITY_TestSecurityFeatures]]
- 3 edges to [[_COMMUNITY_RuntimeConfig]]
- 1 edge to [[_COMMUNITY_ContainerEngine]]
- 1 edge to [[_COMMUNITY_ServiceManager]]
- 1 edge to [[_COMMUNITY_create_auth_dependency]]

## Top bridge nodes
- [[get_engine()]] - degree 16, connects to 6 communities
- [[TestGetEngine_1]] - degree 12, connects to 4 communities
- [[TestDetectRuntime]] - degree 11, connects to 4 communities
- [[ContainerEngine_2]] - degree 5, connects to 4 communities
- [[detect_runtime()]] - degree 11, connects to 3 communities
