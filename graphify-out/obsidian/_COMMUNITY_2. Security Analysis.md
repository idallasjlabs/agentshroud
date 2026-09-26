---
type: community
cohesion: 0.14
members: 14
---

# 2. Security Analysis

**Cohesion:** 0.14 - loosely connected
**Members:** 14 nodes

## Members
- [[0. Preflight (both environments)]] - document - prompts/sunday-upgrade.md
- [[1. Inventory]] - document - prompts/sunday-upgrade.md
- [[2b. AgentShroud-side remediation — the vendor's fix is NOT the finish line]] - document - prompts/sunday-upgrade.md
- [[3. Upgrade DEV]] - document - prompts/sunday-upgrade.md
- [[4. Promote to PROD]] - document - prompts/sunday-upgrade.md
- [[5. Cleanup]] - document - prompts/sunday-upgrade.md
- [[6. Jira tracking (standard procedure, owner directive 2026-08-30)]] - document - prompts/sunday-upgrade.md
- [[7. Report]] - document - prompts/sunday-upgrade.md
- [[AgentShroud Weekly Upgrade — Sunday Maintenance Run]] - document - prompts/sunday-upgrade.md
- [[Cross-account reality (marvin)]] - document - prompts/sunday-upgrade.md
- [[Ground rules]] - document - prompts/sunday-upgrade.md
- [[Procedure_1]] - document - prompts/sunday-upgrade.md
- [[THE RUN IS JUDGED ON STATE CHANGE, NOT ON STEPS COMPLETED]] - document - prompts/sunday-upgrade.md
- [[USE THE DETERMINISTIC SCRIPT — do not improvise these steps]] - document - prompts/sunday-upgrade.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/2_Security_Analysis
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY__process_inbound()]]
- 1 edge to [[_COMMUNITY_OutputSchemaEnforcer]]
- 1 edge to [[_COMMUNITY_TestEgressTargetExtraction]]

## Top bridge nodes
- [[AgentShroud Weekly Upgrade — Sunday Maintenance Run]] - degree 7, connects to 2 communities
- [[Procedure_1]] - degree 10, connects to 1 community