---
type: community
cohesion: 0.09
members: 33
---

# Podman Engine (runtime)

**Cohesion:** 0.09 - loosely connected
**Members:** 33 nodes

## Members
- [[.__init__()_48]] - code - gateway/runtime/podman_engine.py
- [[._cmd()_2]] - code - gateway/runtime/podman_engine.py
- [[._detect_compose()]] - code - gateway/runtime/podman_engine.py
- [[.build()_3]] - code - gateway/runtime/podman_engine.py
- [[.compose_down()_3]] - code - gateway/runtime/podman_engine.py
- [[.compose_up()_3]] - code - gateway/runtime/podman_engine.py
- [[.exec()_3]] - code - gateway/runtime/podman_engine.py
- [[.generate_systemd()]] - code - gateway/runtime/podman_engine.py
- [[.health_check()_5]] - code - gateway/runtime/podman_engine.py
- [[.inspect()_3]] - code - gateway/runtime/podman_engine.py
- [[.logs()_3]] - code - gateway/runtime/podman_engine.py
- [[.network_create()_3]] - code - gateway/runtime/podman_engine.py
- [[.network_rm()_3]] - code - gateway/runtime/podman_engine.py
- [[.pause()_3]] - code - gateway/runtime/podman_engine.py
- [[.pull()_3]] - code - gateway/runtime/podman_engine.py
- [[.push()_3]] - code - gateway/runtime/podman_engine.py
- [[.rm()_3]] - code - gateway/runtime/podman_engine.py
- [[.run()_3]] - code - gateway/runtime/podman_engine.py
- [[.setup_method()_24]] - code - gateway/tests/test_runtime_engines.py
- [[.stop()_8]] - code - gateway/runtime/podman_engine.py
- [[.test_generate_systemd()]] - code - gateway/tests/test_runtime_engines.py
- [[.test_health_check()]] - code - gateway/tests/test_runtime_engines.py
- [[.test_ps_json()]] - code - gateway/tests/test_runtime_engines.py
- [[.test_run_selinux_volumes()]] - code - gateway/tests/test_runtime_engines.py
- [[.unpause()_3]] - code - gateway/runtime/podman_engine.py
- [[.volume_create()_3]] - code - gateway/runtime/podman_engine.py
- [[.volume_rm()_3]] - code - gateway/runtime/podman_engine.py
- [[Any_28]] - code - gateway/runtime/podman_engine.py
- [[Container engine backed by the Podman CLI.]] - rationale - gateway/runtime/podman_engine.py
- [[Detect podman compose or podman-compose.]] - rationale - gateway/runtime/podman_engine.py
- [[Generate a systemd unit file for a container.]] - rationale - gateway/runtime/podman_engine.py
- [[PodmanEngine]] - code - gateway/runtime/podman_engine.py
- [[TestPodmanEngine]] - code - gateway/tests/test_runtime_engines.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Podman_Engine_runtime
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_Runtime Engines]]
- 5 edges to [[_COMMUNITY_Engine (runtime)]]
- 3 edges to [[_COMMUNITY_Runtime Engines]]
- 2 edges to [[_COMMUNITY_Runtime Engines]]
- 2 edges to [[_COMMUNITY_Docker Engine (runtime)]]
- 2 edges to [[_COMMUNITY_Engine (runtime)]]
- 1 edge to [[_COMMUNITY_Apple Engine (runtime)]]
- 1 edge to [[_COMMUNITY_Runtime Engines]]
- 1 edge to [[_COMMUNITY_Installer (web)]]
- 1 edge to [[_COMMUNITY_Runtime Engines]]
- 1 edge to [[_COMMUNITY_Runtime Engines]]
- 1 edge to [[_COMMUNITY_Runtime Engines]]
- 1 edge to [[_COMMUNITY_Runtime Engines]]

## Top bridge nodes
- [[PodmanEngine]] - degree 45, connects to 12 communities
- [[TestPodmanEngine]] - degree 11, connects to 4 communities
- [[Any_28]] - degree 3, connects to 2 communities