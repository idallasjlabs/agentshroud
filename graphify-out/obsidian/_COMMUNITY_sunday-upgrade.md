---
type: community
cohesion: 0.19
members: 14
---

# sunday-upgrade.md

**Cohesion:** 0.19 - loosely connected
**Members:** 14 nodes

## Members
- [[AgentShroud-Side Remediation (Arm 2)]] - concept - prompts/sunday-upgrade.md
- [[Seven-Week No-Op Upgrade Failure (PASS reported while upgrading nothing)]] - rationale - prompts/sunday-upgrade.md
- [[State-Change-Not-Steps Mandate]] - concept - prompts/sunday-upgrade.md
- [[Sunday Run Jira Tracking Procedure]] - concept - prompts/sunday-upgrade.md
- [[Tests for scriptsdiscover_upstream_versions.py — latest-release discovery.  Cop]] - rationale - gateway/tests/test_discover_upstream_versions.py
- [[is_stable]] - code - scripts/discover_upstream_versions.py
- [[pick_latest_hermes_tag]] - code - scripts/discover_upstream_versions.py
- [[pick_latest_stable]] - code - scripts/discover_upstream_versions.py
- [[plan_remediation]] - code - scripts/auto_remediate_cves.py
- [[scriptsdiscover_upstream_versions.py]] - concept - prompts/sunday-upgrade.md
- [[scriptssunday-upgrade-apply.sh]] - concept - prompts/sunday-upgrade.md
- [[scriptstriage-cve-mitigations.py]] - concept - prompts/sunday-upgrade.md
- [[sunday-upgrade]] - document - prompts/sunday-upgrade.md
- [[test_discover_upstream_versions.py_1]] - code - gateway/tests/test_discover_upstream_versions.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/sunday-upgrademd
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_auto_remediate_cves.py]]
- 2 edges to [[_COMMUNITY_check-vendor-compat.sh]]
- 1 edge to [[_COMMUNITY_plan_remediation()]]
- 1 edge to [[_COMMUNITY_discover_upstream_versions.py]]
- 1 edge to [[_COMMUNITY_pick_latest_hermes_tag()]]
- 1 edge to [[_COMMUNITY_pick_latest_stable()]]
- 1 edge to [[_COMMUNITY__t()]]
- 1 edge to [[_COMMUNITY_ToolACLEnforcer]]

## Top bridge nodes
- [[test_discover_upstream_versions.py_1]] - degree 8, connects to 3 communities
- [[sunday-upgrade]] - degree 9, connects to 2 communities
- [[scriptssunday-upgrade-apply.sh]] - degree 4, connects to 1 community
- [[AgentShroud-Side Remediation (Arm 2)]] - degree 3, connects to 1 community
- [[scriptstriage-cve-mitigations.py]] - degree 3, connects to 1 community