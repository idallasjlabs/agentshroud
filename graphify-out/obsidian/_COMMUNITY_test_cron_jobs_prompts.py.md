---
type: community
cohesion: 0.15
members: 17
---

# test_cron_jobs_prompts.py

**Cohesion:** 0.15 - loosely connected
**Members:** 17 nodes

## Members
- [[1Password (credential vault)]] - image - docs/diagrams/images/diagram-01-c4-context.svg
- [[1Password Integration (service account)]] - document - docs/api/integration-guide.md
- [[ADR-004 Proxy-Side API Key Management]] - concept - docs/architecture/adr/ADR-004-api-keys-never-in-agent-container.md
- [[AgentShroud (system, C4 context)]] - image - docs/diagrams/images/diagram-01-c4-context.svg
- [[AgentShroud Bot Container (Node.js 22OpenClaw 18789)]] - image - docs/diagrams/images/diagram-02-c4-container.svg
- [[Anthropic API (external system)]] - image - docs/diagrams/images/diagram-01-c4-context.svg
- [[Brave Search API (external system)]] - image - docs/diagrams/images/diagram-01-c4-context.svg
- [[External Collaborators]] - image - docs/diagrams/images/diagram-01-c4-context.svg
- [[Gateway (FastAPI)]] - concept - docs/architecture/system-architecture.md
- [[Gateway Container (Python 3.11FastAPI 8080)]] - image - docs/diagrams/images/diagram-02-c4-container.svg
- [[GitHub (external system)]] - image - docs/diagrams/images/diagram-01-c4-context.svg
- [[Isaiah Jefferson (ArchitectOwner)]] - image - docs/diagrams/images/diagram-01-c4-context.svg
- [[OpenAI API (external system)]] - image - docs/diagrams/images/diagram-01-c4-context.svg
- [[PII Sanitizer (Presidio + Regex)]] - concept - docs/architecture/system-architecture.md
- [[Running Containers (gateway + bot, healthy)]] - image - docs/diagrams/images/diagram-06-cicd-deployment.svg
- [[Telegram (external system)]] - image - docs/diagrams/images/diagram-01-c4-context.svg
- [[sanitizer.py (PII redaction, Presidioregex)]] - image - docs/diagrams/images/diagram-03-gateway-components.svg

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_cron_jobs_promptspy
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_container-net-diag.sh]]
- 1 edge to [[_COMMUNITY_OpenClaw Setup Guide - agentshroud.ai Bot]]
- 1 edge to [[_COMMUNITY_TestAppleContainerEngine]]
- 1 edge to [[_COMMUNITY_Phase Review P0 — Core Pipeline Wiring]]
- 1 edge to [[_COMMUNITY_1.4 Implementation Plan]]

## Top bridge nodes
- [[Gateway Container (Python 3.11FastAPI 8080)]] - degree 9, connects to 2 communities
- [[AgentShroud (system, C4 context)]] - degree 9, connects to 1 community
- [[Gateway (FastAPI)]] - degree 4, connects to 1 community
- [[PII Sanitizer (Presidio + Regex)]] - degree 3, connects to 1 community