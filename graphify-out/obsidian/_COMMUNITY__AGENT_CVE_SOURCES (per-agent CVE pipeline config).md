---
type: community
members: 1
---

# _AGENT_CVE_SOURCES (per-agent CVE pipeline config)

**Members:** 1 nodes

## Members
- [[_AGENT_CVE_SOURCES (per-agent CVE pipeline config)]] - code - gateway/security/agent_cve_registry.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/_AGENT_CVE_SOURCES_per-agent_CVE_pipeline_config
SORT file.name ASC
```
