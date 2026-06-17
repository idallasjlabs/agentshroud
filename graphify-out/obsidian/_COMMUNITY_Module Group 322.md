---
type: community
cohesion: 0.15
members: 13
---

# Module Group 322

**Cohesion:** 0.15 - loosely connected
**Members:** 13 nodes

## Members
- [[.pipeline()]] - code - gateway/tests/test_performance.py
- [[.test_100_inbound_messages_under_5s()]] - code - gateway/tests/test_performance.py
- [[.test_100_outbound_messages_under_5s()]] - code - gateway/tests/test_performance.py
- [[.test_pii_inbound_latency()]] - code - gateway/tests/test_performance.py
- [[.test_single_inbound_under_200ms()]] - code - gateway/tests/test_performance.py
- [[.test_single_outbound_under_200ms()]] - code - gateway/tests/test_performance.py
- [[100 messages through process_inbound in under 5 seconds.]] - rationale - gateway/tests/test_performance.py
- [[100 messages through process_outbound in under 5 seconds.]] - rationale - gateway/tests/test_performance.py
- [[PII-laden messages through inbound pipeline — verify redaction + timing.]] - rationale - gateway/tests/test_performance.py
- [[SecurityPipeline.process_inboundoutbound latency via the real pipeline class.]] - rationale - gateway/tests/test_performance.py
- [[Single message through SecurityPipeline.process_inbound  200ms.]] - rationale - gateway/tests/test_performance.py
- [[Single message through SecurityPipeline.process_outbound  200ms.]] - rationale - gateway/tests/test_performance.py
- [[TestSecurityPipelineChainLatency]] - code - gateway/tests/test_performance.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_322
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_Tool Result Sanitizer]]
- 2 edges to [[_COMMUNITY_Ledger Config & Test Infra]]
- 2 edges to [[_COMMUNITY_Security Pipeline & Audit Chain]]
- 2 edges to [[_COMMUNITY_Context Guard & Integrity]]
- 2 edges to [[_COMMUNITY_Progressive Trust Levels]]

## Top bridge nodes
- [[TestSecurityPipelineChainLatency]] - degree 15, connects to 5 communities
- [[.pipeline()]] - degree 6, connects to 4 communities