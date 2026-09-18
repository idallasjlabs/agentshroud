---
type: community
cohesion: 0.14
members: 24
---

# AppleContainerEngine

**Cohesion:** 0.14 - loosely connected
**Members:** 24 nodes

## Members
- [[.__init__()_138]] - code - gateway/runtime/apple_engine.py
- [[._cmd()_2]] - code - gateway/runtime/apple_engine.py
- [[.build()_3]] - code - gateway/runtime/apple_engine.py
- [[.compose_down()_3]] - code - gateway/runtime/apple_engine.py
- [[.compose_up()_3]] - code - gateway/runtime/apple_engine.py
- [[.exec()_3]] - code - gateway/runtime/apple_engine.py
- [[.health_check()_5]] - code - gateway/runtime/apple_engine.py
- [[.inspect()_3]] - code - gateway/runtime/apple_engine.py
- [[.logs()_3]] - code - gateway/runtime/apple_engine.py
- [[.network_create()_3]] - code - gateway/runtime/apple_engine.py
- [[.network_rm()_3]] - code - gateway/runtime/apple_engine.py
- [[.pause()_3]] - code - gateway/runtime/apple_engine.py
- [[.pull()_3]] - code - gateway/runtime/apple_engine.py
- [[.push()_4]] - code - gateway/runtime/apple_engine.py
- [[.rm()_3]] - code - gateway/runtime/apple_engine.py
- [[.run()_5]] - code - gateway/runtime/apple_engine.py
- [[.stop()_9]] - code - gateway/runtime/apple_engine.py
- [[.unpause()_3]] - code - gateway/runtime/apple_engine.py
- [[.volume_create()_3]] - code - gateway/runtime/apple_engine.py
- [[.volume_rm()_3]] - code - gateway/runtime/apple_engine.py
- [[Any_48]] - code - gateway/runtime/apple_engine.py
- [[AppleContainerEngine]] - code - gateway/runtime/apple_engine.py
- [[Container engine backed by Apple's `container` CLI.]] - rationale - gateway/runtime/apple_engine.py
- [[get_engine]] - code - gateway/runtime/__init__.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/AppleContainerEngine
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_test_runtime_engines.py]]
- 4 edges to [[_COMMUNITY_ContainerInfo]]
- 3 edges to [[_COMMUNITY_RuntimeConfig]]
- 2 edges to [[_COMMUNITY_ContainerEngine]]
- 2 edges to [[_COMMUNITY_get_engine()]]
- 2 edges to [[_COMMUNITY_TestAppleContainerEngine]]
- 1 edge to [[_COMMUNITY_TestInstallerAPI]]
- 1 edge to [[_COMMUNITY_PodmanEngine]]
- 1 edge to [[_COMMUNITY_DockerEngine]]
- 1 edge to [[_COMMUNITY_detect_runtime()]]
- 1 edge to [[_COMMUNITY_TestDockerEngine]]
- 1 edge to [[_COMMUNITY_TestSecurityFeatures]]
- 1 edge to [[_COMMUNITY_TestWebAPI]]

## Top bridge nodes
- [[AppleContainerEngine]] - degree 45, connects to 13 communities
- [[Any_48]] - degree 3, connects to 2 communities