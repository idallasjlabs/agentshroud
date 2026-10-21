---
type: community
members: 3
---

# Agent CVE Registry module (_AGENT_CVE_REGISTRIES etc.)

**Members:** 3 nodes

## Members
- [[A2APolicyEngine (gatewaysecuritya2a_policy.py)]] - concept - CHANGELOG.md
- [[A2AProxy (gatewayproxya2a_proxy.py)]] - concept - CHANGELOG.md
- [[v1.5.0 A2A Governance]] - document - CHANGELOG.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Agent_CVE_Registry_module__AGENT_CVE_REGISTRIES_etc
SORT file.name ASC
```
