---
type: community
cohesion: 0.14
members: 22
---

# TestSecurityFeatures

**Cohesion:** 0.14 - loosely connected
**Members:** 22 nodes

## Members
- [[.test_get_features_apple()]] - code - gateway/tests/test_runtime_engines.py
- [[.test_get_features_docker()]] - code - gateway/tests/test_runtime_engines.py
- [[.test_get_features_podman()]] - code - gateway/tests/test_runtime_engines.py
- [[.test_missing_features()]] - code - gateway/tests/test_runtime_engines.py
- [[.test_security_comparison()]] - code - gateway/tests/test_runtime_engines.py
- [[.test_security_options_apple()]] - code - gateway/tests/test_runtime_engines.py
- [[.test_security_options_docker()]] - code - gateway/tests/test_runtime_engines.py
- [[.test_security_options_podman()]] - code - gateway/tests/test_runtime_engines.py
- [[.test_security_options_unknown()]] - code - gateway/tests/test_runtime_engines.py
- [[.test_warn_missing()]] - code - gateway/tests/test_runtime_engines.py
- [[A security feature with runtime support info.]] - rationale - gateway/runtime/security.py
- [[Return features available for a given runtime.]] - rationale - gateway/runtime/security.py
- [[Return recommended security CLI options for a runtime.]] - rationale - gateway/runtime/security.py
- [[Return warning messages for missing security features.]] - rationale - gateway/runtime/security.py
- [[SecurityFeature]] - code - gateway/runtime/security.py
- [[TestSecurityFeatures]] - code - gateway/tests/test_runtime_engines.py
- [[Validate runtime name to prevent attribute access injection.]] - rationale - gateway/runtime/security.py
- [[_validate_runtime()]] - code - gateway/runtime/security.py
- [[get_features_for_runtime()]] - code - gateway/runtime/security.py
- [[get_missing_features()]] - code - gateway/runtime/security.py
- [[get_security_options()]] - code - gateway/runtime/security.py
- [[warn_missing_features()]] - code - gateway/runtime/security.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestSecurityFeatures
SORT file.name ASC
```

## Connections to other communities
- 7 edges to [[_COMMUNITY_test_runtime_engines.py]]
- 6 edges to [[_COMMUNITY_RuntimeConfig]]
- 4 edges to [[_COMMUNITY_api.py]]
- 1 edge to [[_COMMUNITY_ContainerInfo]]
- 1 edge to [[_COMMUNITY_PodmanEngine]]
- 1 edge to [[_COMMUNITY_DockerEngine]]
- 1 edge to [[_COMMUNITY_AppleContainerEngine]]

## Top bridge nodes
- [[TestSecurityFeatures]] - degree 16, connects to 5 communities
- [[warn_missing_features()]] - degree 9, connects to 3 communities
- [[get_security_options()]] - degree 9, connects to 2 communities
- [[get_features_for_runtime()]] - degree 8, connects to 2 communities
- [[get_missing_features()]] - degree 7, connects to 2 communities