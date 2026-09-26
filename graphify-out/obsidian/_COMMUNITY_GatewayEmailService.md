---
type: community
cohesion: 0.11
members: 29
---

# GatewayEmailService

**Cohesion:** 0.11 - loosely connected
**Members:** 29 nodes

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
- [[.ps()_3]] - code - gateway/runtime/podman_engine.py
- [[.pull()_3]] - code - gateway/runtime/podman_engine.py
- [[.push()_3]] - code - gateway/runtime/podman_engine.py
- [[.rm()_3]] - code - gateway/runtime/podman_engine.py
- [[.run()_3]] - code - gateway/runtime/podman_engine.py
- [[.stop()_8]] - code - gateway/runtime/podman_engine.py
- [[.unpause()_3]] - code - gateway/runtime/podman_engine.py
- [[.volume_create()_3]] - code - gateway/runtime/podman_engine.py
- [[.volume_rm()_3]] - code - gateway/runtime/podman_engine.py
- [[Any_28]] - code - gateway/runtime/podman_engine.py
- [[Container engine backed by the Podman CLI.]] - rationale - gateway/runtime/podman_engine.py
- [[ContainerInfo_3]] - code - gateway/runtime/podman_engine.py
- [[Detect podman compose or podman-compose.]] - rationale - gateway/runtime/podman_engine.py
- [[Generate a systemd unit file for a container.]] - rationale - gateway/runtime/podman_engine.py
- [[PodmanEngine]] - code - gateway/runtime/podman_engine.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/GatewayEmailService
SORT file.name ASC
```

## Connections to other communities
- 10 edges to [[_COMMUNITY_export-bot-conversations.py]]
- 3 edges to [[_COMMUNITY_ADR-009 Enforce-by-Default Security Philosophy]]
- 3 edges to [[_COMMUNITY_WebhookReceiver]]
- 2 edges to [[_COMMUNITY_REPORT STRUCTURE]]
- 1 edge to [[_COMMUNITY_DELIVERABLE 1 — Domain-by-Domain Assessment]]
- 1 edge to [[_COMMUNITY_🟠 HIGH Security & Logic Issues]]
- 1 edge to [[_COMMUNITY_get_trivy_summary()]]
- 1 edge to [[_COMMUNITY_setup-secrets.sh]]
- 1 edge to [[_COMMUNITY_i-icloud SKILL — iCloud Services]]
- 1 edge to [[_COMMUNITY_TestObservatoryMode]]
- 1 edge to [[_COMMUNITY_Skill Audit Branch (AB) — Merge Regression Dete]]

## Top bridge nodes
- [[PodmanEngine]] - degree 45, connects to 11 communities
- [[Any_28]] - degree 3, connects to 2 communities
- [[ContainerInfo_3]] - degree 3, connects to 2 communities