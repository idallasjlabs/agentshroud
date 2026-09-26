---
type: community
cohesion: 0.18
members: 19
---

# ADR-009: Enforce-by-Default Security Philosophy

**Cohesion:** 0.18 - loosely connected
**Members:** 19 nodes

## Members
- [[.effective_rootless()]] - code - gateway/runtime/config.py
- [[.test_effective_rootless_docker()]] - code - gateway/tests/test_runtime_engines.py
- [[.test_effective_rootless_override()]] - code - gateway/tests/test_runtime_engines.py
- [[.test_effective_rootless_podman()]] - code - gateway/tests/test_runtime_engines.py
- [[.test_from_dict()]] - code - gateway/tests/test_runtime_engines.py
- [[.test_from_env_defaults()]] - code - gateway/tests/test_runtime_engines.py
- [[.test_from_env_set()]] - code - gateway/tests/test_runtime_engines.py
- [[Configuration for container runtime selection and behavior.      Loaded from env]] - rationale - gateway/runtime/config.py
- [[Resolve rootless setting based on runtime.]] - rationale - gateway/runtime/config.py
- [[RuntimeConfig]] - code - gateway/runtime/config.py
- [[TestRuntimeConfig]] - code - gateway/tests/test_runtime_engines.py
- [[__init__.py_8]] - code - gateway/runtime/__init__.py
- [[apple_engine.py]] - code - gateway/runtime/apple_engine.py
- [[compose_generator.py]] - code - gateway/runtime/compose_generator.py
- [[config.py_1]] - code - gateway/runtime/config.py
- [[docker_engine.py]] - code - gateway/runtime/docker_engine.py
- [[engine.py]] - code - gateway/runtime/engine.py
- [[podman_engine.py]] - code - gateway/runtime/podman_engine.py
- [[security.py]] - code - gateway/runtime/security.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/ADR-009_Enforce-by-Default_Security_Philosophy
SORT file.name ASC
```

## Connections to other communities
- 11 edges to [[_COMMUNITY_export-bot-conversations.py]]
- 6 edges to [[_COMMUNITY_WebhookReceiver]]
- 5 edges to [[_COMMUNITY_api.py]]
- 5 edges to [[_COMMUNITY_TestObservatoryMode]]
- 3 edges to [[_COMMUNITY_iCloud Services]]
- 3 edges to [[_COMMUNITY_DELIVERABLE 1 — Domain-by-Domain Assessment]]
- 3 edges to [[_COMMUNITY_GatewayEmailService]]
- 2 edges to [[_COMMUNITY_get_trivy_summary()]]
- 2 edges to [[_COMMUNITY_TestAlertDispatcher]]
- 2 edges to [[_COMMUNITY_OpenClaw Setup Guide - agentshroud.ai Bot]]
- 1 edge to [[_COMMUNITY_REPORT STRUCTURE]]

## Top bridge nodes
- [[__init__.py_8]] - degree 10, connects to 6 communities
- [[TestRuntimeConfig]] - degree 12, connects to 4 communities
- [[docker_engine.py]] - degree 9, connects to 4 communities
- [[podman_engine.py]] - degree 9, connects to 4 communities
- [[RuntimeConfig]] - degree 13, connects to 3 communities