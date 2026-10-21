---
type: community
members: 10
---

# Workflow (follow in order)

**Members:** 10 nodes

## Members
- [[dot-test_auto_detect_priority()]] - code - gateway/tests/test_runtime_engines.py
- [[dot-test_explicit_apple()]] - code - gateway/tests/test_runtime_engines.py
- [[dot-test_explicit_docker()]] - code - gateway/tests/test_runtime_engines.py
- [[dot-test_explicit_podman()]] - code - gateway/tests/test_runtime_engines.py
- [[dot-test_invalid_runtime()]] - code - gateway/tests/test_runtime_engines.py
- [[dot-test_no_runtime_available()]] - code - gateway/tests/test_runtime_engines.py
- [[ContainerEngine_2]] - code - gateway/runtime/__init__.py
- [[Return an appropriate container engine instance.      Args         preference]] - rationale - gateway/runtime/__init__.py
- [[TestGetEngine_1]] - code - gateway/tests/test_runtime_engines.py
- [[get_engine()]] - code - gateway/runtime/__init__.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Workflow_follow_in_order
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_jira_weekly_review.py]]
- 3 edges to [[_COMMUNITY_MCPPolicyEngine]]
- 2 edges to [[_COMMUNITY_setup-secrets.sh]]
- 2 edges to [[_COMMUNITY_Approval Queue (human-in-the-loop)]]
- 2 edges to [[_COMMUNITY_AppleContainerEngine]]
- 1 edge to [[_COMMUNITY_lifespan()]]
- 1 edge to [[_COMMUNITY_MiddlewareManager (6)]]
- 1 edge to [[_COMMUNITY_pipeline.py — Security Pipeline]]
- 1 edge to [[_COMMUNITY_test_soc_router_coverage.py]]
- 1 edge to [[_COMMUNITY_egress_retry.py]]

## Top bridge nodes
- [[get_engine()]] - degree 16, connects to 5 communities
- [[TestGetEngine_1]] - degree 12, connects to 5 communities
- [[ContainerEngine_2]] - degree 5, connects to 4 communities
