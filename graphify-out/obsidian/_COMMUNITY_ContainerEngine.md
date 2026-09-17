---
type: community
cohesion: 0.06
members: 35
---

# ContainerEngine

**Cohesion:** 0.06 - loosely connected
**Members:** 35 nodes

## Members
- [[._run()]] - code - gateway/runtime/engine.py
- [[.build()]] - code - gateway/runtime/engine.py
- [[.compose_down()]] - code - gateway/runtime/engine.py
- [[.compose_up()]] - code - gateway/runtime/engine.py
- [[.exec()]] - code - gateway/runtime/engine.py
- [[.health_check()]] - code - gateway/runtime/engine.py
- [[.inspect()]] - code - gateway/runtime/engine.py
- [[.logs()]] - code - gateway/runtime/engine.py
- [[.network_create()]] - code - gateway/runtime/engine.py
- [[.network_rm()]] - code - gateway/runtime/engine.py
- [[.pause()]] - code - gateway/runtime/engine.py
- [[.pull()]] - code - gateway/runtime/engine.py
- [[.push()_1]] - code - gateway/runtime/engine.py
- [[.rm()]] - code - gateway/runtime/engine.py
- [[.stop()]] - code - gateway/runtime/engine.py
- [[.unpause()]] - code - gateway/runtime/engine.py
- [[.volume_create()]] - code - gateway/runtime/engine.py
- [[.volume_rm()]] - code - gateway/runtime/engine.py
- [[ABC]] - code
- [[Any_10]] - code - gateway/runtime/engine.py
- [[Bring up services from a compose file.]] - rationale - gateway/runtime/engine.py
- [[Build an image. Returns the image idtag.]] - rationale - gateway/runtime/engine.py
- [[CompletedProcess_1]] - code - gateway/runtime/engine.py
- [[ContainerEngine]] - code - gateway/runtime/engine.py
- [[Execute a command inside a running container.]] - rationale - gateway/runtime/engine.py
- [[Pull an image from a registry.]] - rationale - gateway/runtime/engine.py
- [[Push an image to a registry.]] - rationale - gateway/runtime/engine.py
- [[Retrieve container logs.]] - rationale - gateway/runtime/engine.py
- [[Return True if the runtime is available and responsive.]] - rationale - gateway/runtime/engine.py
- [[Return detailed container metadata.]] - rationale - gateway/runtime/engine.py
- [[Run a CLI command and return the result.]] - rationale - gateway/runtime/engine.py
- [[Start a container. Returns container id.]] - rationale - gateway/runtime/engine.py
- [[Stop a running container.]] - rationale - gateway/runtime/engine.py
- [[Tear down services from a compose file.]] - rationale - gateway/runtime/engine.py
- [[Unified interface for container runtimes (Docker  Podman  Apple Containers).]] - rationale - gateway/runtime/engine.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/ContainerEngine
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_RuntimeConfig]]
- 4 edges to [[_COMMUNITY_ContainerInfo]]
- 2 edges to [[_COMMUNITY_AppleContainerEngine]]
- 2 edges to [[_COMMUNITY_DockerEngine]]
- 2 edges to [[_COMMUNITY_PodmanEngine]]
- 1 edge to [[_COMMUNITY_get_engine()]]

## Top bridge nodes
- [[ContainerEngine]] - degree 36, connects to 6 communities
- [[ABC]] - degree 2, connects to 1 community