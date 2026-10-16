---
type: community
cohesion: 0.11
members: 24
---

# AgentTarget

**Cohesion:** 0.11 - loosely connected
**Members:** 24 nodes

## Members
- [[dot-__init__()_135]] - code - gateway/ingest_api/router.py
- [[dot-_build_forward_payload()]] - code - gateway/ingest_api/router.py
- [[dot-forward_to_agent()]] - code - gateway/ingest_api/router.py
- [[dot-forward_to_agent_stream()]] - code - gateway/ingest_api/router.py
- [[dot-health_check()_4]] - code - gateway/ingest_api/router.py
- [[dot-list_targets()]] - code - gateway/ingest_api/router.py
- [[dot-register_bots()]] - code - gateway/ingest_api/router.py
- [[dot-resolve_target()]] - code - gateway/ingest_api/router.py
- [[AgentShroud Secure Chat Interface (static HTMLJS)]] - code - gateway/ingest_api/static/chat.html
- [[AgentTarget_2]] - code - gateway/ingest_api/router.py
- [[Any_55]] - code - gateway/ingest_api/router.py
- [[Build the outbound payload for `target`, shared by the blocking and         stre]] - rationale - gateway/ingest_api/router.py
- [[Check health of one or all agent targets          Args             target Spec]] - rationale - gateway/ingest_api/router.py
- [[Determine which agent should receive this content          Args             req]] - rationale - gateway/ingest_api/router.py
- [[Forward sanitized content to agent via HTTP POST          Args             targ]] - rationale - gateway/ingest_api/router.py
- [[ForwardRequest_1]] - code - gateway/ingest_api/router.py
- [[Initialize router          Args             config Router configuration]] - rationale - gateway/ingest_api/router.py
- [[Populate routing targets from the bots registry.          Iterates all BotConfig]] - rationale - gateway/ingest_api/router.py
- [[Raised when no valid routing target found]] - rationale - gateway/ingest_api/router.py
- [[Return all configured agent targets          Returns             List of AgentT]] - rationale - gateway/ingest_api/router.py
- [[RouterConfig]] - code - gateway/ingest_api/router.py
- [[RouterError]] - code - gateway/ingest_api/router.py
- [[Stream sanitized content to an OpenAI-compatible agent, yielding text         de]] - rationale - gateway/ingest_api/router.py
- [[sendMessage() JS — POST forward from browser chat UI]] - code - gateway/ingest_api/static/chat.html

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/AgentTarget
SORT file.name ASC
```

## Connections to other communities
- 14 edges to [[_COMMUNITY_DataLedger]]
- 5 edges to [[_COMMUNITY_AgentTarget]]
- 5 edges to [[_COMMUNITY_ForwardRequest]]
- 2 edges to [[_COMMUNITY_test_forward_stream.py]]
- 1 edge to [[_COMMUNITY_ThreatAssessment]]

## Top bridge nodes
- [[RouterError]] - degree 7, connects to 4 communities
- [[AgentTarget_2]] - degree 11, connects to 3 communities
- [[Any_55]] - degree 7, connects to 3 communities
- [[ForwardRequest_1]] - degree 4, connects to 3 communities
- [[RouterConfig]] - degree 4, connects to 3 communities
