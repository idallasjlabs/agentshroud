---
type: community
cohesion: 0.04
members: 48
---

# Deployment (runbooks)

**Cohesion:** 0.04 - loosely connected
**Members:** 48 nodes

## Members
- [[1. Pull Latest Code]] - document - docs/runbooks/deployment.md
- [[2. Run Tests]] - document - docs/runbooks/deployment.md
- [[3. Update Dependencies (if changed)]] - document - docs/runbooks/deployment.md
- [[4. Build Containers]] - document - docs/runbooks/deployment.md
- [[4. Environment Variables]] - document - docs/planning/v1.2/LOCAL_LLM_REVIEW.md
- [[5. Deploy]] - document - docs/runbooks/deployment.md
- [[6. Verify_3]] - document - docs/runbooks/deployment.md
- [[All Environment Variables (reference)]] - document - docs/vault/03 - Configuration/All Environment Variables.md
- [[Bot Container (`agentshroud-bot`)_1]] - document - docs/vault/03 - Configuration/All Environment Variables.md
- [[Build Process]] - document - docs/vault/03 - Configuration/Dockerfile.bot.md
- [[Build Stages]] - document - docs/vault/03 - Configuration/Dockerfile.gateway.md
- [[Config Defaults (Baked In)]] - document - docs/vault/03 - Configuration/Dockerfile.bot.md
- [[Deployment Runbook — AgentShroud]] - document - docs/runbooks/deployment.md
- [[Derived (set at runtime by `config.py`)]] - document - docs/vault/03 - Configuration/All Environment Variables.md
- [[Directory Structure_1]] - document - docs/vault/03 - Configuration/Dockerfile.bot.md
- [[Dockerfile — Bot (OpenClaw)]] - document - docs/vault/03 - Configuration/Dockerfile.bot.md
- [[Dockerfile — Gateway]] - document - docs/vault/03 - Configuration/Dockerfile.gateway.md
- [[Dockerfile.bot]] - document - docs/vault/03 - Configuration/Dockerfile.bot.md
- [[Dockerfile.gateway]] - document - docs/vault/03 - Configuration/Dockerfile.gateway.md
- [[Environment Variables]] - document - docs/runbooks/deployment.md
- [[First-Time Setup]] - document - docs/runbooks/deployment.md
- [[Gateway Container (`agentshroud-gateway`)_1]] - document - docs/vault/03 - Configuration/All Environment Variables.md
- [[Image Labels (OCI)]] - document - docs/vault/03 - Configuration/Dockerfile.bot.md
- [[Image Labels (OCI)_1]] - document - docs/vault/03 - Configuration/Dockerfile.gateway.md
- [[Loaded at Startup via 1Password op-proxy]] - document - docs/vault/03 - Configuration/All Environment Variables.md
- [[Optional  Runtime]] - document - docs/vault/03 - Configuration/All Environment Variables.md
- [[Pre-installed Tools]] - document - docs/vault/03 - Configuration/Dockerfile.bot.md
- [[Pre-installed Tools_1]] - document - docs/vault/03 - Configuration/Dockerfile.gateway.md
- [[Prerequisites_8]] - document - docs/runbooks/deployment.md
- [[Quick Summary]] - document - docs/runbooks/deployment.md
- [[Related Notes_16]] - document - docs/vault/03 - Configuration/All Environment Variables.md
- [[Related Notes_17]] - document - docs/vault/03 - Configuration/Dockerfile.bot.md
- [[Related Notes_18]] - document - docs/vault/03 - Configuration/Dockerfile.gateway.md
- [[Required]] - document - docs/vault/03 - Configuration/All Environment Variables.md
- [[Required Secrets (as Docker secret files)]] - document - docs/vault/03 - Configuration/All Environment Variables.md
- [[Rolling Back]] - document - docs/runbooks/deployment.md
- [[Runtime Command]] - document - docs/vault/03 - Configuration/Dockerfile.gateway.md
- [[Scripts Copied to `usrlocalbin`]] - document - docs/vault/03 - Configuration/Dockerfile.bot.md
- [[Security Hardening_2]] - document - docs/vault/03 - Configuration/Dockerfile.gateway.md
- [[Security Notes_7]] - document - docs/vault/03 - Configuration/All Environment Variables.md
- [[Security Patches Applied at Build Time]] - document - docs/vault/03 - Configuration/Dockerfile.bot.md
- [[Set in `docker-compose.yml`]] - document - docs/vault/03 - Configuration/All Environment Variables.md
- [[Stage 1 Builder (`python3.13-slim AS builder`)]] - document - docs/vault/03 - Configuration/Dockerfile.gateway.md
- [[Stage 2 Runtime (`python3.13-slim`)]] - document - docs/vault/03 - Configuration/Dockerfile.gateway.md
- [[Standard Deployment]] - document - docs/runbooks/deployment.md
- [[Summary_22]] - document - docs/vault/03 - Configuration/All Environment Variables.md
- [[TODO (from source)]] - document - docs/vault/03 - Configuration/Dockerfile.bot.md
- [[Version Tagging]] - document - docs/runbooks/deployment.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Deployment_runbooks
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_Daily Cve Report (security)]]
- 1 edge to [[_COMMUNITY_Container Runtime (smoke.d)]]
- 1 edge to [[_COMMUNITY_Local Llm Review (v1.2)]]
- 1 edge to [[_COMMUNITY_Updating (operations)]]
- 1 edge to [[_COMMUNITY_Auth.py (Gateway Core)]]

## Top bridge nodes
- [[Dockerfile — Gateway]] - degree 12, connects to 2 communities
- [[Dockerfile — Bot (OpenClaw)]] - degree 13, connects to 1 community
- [[4. Environment Variables]] - degree 8, connects to 1 community
- [[Deployment Runbook — AgentShroud]] - degree 7, connects to 1 community
- [[Environment Variables]] - degree 4, connects to 1 community