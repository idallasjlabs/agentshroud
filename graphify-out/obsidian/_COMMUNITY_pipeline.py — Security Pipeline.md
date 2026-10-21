---
type: community
members: 19
---

# pipeline.py — Security Pipeline

**Members:** 19 nodes

## Members
- [[dot-effective_rootless()]] - code - gateway/runtime/config.py
- [[dot-test_effective_rootless_docker()]] - code - gateway/tests/test_runtime_engines.py
- [[dot-test_effective_rootless_override()]] - code - gateway/tests/test_runtime_engines.py
- [[dot-test_effective_rootless_podman()]] - code - gateway/tests/test_runtime_engines.py
- [[dot-test_from_dict()]] - code - gateway/tests/test_runtime_engines.py
- [[dot-test_from_env_defaults()]] - code - gateway/tests/test_runtime_engines.py
- [[dot-test_from_env_set()]] - code - gateway/tests/test_runtime_engines.py
- [[Configuration for container runtime selection and behavior.      Loaded from env]] - rationale - gateway/runtime/config.py
- [[Resolve rootless setting based on runtime.]] - rationale - gateway/runtime/config.py
- [[RuntimeConfig]] - code - gateway/runtime/config.py
- [[TestRuntimeConfig]] - code - gateway/tests/test_runtime_engines.py
- [[apple_engine.py]] - code - gateway/runtime/apple_engine.py
- [[compose_generator.py]] - code - gateway/runtime/compose_generator.py
- [[docker_engine.py]] - code - gateway/runtime/docker_engine.py
- [[engine.py]] - code - gateway/runtime/engine.py
- [[podman_engine.py]] - code - gateway/runtime/podman_engine.py
- [[runtime__init__.py]] - code - gateway/runtime/__init__.py
- [[runtimeconfig.py]] - code - gateway/runtime/config.py
- [[security.py]] - code - gateway/runtime/security.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/pipelinepy__Security_Pipeline
SORT file.name ASC
```

## Connections to other communities
- 7 edges to [[_COMMUNITY_jira_weekly_review.py]]
- 6 edges to [[_COMMUNITY_MiddlewareManager (6)]]
- 5 edges to [[_COMMUNITY_MCPPolicyEngine]]
- 5 edges to [[_COMMUNITY__get_gmail_app_password]]
- 5 edges to [[_COMMUNITY_egress_retry.py]]
- 3 edges to [[_COMMUNITY_setup-secrets.sh]]
- 3 edges to [[_COMMUNITY_Approval Queue (human-in-the-loop)]]
- 3 edges to [[_COMMUNITY_AppleContainerEngine]]
- 2 edges to [[_COMMUNITY_AlertTelegramRelay]]
- 2 edges to [[_COMMUNITY_Skill MCP Doctor (MCPM-DOCTOR)]]
- 1 edge to [[_COMMUNITY_Workflow (follow in order)]]

## Top bridge nodes
- [[runtime__init__.py]] - degree 10, connects to 6 communities
- [[TestRuntimeConfig]] - degree 12, connects to 5 communities
- [[docker_engine.py]] - degree 9, connects to 4 communities
- [[podman_engine.py]] - degree 9, connects to 4 communities
- [[RuntimeConfig]] - degree 13, connects to 3 communities
