---
type: community
members: 11
---

# ContextSegment (3)

**Members:** 11 nodes

## Members
- [[dot-pipeline()_1]] - code - gateway/tests/test_performance.py
- [[dot-test_100_inbound_messages_under_5s()]] - code - gateway/tests/test_performance.py
- [[dot-test_100_outbound_messages_under_5s()]] - code - gateway/tests/test_performance.py
- [[dot-test_pii_inbound_latency()]] - code - gateway/tests/test_performance.py
- [[dot-test_single_inbound_under_200ms()]] - code - gateway/tests/test_performance.py
- [[dot-test_single_outbound_under_200ms()]] - code - gateway/tests/test_performance.py
- [[100 messages through process_inbound in under 5 seconds.]] - rationale - gateway/tests/test_performance.py
- [[PII-laden messages through inbound pipeline — verify redaction + timing.]] - rationale - gateway/tests/test_performance.py
- [[SecurityPipeline.process_inboundoutbound latency via the real pipeline class.]] - rationale - gateway/tests/test_performance.py
- [[Single message through SecurityPipeline.process_inbound  200ms.]] - rationale - gateway/tests/test_performance.py
- [[TestSecurityPipelineChainLatency]] - code - gateway/tests/test_performance.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/ContextSegment_3
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_ToolResultSanitizer]]
- 3 edges to [[_COMMUNITY_ApprovalQueueConfig]]
- 2 edges to [[_COMMUNITY_ContextSegment]]
- 2 edges to [[_COMMUNITY_AuditChain]]
- 2 edges to [[_COMMUNITY_TrustConfig]]

## Top bridge nodes
- [[TestSecurityPipelineChainLatency]] - degree 15, connects to 5 communities
- [[dot-pipeline()_1]] - degree 6, connects to 4 communities
