---
type: community
cohesion: 0.18
members: 12
---

# Module Group 330

**Cohesion:** 0.18 - loosely connected
**Members:** 12 nodes

## Members
- [[FR-001 PII Detection and Sanitization (10ms latency)]] - concept - docs/requirements/system-requirements.md
- [[FR-007 Kill Switch emergency shutdown mechanism]] - concept - docs/requirements/system-requirements.md
- [[FR-009 Immutable audit logs with hash chain, JSON format]] - concept - docs/requirements/system-requirements.md
- [[NFR-001 50ms additional latency per request (95th percentile)]] - concept - docs/requirements/system-requirements.md
- [[NFR-002 99.9% uptime target]] - concept - docs/requirements/system-requirements.md
- [[System Requirements Specification (SRS) v0.9.0]] - document - docs/requirements/system-requirements.md
- [[UC-001 User Sends Message — PII Sanitization Flow]] - concept - docs/requirements/use-cases.md
- [[UC-002 Agent Calls MCP Tool — Inspection + Permission Check]] - concept - docs/requirements/use-cases.md
- [[UC-004 Admin Activates Kill Switch]] - concept - docs/requirements/use-cases.md
- [[UC-005 Agent Requests SSH Access via Approval Queue]] - concept - docs/requirements/use-cases.md
- [[UC-007 New Agent Onboarding — Trust Level 0]] - concept - docs/requirements/use-cases.md
- [[Use Cases Document (10 use cases for AgentShroud security proxy)]] - document - docs/requirements/use-cases.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_330
SORT file.name ASC
```
