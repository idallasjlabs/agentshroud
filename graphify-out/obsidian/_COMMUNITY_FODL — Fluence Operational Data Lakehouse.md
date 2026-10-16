---
type: community
cohesion: 0.15
members: 15
---

# FODL — Fluence Operational Data Lakehouse

**Cohesion:** 0.15 - loosely connected
**Members:** 15 nodes

## Members
- [[2026-05-05 agent stub cleanup (160 files removed)]] - document - .llm_settings/UPGRADE_LOG.md
- [[AWS Glue MCP server]] - concept - .llm_settings/docs/MCP_ADDITIONAL_SERVICES.md
- [[AWS tagging standard (CostCenter, FOD, DataRetentionTier…)]] - concept - .llm_settings/docs/AWS_AGENT_README.md
- [[CDAS — Central Data Acquisition Systems]] - concept - docker/config/hermes/skills/i-aws/SKILL.md
- [[Data platform guardrails (schemapartition stability)]] - concept - .llm_settings/scripts/CLAUDE.md
- [[FODL — Fluence Operational Data Lakehouse]] - concept - docker/config/hermes/skills/i-aws/SKILL.md
- [[FY26 40% Cost Reduction Target]] - rationale - .agents/skills/i-aws/SKILL.md
- [[FY26 Cost Reduction Plan (40% target)]] - concept - docker/config/hermes/skills/i-aws/SKILL.md
- [[Gemini standalone-mode recursion fix]] - rationale - .llm_settings/UPGRADE_LOG.md
- [[Governance & risk doctrine (ITIL v4, ISO 200009001, NIST CSF)]] - concept - .llm_settings/scripts/CLAUDE.md
- [[LLM Operating Context — Isaiah Jefferson]] - concept - .llm_settings/scripts/CLAUDE.md
- [[MCP server expansion (3 → 11) and --mcp flag]] - document - .llm_settings/UPGRADE_LOG.md
- [[Normalized domain glossary (BESS, DAS, FODL, PKEOKE, FOD)]] - concept - .llm_settings/scripts/CLAUDE.md
- [[Zabbix MCP server]] - concept - .llm_settings/docs/MCP_ADDITIONAL_SERVICES.md
- [[llm-init.sh — project-level multi-tool config deployment]] - concept - .llm_settings/scripts/README.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/FODL__Fluence_Operational_Data_Lakehouse
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_AWS Cloud Management & FinOps Agent_2]]
- 1 edge to [[_COMMUNITY_AWS Cloud Management & FinOps Agent_1]]
- 1 edge to [[_COMMUNITY_Claude Code skill catalog (59 skills)]]
- 1 edge to [[_COMMUNITY_CICD Pipeline Advisor (SKILL)]]
- 1 edge to [[_COMMUNITY_awslabs.aws-api-mcp-server configuration (--readonly)]]

## Top bridge nodes
- [[FODL — Fluence Operational Data Lakehouse]] - degree 8, connects to 2 communities
- [[FY26 40% Cost Reduction Target]] - degree 4, connects to 1 community
- [[CDAS — Central Data Acquisition Systems]] - degree 4, connects to 1 community
- [[LLM Operating Context — Isaiah Jefferson]] - degree 4, connects to 1 community
- [[FY26 Cost Reduction Plan (40% target)]] - degree 3, connects to 1 community
