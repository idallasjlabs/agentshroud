---
type: community
cohesion: 0.13
members: 24
---

# DockerEngine

**Cohesion:** 0.13 - loosely connected
**Members:** 24 nodes

## Members
- [[.__init__()_137]] - code - gateway/runtime/docker_engine.py
- [[._cmd()_1]] - code - gateway/runtime/docker_engine.py
- [[.build()_2]] - code - gateway/runtime/docker_engine.py
- [[.compose_down()_2]] - code - gateway/runtime/docker_engine.py
- [[.compose_up()_2]] - code - gateway/runtime/docker_engine.py
- [[.exec()_2]] - code - gateway/runtime/docker_engine.py
- [[.health_check()_4]] - code - gateway/runtime/docker_engine.py
- [[.inspect()_2]] - code - gateway/runtime/docker_engine.py
- [[.logs()_2]] - code - gateway/runtime/docker_engine.py
- [[.network_create()_2]] - code - gateway/runtime/docker_engine.py
- [[.network_rm()_2]] - code - gateway/runtime/docker_engine.py
- [[.pause()_2]] - code - gateway/runtime/docker_engine.py
- [[.pull()_2]] - code - gateway/runtime/docker_engine.py
- [[.push()_3]] - code - gateway/runtime/docker_engine.py
- [[.rm()_2]] - code - gateway/runtime/docker_engine.py
- [[.run()_4]] - code - gateway/runtime/docker_engine.py
- [[.stop()_8]] - code - gateway/runtime/docker_engine.py
- [[.unpause()_2]] - code - gateway/runtime/docker_engine.py
- [[.volume_create()_2]] - code - gateway/runtime/docker_engine.py
- [[.volume_rm()_2]] - code - gateway/runtime/docker_engine.py
- [[Any_47]] - code - gateway/runtime/docker_engine.py
- [[Container engine backed by the Docker CLI.]] - rationale - gateway/runtime/docker_engine.py
- [[ContainerEngine_1]] - code
- [[DockerEngine]] - code - gateway/runtime/docker_engine.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/DockerEngine
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_ContainerInfo]]
- 4 edges to [[_COMMUNITY_test_runtime_engines.py]]
- 3 edges to [[_COMMUNITY_RuntimeConfig]]
- 2 edges to [[_COMMUNITY_ContainerEngine]]
- 2 edges to [[_COMMUNITY_PodmanEngine]]
- 2 edges to [[_COMMUNITY_get_engine()]]
- 2 edges to [[_COMMUNITY_TestDockerEngine]]
- 1 edge to [[_COMMUNITY_TestInstallerAPI]]
- 1 edge to [[_COMMUNITY_AppleContainerEngine]]
- 1 edge to [[_COMMUNITY_TestAppleContainerEngine]]
- 1 edge to [[_COMMUNITY_detect_runtime()]]
- 1 edge to [[_COMMUNITY_TestSecurityFeatures]]
- 1 edge to [[_COMMUNITY_TestWebAPI]]

## Top bridge nodes
- [[DockerEngine]] - degree 43, connects to 12 communities
- [[ContainerEngine_1]] - degree 3, connects to 2 communities
- [[Any_47]] - degree 3, connects to 2 communities