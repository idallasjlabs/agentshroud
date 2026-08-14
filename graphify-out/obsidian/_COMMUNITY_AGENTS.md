---
type: community
members: 29
---

# AGENTS.md

**Members:** 29 nodes

## Members
- [[DAST Scan (Nuclei) Job]] - code - .github/workflows/ci.yml
- [[Docs Drift Check Job]] - code - .github/workflows/ci.yml
- [[Gateway Service]] - code - docker/docker-compose.yml
- [[Hermes Agent Service]] - code - docker/docker-compose.yml
- [[Hermes Cannot Force-Switch to Custom-Named Local Model (Gap 8)]] - rationale - docs/planning/v1.2/LOCAL_LLM_REVIEW.md
- [[Hermes Dashboard Bridge Port Wiring (9119-9120)]] - rationale - docker/docker-compose.yml
- [[Hermes Dev Workflow Skill (i-hdev)]] - document - docker/config/hermes/skills/i-hdev/SKILL.md
- [[Jira Ticket Per Dev Batch (Standing Rule)]] - rationale - docker/config/hermes/skills/i-hdev/SKILL.md
- [[LLMProxy (llm_proxy.py)]] - code - gateway/proxy/llm_proxy.py
- [[LOCAL_MODEL_ROUTES Dict]] - code - gateway/proxy/llm_proxy.py
- [[Multi-LLM Review Loop (Codex+Gemini review, Claude fixer)]] - concept - docker/config/hermes/skills/i-hdev/SKILL.md
- [[OpenClaw Bot Service]] - code - docker/docker-compose.yml
- [[OpenClaw Dev Workflow Skill (i-odev)]] - document - docker/config/hermes/skills/i-odev/SKILL.md
- [[Release Workflow_1]] - code - .github/workflows/release.yml
- [[TagVersion Sync Verification]] - rationale - .github/workflows/release.yml
- [[Three-Tier Network Segmentation (IEC 62443 FR5)]] - rationale - docker/docker-compose.yml
- [[Turbo Fieldflare Local Backend]] - concept - docs/planning/v1.2/LOCAL_LLM_REVIEW.md
- [[dockerversions.env (Vendor Version Pins)]] - code - docker/versions.env
- [[ensure_local_model_available()]] - code - scripts/switch_model.sh
- [[gateway__init__.py __version__]] - code - gateway/__init__.py
- [[hermes-openclaw-dev-workflow]] - document - docs/runbooks/hermes-openclaw-dev-workflow.md
- [[normalize_cloud_ref()]] - code - scripts/switch_model.sh
- [[preflight_local()]] - code - scripts/switch_model.sh
- [[switch_model.sh]] - code - scripts/switch_model.sh
- [[switch_model.sh script]] - code - scripts/switch_model.sh
- [[upsert_env_value()]] - code - scripts/switch_model.sh
- [[usage()_4]] - code - scripts/switch_model.sh
- [[verify_both_bots_healthy()]] - code - scripts/switch_model.sh
- [[wait_for_local_model()]] - code - scripts/switch_model.sh

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/AGENTSmd
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_docsuser-guide]]
- 1 edge to [[_COMMUNITY_Setup Docs]]
- 1 edge to [[_COMMUNITY_.githubworkflows]]

## Top bridge nodes
- [[hermes-openclaw-dev-workflow]] - degree 5, connects to 2 communities
- [[Release Workflow_1]] - degree 4, connects to 1 community