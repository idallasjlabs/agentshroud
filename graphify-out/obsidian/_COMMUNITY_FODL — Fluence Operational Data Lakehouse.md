---
type: community
cohesion: 0.38
members: 7
---

# FODL — Fluence Operational Data Lakehouse

**Cohesion:** 0.38 - loosely connected
**Members:** 7 nodes

## Members
- [[AWS Glue MCP server]] - concept - .llm_settings/docs/MCP_ADDITIONAL_SERVICES.md
- [[AWS tagging standard (CostCenter, FOD, DataRetentionTier…)]] - concept - .llm_settings/docs/AWS_AGENT_README.md
- [[CDAS — Central Data Acquisition Systems]] - concept - docker/config/hermes/skills/i-aws/SKILL.md
- [[Data platform guardrails (schemapartition stability)]] - concept - .llm_settings/scripts/CLAUDE.md
- [[FODL — Fluence Operational Data Lakehouse]] - concept - docker/config/hermes/skills/i-aws/SKILL.md
- [[FY26 40% Cost Reduction Target]] - rationale - .agents/skills/i-aws/SKILL.md
- [[FY26 Cost Reduction Plan (40% target)]] - concept - docker/config/hermes/skills/i-aws/SKILL.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/FODL__Fluence_Operational_Data_Lakehouse
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_AWS Cloud Management & FinOps Agent]]
- 1 edge to [[_COMMUNITY_AWS Cloud Management & FinOps Agent]]
- 1 edge to [[_COMMUNITY_LLM Operating Context — Isaiah Jefferson]]
- 1 edge to [[_COMMUNITY_Claude Code skill catalog (59 skills)]]
- 1 edge to [[_COMMUNITY_CICD Pipeline Advisor (README)]]

## Top bridge nodes
- [[FODL — Fluence Operational Data Lakehouse]] - degree 8, connects to 3 communities
- [[FY26 40% Cost Reduction Target]] - degree 4, connects to 1 community
- [[CDAS — Central Data Acquisition Systems]] - degree 4, connects to 1 community
- [[FY26 Cost Reduction Plan (40% target)]] - degree 3, connects to 1 community
- [[AWS tagging standard (CostCenter, FOD, DataRetentionTier…)]] - degree 2, connects to 1 community