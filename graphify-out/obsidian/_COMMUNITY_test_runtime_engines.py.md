---
type: community
members: 36
---

# test_runtime_engines.py

**Members:** 36 nodes

## Members
- [[dot-ps()]] - code - gateway/runtime/apple_engine.py
- [[dot-ps()_1]] - code - gateway/runtime/docker_engine.py
- [[dot-ps()_2]] - code - gateway/runtime/podman_engine.py
- [[dot-test_defaults()_1]] - code - gateway/tests/test_runtime_engines.py
- [[dot-test_get_features_apple()]] - code - gateway/tests/test_runtime_engines.py
- [[dot-test_get_features_docker()]] - code - gateway/tests/test_runtime_engines.py
- [[dot-test_get_features_podman()]] - code - gateway/tests/test_runtime_engines.py
- [[dot-test_missing_features()]] - code - gateway/tests/test_runtime_engines.py
- [[dot-test_security_comparison()]] - code - gateway/tests/test_runtime_engines.py
- [[dot-test_security_options_apple()]] - code - gateway/tests/test_runtime_engines.py
- [[dot-test_security_options_docker()]] - code - gateway/tests/test_runtime_engines.py
- [[dot-test_security_options_podman()]] - code - gateway/tests/test_runtime_engines.py
- [[dot-test_security_options_unknown()]] - code - gateway/tests/test_runtime_engines.py
- [[dot-test_warn_missing()]] - code - gateway/tests/test_runtime_engines.py
- [[dot-test_with_data()]] - code - gateway/tests/test_runtime_engines.py
- [[A security feature with runtime support info.]] - rationale - gateway/runtime/security.py
- [[ContainerInfo]] - code - gateway/runtime/engine.py
- [[Lightweight container metadata returned by psinspect.]] - rationale - gateway/runtime/engine.py
- [[Return a comparison dict {feature_name {runtime supported}}.]] - rationale - gateway/runtime/security.py
- [[Return features NOT available for a given runtime.]] - rationale - gateway/runtime/security.py
- [[Return features available for a given runtime.]] - rationale - gateway/runtime/security.py
- [[Return recommended security CLI options for a runtime.]] - rationale - gateway/runtime/security.py
- [[Return warning messages for missing security features.]] - rationale - gateway/runtime/security.py
- [[SecurityFeature]] - code - gateway/runtime/security.py
- [[TestContainerInfo]] - code - gateway/tests/test_runtime_engines.py
- [[TestSecurityFeatures]] - code - gateway/tests/test_runtime_engines.py
- [[Tests for multi-runtime container abstraction layer. Covers all three engines…]] - rationale - gateway/tests/test_runtime_engines.py
- [[Validate runtime name to prevent attribute access injection.]] - rationale - gateway/runtime/security.py
- [[_validate_runtime()]] - code - gateway/runtime/security.py
- [[get_features_for_runtime()]] - code - gateway/runtime/security.py
- [[get_missing_features()]] - code - gateway/runtime/security.py
- [[get_security_comparison()]] - code - gateway/runtime/security.py
- [[get_security_options()]] - code - gateway/runtime/security.py
- [[security.py_2]] - code - gateway/runtime/security.py
- [[test_runtime_engines.py]] - code - gateway/tests/test_runtime_engines.py
- [[warn_missing_features()]] - code - gateway/runtime/security.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_runtime_enginespy
SORT file.name ASC
```

## Connections to other communities
- 9 edges to [[_COMMUNITY_api.py]]
- 6 edges to [[_COMMUNITY_patch]]
- 5 edges to [[_COMMUNITY_ContainerEngine]]
- 5 edges to [[_COMMUNITY_detect_runtime]]
- 4 edges to [[_COMMUNITY_generate_compose]]
- 3 edges to [[_COMMUNITY_TestInstallerAPI]]
- 3 edges to [[_COMMUNITY_AppleContainerEngine]]
- 3 edges to [[_COMMUNITY_DockerEngine]]
- 3 edges to [[_COMMUNITY_PodmanEngine]]
- 1 edge to [[_COMMUNITY_require_auth]]

## Top bridge nodes
- [[test_runtime_engines.py]] - degree 30, connects to 9 communities
- [[ContainerInfo]] - degree 16, connects to 4 communities
- [[get_security_comparison()]] - degree 9, connects to 2 communities
- [[security.py_2]] - degree 9, connects to 2 communities
- [[warn_missing_features()]] - degree 9, connects to 1 community
