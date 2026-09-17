---
type: community
cohesion: 0.09
members: 33
---

# PodmanEngine

**Cohesion:** 0.09 - loosely connected
**Members:** 33 nodes

## Members
- [[.__init__()_103]] - code - gateway/runtime/podman_engine.py
- [[._cmd()]] - code - gateway/runtime/podman_engine.py
- [[._detect_compose()]] - code - gateway/runtime/podman_engine.py
- [[.build()_1]] - code - gateway/runtime/podman_engine.py
- [[.compose_down()_1]] - code - gateway/runtime/podman_engine.py
- [[.compose_up()_1]] - code - gateway/runtime/podman_engine.py
- [[.exec()_1]] - code - gateway/runtime/podman_engine.py
- [[.generate_systemd()]] - code - gateway/runtime/podman_engine.py
- [[.health_check()_3]] - code - gateway/runtime/podman_engine.py
- [[.inspect()_1]] - code - gateway/runtime/podman_engine.py
- [[.logs()_1]] - code - gateway/runtime/podman_engine.py
- [[.network_create()_1]] - code - gateway/runtime/podman_engine.py
- [[.network_rm()_1]] - code - gateway/runtime/podman_engine.py
- [[.pause()_1]] - code - gateway/runtime/podman_engine.py
- [[.pull()_1]] - code - gateway/runtime/podman_engine.py
- [[.push()_2]] - code - gateway/runtime/podman_engine.py
- [[.rm()_1]] - code - gateway/runtime/podman_engine.py
- [[.run()_2]] - code - gateway/runtime/podman_engine.py
- [[.setup_method()_26]] - code - gateway/tests/test_runtime_engines.py
- [[.stop()_7]] - code - gateway/runtime/podman_engine.py
- [[.test_generate_systemd()]] - code - gateway/tests/test_runtime_engines.py
- [[.test_health_check()]] - code - gateway/tests/test_runtime_engines.py
- [[.test_ps_json()]] - code - gateway/tests/test_runtime_engines.py
- [[.test_run_selinux_volumes()]] - code - gateway/tests/test_runtime_engines.py
- [[.unpause()_1]] - code - gateway/runtime/podman_engine.py
- [[.volume_create()_1]] - code - gateway/runtime/podman_engine.py
- [[.volume_rm()_1]] - code - gateway/runtime/podman_engine.py
- [[Any_38]] - code - gateway/runtime/podman_engine.py
- [[Container engine backed by the Podman CLI.]] - rationale - gateway/runtime/podman_engine.py
- [[Detect podman compose or podman-compose.]] - rationale - gateway/runtime/podman_engine.py
- [[Generate a systemd unit file for a container.]] - rationale - gateway/runtime/podman_engine.py
- [[PodmanEngine]] - code - gateway/runtime/podman_engine.py
- [[TestPodmanEngine]] - code - gateway/tests/test_runtime_engines.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/PodmanEngine
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_test_runtime_engines.py]]
- 5 edges to [[_COMMUNITY_ContainerInfo]]
- 3 edges to [[_COMMUNITY_RuntimeConfig]]
- 2 edges to [[_COMMUNITY_ContainerEngine]]
- 2 edges to [[_COMMUNITY_get_engine()]]
- 2 edges to [[_COMMUNITY_DockerEngine]]
- 1 edge to [[_COMMUNITY_TestInstallerAPI]]
- 1 edge to [[_COMMUNITY_TestAppleContainerEngine]]
- 1 edge to [[_COMMUNITY_detect_runtime()]]
- 1 edge to [[_COMMUNITY_TestDockerEngine]]
- 1 edge to [[_COMMUNITY_TestSecurityFeatures]]
- 1 edge to [[_COMMUNITY_TestWebAPI]]
- 1 edge to [[_COMMUNITY_AppleContainerEngine]]

## Top bridge nodes
- [[PodmanEngine]] - degree 45, connects to 12 communities
- [[TestPodmanEngine]] - degree 11, connects to 4 communities
- [[Any_38]] - degree 3, connects to 2 communities