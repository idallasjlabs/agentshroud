---
type: community
cohesion: 0.22
members: 10
---

# hermes/skills/i-icloud/scripts/calendar.js

**Cohesion:** 0.22 - loosely connected
**Members:** 10 nodes

## Members
- [[Cross-Turn Correlation Capability]] - concept - docs/papers/attack-teardowns-rovoblast-cross-turn.md
- [[EgressFilter.check()]] - code - gateway/security/egress_filter.py
- [[OpenAI Agent Message-Board Coordination Attack]] - concept - docs/papers/attack-teardowns-rovoblast-cross-turn.md
- [[PromptArmor Atlassian Rovo Content-Borne Injection Disclosure]] - document - docs/papers/attack-teardowns-rovoblast-cross-turn.md
- [[RovoBlast Attack (Atlassian Rovo AI)]] - concept - docs/papers/attack-teardowns-rovoblast-cross-turn.md
- [[UK AISI Rogue Agent Actions Findings]] - concept - docs/papers/attack-teardowns-rovoblast-cross-turn.md
- [[Varonis RovoBlast How One Click Triggered Atlassian's AI Assistant to Leak Data]] - document - docs/papers/attack-teardowns-rovoblast-cross-turn.md
- [[context_guard.py Provenance Tagging (ContextSegment)]] - code - gateway/security/context_guard.py
- [[egress_filter.py_is_private_ip SSRF Encoding-Bypass Bug]] - rationale - gateway/security/egress_filter.py
- [[multi_turn_tracker.py  SubagentMonitor]] - code - gateway/security/multi_turn_tracker.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/hermes/skills/i-icloud/scripts/calendarjs
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_AgentTarget]]
- 1 edge to [[_COMMUNITY_test_soc_router_coverage.py]]
- 1 edge to [[_COMMUNITY_TrustManager]]

## Top bridge nodes
- [[RovoBlast Attack (Atlassian Rovo AI)]] - degree 7, connects to 2 communities
- [[egress_filter.py_is_private_ip SSRF Encoding-Bypass Bug]] - degree 2, connects to 1 community