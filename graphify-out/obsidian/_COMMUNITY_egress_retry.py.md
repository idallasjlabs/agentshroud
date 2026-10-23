---
type: community
cohesion: 0.20
members: 12
---

# egress_retry.py

**Cohesion:** 0.20 - loosely connected
**Members:** 12 nodes

## Members
- [[dot-ps()]] - code - gateway/runtime/apple_engine.py
- [[dot-ps()_1]] - code - gateway/runtime/docker_engine.py
- [[dot-ps()_2]] - code - gateway/runtime/engine.py
- [[dot-ps()_3]] - code - gateway/runtime/podman_engine.py
- [[dot-test_defaults()_2]] - code - gateway/tests/test_runtime_engines.py
- [[dot-test_with_data()]] - code - gateway/tests/test_runtime_engines.py
- [[ContainerInfo]] - code - gateway/runtime/apple_engine.py
- [[ContainerInfo_1]] - code - gateway/runtime/docker_engine.py
- [[ContainerInfo_2]] - code - gateway/runtime/podman_engine.py
- [[ContainerInfo_3]] - code - gateway/runtime/engine.py
- [[Lightweight container metadata returned by psinspect.]] - rationale - gateway/runtime/engine.py
- [[TestContainerInfo]] - code - gateway/tests/test_runtime_engines.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/egress_retrypy
SORT file.name ASC
```

## Connections to other communities
- 7 edges to [[_COMMUNITY_jira_weekly_review.py]]
- 5 edges to [[_COMMUNITY_PodmanEngine]]
- 5 edges to [[_COMMUNITY_pipeline.py — Security Pipeline]]
- 4 edges to [[_COMMUNITY_MiddlewareManager (6)]]
- 4 edges to [[_COMMUNITY_Approval Queue (human-in-the-loop)]]
- 4 edges to [[_COMMUNITY_AppleContainerEngine]]
- 1 edge to [[_COMMUNITY_hermesskillsi-browserbrowse.js]]
- 1 edge to [[_COMMUNITY_AgentShroud v1.2.0 Master Plan]]
- 1 edge to [[_COMMUNITY__get_gmail_app_password]]
- 1 edge to [[_COMMUNITY_tts.py]]
- 1 edge to [[_COMMUNITY_server.py]]
- 1 edge to [[_COMMUNITY_Workflow (follow in order)]]

## Top bridge nodes
- [[ContainerInfo_3]] - degree 31, connects to 11 communities
- [[TestContainerInfo]] - degree 8, connects to 4 communities
- [[ContainerInfo]] - degree 3, connects to 1 community
- [[ContainerInfo_1]] - degree 3, connects to 1 community
- [[ContainerInfo_2]] - degree 3, connects to 1 community
