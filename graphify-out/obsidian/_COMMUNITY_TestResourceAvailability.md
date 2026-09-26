---
type: community
cohesion: 0.67
members: 3
---

# TestResourceAvailability

**Cohesion:** 0.67 - moderately connected
**Members:** 3 nodes

## Members
- [[Agent CVE Registry module (_AGENT_CVE_REGISTRIES etc.)]] - code - gateway/security/agent_cve_registry.py
- [[Registry-integrity fix fabricated CVE ids replaced with synthetic ASH refs]] - rationale - gateway/security/agent_cve_registry.py
- [[test_security_tool_entries_start_as_under_review_never_pre_claimed_mitigated]] - code - gateway/tests/test_agent_cve_registry.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestResourceAvailability
SORT file.name ASC
```
