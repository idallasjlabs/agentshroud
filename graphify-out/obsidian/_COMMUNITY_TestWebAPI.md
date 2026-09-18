---
type: community
cohesion: 0.13
members: 15
---

# TestWebAPI

**Cohesion:** 0.13 - loosely connected
**Members:** 15 nodes

## Members
- [[.client()_6]] - code - gateway/tests/test_runtime_engines.py
- [[.test_check_agentshroud_updates()]] - code - gateway/tests/test_runtime_engines.py
- [[.test_check_openclaw_updates()]] - code - gateway/tests/test_runtime_engines.py
- [[.test_export_config()]] - code - gateway/tests/test_runtime_engines.py
- [[.test_get_config()]] - code - gateway/tests/test_runtime_engines.py
- [[.test_get_logs()]] - code - gateway/tests/test_runtime_engines.py
- [[.test_killswitch_freeze()]] - code - gateway/tests/test_runtime_engines.py
- [[.test_killswitch_invalid_mode()]] - code - gateway/tests/test_runtime_engines.py
- [[.test_killswitch_no_confirm()]] - code - gateway/tests/test_runtime_engines.py
- [[.test_security_report()]] - code - gateway/tests/test_runtime_engines.py
- [[.test_status()]] - code - gateway/tests/test_runtime_engines.py
- [[.test_stop_service()]] - code - gateway/tests/test_runtime_engines.py
- [[.test_update_history()]] - code - gateway/tests/test_runtime_engines.py
- [[Test the management API endpoints with mocked runtime.]] - rationale - gateway/tests/test_runtime_engines.py
- [[TestWebAPI]] - code - gateway/tests/test_runtime_engines.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestWebAPI
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_test_runtime_engines.py]]
- 1 edge to [[_COMMUNITY_ContainerInfo]]
- 1 edge to [[_COMMUNITY_PodmanEngine]]
- 1 edge to [[_COMMUNITY_DockerEngine]]
- 1 edge to [[_COMMUNITY_AppleContainerEngine]]

## Top bridge nodes
- [[TestWebAPI]] - degree 20, connects to 5 communities