---
type: community
members: 3
---

# Agentic AI Threat Intelligence Cron Prompt

**Members:** 3 nodes

## Members
- [[AI Security Standards Watch Cron Prompt]] - document - docker/config/openclaw/cron/prompts/ai-security-standards-watch.txt
- [[AI Security Standards Watch Job (OWASP  NIST AI RMF  MITRE ATLAS)]] - document - docker/config/openclaw/cron/prompts/ai-security-standards-watch.txt
- [[Agentic AI Threat Intelligence Cron Prompt]] - document - docker/config/openclaw/cron/prompts/agentic-ai-threat-intelligence.txt

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Agentic_AI_Threat_Intelligence_Cron_Prompt
SORT file.name ASC
```
